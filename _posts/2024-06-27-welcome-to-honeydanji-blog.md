---
layout: post
title: "안녕하세요, HoneyDanji입니다! 🚀"
date: 2024-06-27 14:00:00 +0900
categories: [블로그, 소개]
tags: [welcome, kubernetes, mlops, aws, devops, backend, 자기소개]
author: HoneyDanji
excerpt: "안녕하세요! 클라우드 네이티브 기술과 MLOps를 전문으로 하는 백엔드 개발자 HoneyDanji입니다. Kubernetes와 AWS를 활용한 대규모 시스템 구축 경험과 앞으로 이 블로그에서 공유하고 싶은 이야기들을 소개합니다."
---

# 안녕하세요, HoneyDanji입니다! 🚀

**HoneyDanji 기술 블로그**에 오신 것을 환영합니다!

저는 **클라우드 네이티브 기술과 MLOps**에 깊은 관심을 가지고 있는 백엔드 개발자입니다. 복잡한 분산 시스템을 설계하고 구축하는 것을 좋아하며, 특히 Kubernetes 생태계에서 대규모 서비스를 운영하는 일에 열정을 가지고 있습니다.

## 🛠️ 제가 다루는 기술들

### **클라우드 & 인프라**
현재 **AWS EKS 기반의 Kubernetes 클러스터**에서 대부분의 작업을 하고 있습니다. 단순히 Pod를 띄우는 것을 넘어서, **ArgoCD를 통한 GitOps 배포**, **Karpenter로 노드 자동 스케일링**, **Istio 서비스 메시** 등을 활용한 프로덕션 환경을 구축하고 운영합니다.

```yaml
# 이런 식의 복잡한 인프라 구성을 다룹니다
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: gpu-nodes
spec:
  requirements:
    - key: karpenter.sh/capacity-type
      operator: In
      values: ["spot", "on-demand"]
    - key: node.kubernetes.io/instance-type
      operator: In
      values: ["g4dn.xlarge", "g5.xlarge", "p3.2xlarge"]
```

### **MLOps & AI 인프라**
머신러닝 모델을 프로덕션에서 서빙하고 관리하는 일을 주로 합니다. **KServe**로 모델 추론 서비스를 구축하고, **Kubeflow Pipelines**로 ML 워크플로우를 자동화하며, **Label Studio** 같은 도구들을 Kubernetes 환경에 통합해서 엔드투엔드 ML 파이프라인을 만들어왔습니다.

물론 이런 오픈소스 도구들의 자세한 사용법은 각각의 GitHub 저장소에서 더 잘 설명되어 있습니다. 저는 이들을 **실제 프로덕션 환경에서 어떻게 조합하고 운영하는지**에 대한 경험을 가지고 있습니다.

### **백엔드 개발**
- **Python**: FastAPI를 주로 사용하며, 비동기 처리와 대용량 데이터 처리에 익숙합니다

### **DevOps & 자동화**
- **AWS**: EC2, S3, RDS, Lambda 등 다양한 서비스 경험, 특히 **EC2 Spot 인스턴스**를 활용한 비용 최적화
- **컨테이너**: Docker, Kubernetes, Helm 차트 작성
- **CI/CD**: GitHub Actions, ArgoCD를 통한 완전 자동화된 배포 파이프라인
- **모니터링**: Prometheus, Grafana, CloudWatch를 활용한 시스템 관찰성

## 💡 최근에 작업한 것들

### **GPU 기반 AI 추론 플랫폼**
DINO(Detection Transformer) 모델을 활용한 이미지 분류 서비스를 구축했습니다. 단순히 모델을 배포하는 것을 넘어서, **동적으로 GPU 인스턴스를 생성하고 종료하는 시스템**을 만들어 비용을 크게 절약했습니다.

특히 **AWS Lambda + EC2 Spot 인스턴스** 조합으로 필요할 때만 GPU 서버를 띄우고, 훈련 완료 후 자동으로 정리하는 구조를 만들었습니다. 기존 상시 운영 대비 **70% 비용 절감** 효과를 얻었습니다.

### **완전 자동화된 ML 파이프라인**
데이터 과학자가 "모델을 새로 훈련시키고 싶다"고 하면, 버튼 하나로 전체 과정이 자동화되는 시스템을 구축했습니다:

1. **Slack 알림**: 훈련 시작을 팀에 알림
2. **검증**: S3에서 필요한 파일들이 준비되었는지 확인
3. **인프라 생성**: AWS Lambda로 GPU 인스턴스 동적 생성
4. **훈련 실행**: 컨테이너 기반으로 격리된 환경에서 모델 훈련
5. **완료 알림**: 성공/실패 여부를 다시 Slack으로 알림

이 모든 과정이 **Kubeflow Pipelines**로 시각화되어 있어서 어느 단계에서 문제가 생겼는지 바로 확인할 수 있습니다.

### **데이터 라벨링 자동화**
**Label Studio**를 Kubernetes에 배포하고, 우리가 훈련한 DINO 모델을 ML Backend로 연결해서 **자동 어노테이션** 기능을 구현했습니다. 사람이 처음부터 라벨링하는 것이 아니라, 모델이 먼저 예측을 해주고 사람이 검토하고 수정하는 **Human-in-the-loop** 방식으로 작업 효율성을 크게 높였습니다.

## 🎯 이 블로그에서 다룰 내용들

### **실제 운영 경험 공유**
오픈소스 도구들의 기본적인 사용법은 각 프로젝트의 문서에서 더 잘 설명되어 있습니다. 저는 이런 도구들을 **실제 프로덕션 환경에서 조합해서 사용할 때의 노하우**를 공유하고 싶습니다.

- KServe의 콜드 스타트 문제를 어떻게 해결했는지
- Spot 인스턴스 중단에 대비한 체크포인트 전략
- Kubernetes에서 GPU 리소스를 효율적으로 관리하는 방법
- 비용 최적화를 위한 실제 전략들

### **문제 해결 과정**
단순한 튜토리얼이 아니라, **실제로 마주한 문제들과 해결 과정**을 솔직하게 공유하겠습니다.

- "왜 g4dn.xlarge와 g5.xlarge 중에 어떤 걸 선택해야 할까?"
- "S3 전송 속도가 너무 느린데 어떻게 개선할까?"
- "모니터링 메트릭이 너무 많은데 정말 중요한 건 뭘까?"

### **기술 선택의 이유**
새로운 기술을 도입할 때의 **의사결정 과정**도 공유하고 싶습니다.

- Kubeflow vs MLflow vs 직접 구축, 어떤 기준으로 선택했는지
- ArgoCD vs Flux, GitOps 도구 선택 경험
- PostgreSQL vs MongoDB, 상황별 데이터베이스 선택 기준

## 🌟 앞으로의 관심사

### **플랫폼 엔지니어링**
최근 **Platform Engineering**이라는 개념에 깊은 관심을 가지고 있습니다. 개발자들이 인프라 복잡성에 신경쓰지 않고 비즈니스 로직에만 집중할 수 있는 환경을 만드는 것이 목표입니다.

### **FinOps**
클라우드 비용을 단순히 줄이는 것이 아니라, **비즈니스 가치와 비용의 균형**을 찾는 것에 관심이 있습니다. Spot 인스턴스, 예약 인스턴스, 리소스 right-sizing 등의 실전 경험을 공유하고 싶습니다.

### **오픈소스 기여**
사용하고 있는 오픈소스 프로젝트들에 더 적극적으로 기여하고 싶습니다. 특히 Kubernetes 생태계의 도구들이 실제 프로덕션에서 더 잘 동작할 수 있도록 피드백하고 개선사항을 제안하고 싶습니다.

## 🤝 함께 성장해요

이 블로그를 통해 제가 경험한 것들을 공유하면서, 비슷한 고민을 하고 있는 분들과 소통하고 싶습니다.

- **실무에서 마주한 구체적인 문제들**과 해결 과정
- **기술 선택의 이유**와 트레이드오프
- **비용 최적화**와 성능 튜닝 경험
- **팀 워크플로우** 개선 사례들

### **연락처**
궁금한 점이나 함께 논의하고 싶은 주제가 있으시면 언제든 연락주세요!

- **GitHub**: [github.com/honeydanji](https://github.com/honeydanji)
- **LinkedIn**: [linkedin.com/in/honeydanji](https://www.linkedin.com/in/%EC%84%B1%EC%A7%84-%ED%95%98-a53151302/)
- **Email**: ekswl3680@gmail.com

---

**앞으로 이런 주제들을 다룰 예정입니다:**

- *"프로덕션에서 KServe 운영하며 마주한 5가지 문제와 해결책"*
- *"AWS Spot 인스턴스로 ML 훈련 비용 70% 절약한 방법"*
- *"Kubernetes에서 GPU 리소스 효율적으로 관리하기"*
- *"ArgoCD + Kustomize로 멀티 환경 배포 자동화하기"*

지속적으로 유용한 콘텐츠로 찾아뵙겠습니다. 많은 관심과 응원 부탁드려요! 🙌

---

*이 블로그는 Jekyll과 GitHub Pages를 이용해 구축되었으며, 모든 포스트는 실제 경험을 바탕으로 작성됩니다.*