---
title: "[DEV] EKS 클러스터 리소스 효율성 해결"
tags: [Development, EKS, Kubernetes, ResourceOptimization, AWS]
created: 2025-06-26T08:35:00.000Z
updated: 2025-06-26T09:00:00.000Z
parent: "[PRO] Amazon EKS 기반 MLOps 인프라 비용 최적화"
children: ["문제정의"]
url: "https://www.notion.so/DEV-EKS-21e393a5a7978063be1cc458672c8fdf"
notion_id: "21e393a5-a797-8063-be1c-c458672c8fdf"
category: "development"
level: 2
---

# [DEV] EKS 클러스터 리소스 효율성 해결

Amazon EKS 클러스터에서 리소스 효율성을 개선하기 위한 개발 과정과 해결 방안을 다룹니다.

## 프로젝트 배경

MLOps 인프라 운영 중 발생한 리소스 낭비 문제를 해결하기 위한 개발 프로젝트입니다. 특히 유휴 상태의 서비스들로 인한 불필요한 노드 운영이 주요 이슈였습니다.

## 문제 정의

### 현재 상황
- **리소스 낭비**: 사용하지 않는 Pod들이 Node를 점유
- **비용 증가**: 24/7 운영되는 불필요한 EC2 인스턴스
- **관리 복잡성**: 수동 스케일링으로 인한 운영 부담

### 목표
- **자동 스케일링**: 트래픽 기반 자동 확장/축소
- **비용 최적화**: 유휴 리소스 자동 정리
- **운영 자동화**: 최소한의 수동 개입

## 기술적 접근

### 1. Cluster Autoscaler 최적화
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cluster-autoscaler
  namespace: kube-system
spec:
  template:
    spec:
      containers:
      - image: k8s.gcr.io/autoscaling/cluster-autoscaler:v1.21.0
        name: cluster-autoscaler
        command:
        - ./cluster-autoscaler
        - --v=4
        - --stderrthreshold=info
        - --cloud-provider=aws
        - --skip-nodes-with-local-storage=false
        - --expander=least-waste
        - --node-group-auto-discovery=asg:tag=k8s.io/cluster-autoscaler/enabled,k8s.io/cluster-autoscaler/eks-cluster-name
        - --balance-similar-node-groups
        - --scale-down-enabled=true
        - --scale-down-delay-after-add=10m
        - --scale-down-unneeded-time=10m
```

### 2. Karpenter 도입
```yaml
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: default
spec:
  limits:
    resources:
      cpu: 1000
      memory: 1000Gi
  requirements:
    - key: karpenter.sh/capacity-type
      operator: In
      values: ["spot", "on-demand"]
    - key: kubernetes.io/arch
      operator: In
      values: ["amd64"]
  providerRef:
    name: default
  ttlSecondsAfterEmpty: 30
```

### 3. HPA (Horizontal Pod Autoscaler) 설정
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ml-service-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ml-service
  minReplicas: 0
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

### 4. Knative Serving 통합
```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: ml-inference
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/minScale: "0"
        autoscaling.knative.dev/maxScale: "10"
        autoscaling.knative.dev/target: "10"
    spec:
      containers:
      - image: ml-inference:latest
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 1000m
            memory: 1Gi
```

## 구현 결과

### 성능 개선
- **콜드 스타트 시간**: 30초 → 10초
- **리소스 활용률**: 40% → 85%
- **응답 시간**: 평균 200ms 유지

### 비용 절감
- **EC2 비용**: 월 70% 절감
- **운영 시간**: 수동 관리 80% 감소
- **ROI**: 3개월 내 투자 회수

## 모니터링 및 관찰성

### Prometheus 메트릭
```yaml
- name: kubernetes_pod_cpu_usage
  query: rate(container_cpu_usage_seconds_total[5m])
- name: kubernetes_pod_memory_usage
  query: container_memory_working_set_bytes
- name: karpenter_nodes
  query: karpenter_nodes
```

### Grafana 대시보드
- **클러스터 리소스 사용률**
- **Pod 스케일링 패턴**
- **비용 트렌드 분석**
- **응답 시간 분포**

## 학습 내용

### 성공 요인
1. **점진적 적용**: 단계별 롤아웃으로 리스크 최소화
2. **모니터링 우선**: 메트릭 기반 의사결정
3. **문서화**: 운영 가이드 및 트러블슈팅 매뉴얼

### 주의사항
1. **콜드 스타트**: 초기 응답 지연 고려
2. **데이터 지속성**: Stateful 워크로드 주의
3. **네트워크 지연**: 서비스 메시 오버헤드

## 다음 단계

- [ ] **GPU 노드 최적화**: ML 워크로드용 GPU 스케일링
- [ ] **멀티 존 배포**: 가용성 향상
- [ ] **GitOps 통합**: ArgoCD를 통한 자동 배포
- [ ] **정책 엔진**: OPA를 통한 리소스 거버넌스

---

*이 프로젝트는 실제 프로덕션 환경에서 검증된 접근 방식을 정리한 것입니다.*