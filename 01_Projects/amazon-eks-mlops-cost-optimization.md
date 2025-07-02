---
title: "[PRO] Amazon EKS 기반 MLOps 인프라 비용 최적화"
tags: [EKS, Karpenter, Knative, MLOps, CostOptimization]
created: 2025-04-23T06:50:00.000Z
updated: 2025-06-26T08:35:00.000Z
parent: "[PRO] AI 활용해서 1인 개발부터 창업까지"
children: 
  - "[DEV] 실제 구현"
  - "[DEV] 아키텍처 설계"  
  - "[DEV] EKS 클러스터 리소스 효율성 해결"
url: "https://www.notion.so/PRO-Amazon-EKS-MLOps-1de393a5a7978061b68fd78fbb2b353b"
public_url: "https://maroon-redcurrant-7c5.notion.site/PRO-Amazon-EKS-MLOps-1de393a5a7978061b68fd78fbb2b353b"
notion_id: "1de393a5-a797-8061-b68f-d78fbb2b353b"
category: "project"
level: 1
---

# [PRO] Amazon EKS 기반 MLOps 인프라 비용 최적화

## 문제 인식

- 평소 사용하지 않는 서비스(pod) 때문에 불필요한 서버(node) 운영으로 인한 서버 비용 발생

## 목표

- Knative와 Karpenter를 이용해, 유휴 상태의 서비스를 자동으로 중지하고, 트래픽 발생 시 자동으로 확장되는 이벤트 기반 스케일링 환경 구축

---

## 관련 기술 스택

- **Kubernetes**: Amazon EKS
- **Auto Scaling**: Karpenter (Node-level), Knative (Pod-level)
- **Cost Optimization**: Spot 인스턴스, Event-driven scaling
- **MLOps**: 서버리스 ML 서비스 운영

## 프로젝트 구조

이 프로젝트는 다음과 같은 하위 구성 요소들로 나뉩니다:

1. **[DEV] 실제 구현** - 구현 세부사항과 실제 코드
2. **[DEV] 아키텍처 설계** - 시스템 아키텍처 설계 문서  
3. **[DEV] EKS 클러스터 리소스 효율성 해결** - 리소스 최적화 방안

## 기대 효과

- **비용 절감**: 유휴 리소스 자동 정리를 통한 AWS 비용 최적화
- **운영 효율성**: 트래픽 기반 자동 스케일링으로 수동 관리 부담 감소
- **MLOps 자동화**: 이벤트 드리븐 ML 서비스 운영 환경 구축

## 학습 포인트

이 프로젝트를 통해 다음을 학습할 수 있습니다:

- Kubernetes 네이티브 도구들의 실무 활용법
- 클라우드 비용 최적화 전략과 실제 구현 방법
- MLOps 인프라의 현실적인 운영 노하우
- 이벤트 기반 아키텍처의 실제 적용 사례

---

*이 문서는 실제 프로덕션 환경에서의 경험을 바탕으로 작성되었습니다.*