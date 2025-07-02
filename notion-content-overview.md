# HoneyDanji 기술 블로그 - Notion 콘텐츠 개요

## 📋 개요

이 문서는 Notion 기술 블로그 데이터베이스에서 수집한 70+ 개의 기술 문서를 체계적으로 정리한 것입니다. MLOps, Kubernetes, AWS EKS 환경에서의 실제 운영 경험과 문제 해결 과정을 중심으로 구성되어 있습니다.

## 🗂️ 디렉토리 구조

### 01_Projects (PRO)
프로덕션 환경에서 진행된 주요 프로젝트들

- **[amazon-eks-mlops-cost-optimization.md](./01_Projects/amazon-eks-mlops-cost-optimization.md)** - Amazon EKS 기반 MLOps 인프라 비용 최적화
- 유기동물 입양 추천 시스템
- AI 활용 1인 개발부터 창업까지

### 02_Development (DEV)  
개발 과정과 구현 세부사항

- **[eks-cluster-resource-efficiency.md](./02_Development/eks-cluster-resource-efficiency.md)** - EKS 클러스터 리소스 효율성 해결
- FastAPI + SQLAlchemy 비동기 설정
- FastAPI + Celery 설정
- Middleware 활용 요청별 session 관리

### 03_Troubleshooting (TB)
실제 마주한 문제들과 해결 과정

- **[cursor-ssh-remote-ec2-connection-issues.md](./03_Troubleshooting/cursor-ssh-remote-ec2-connection-issues.md)** - Cursor SSH Remote EC2 접속 오류 해결
- EKS 치명적인 오류 해결
- ColdStart 문제 해결
- Knative 프로비저닝 문제
- ALB - Grafana 라우팅 문제 해결

### 04_Study (STDY)
기술 학습 및 연구 내용

- **[fastapi-mcp-usage.md](./04_Study/fastapi-mcp-usage.md)** - FastAPI MCP 사용법
- Kubernetes 학습 노트
- SQLAlchemy ORM vs Raw SQL 비교

### 05_Ideas (IDEA)
미래 프로젝트 아이디어와 기술적 가능성

- **[python-virtual-env-copilot-assignment.md](./05_Ideas/python-virtual-env-copilot-assignment.md)** - 파이썬 가상환경별 코파일럿 지정 아이디어
- MCP + Claude 통합 아이디어
- n8n 활용 디자인 자동화
- n8n + MCP + Claude 결합

### 06_AI_Tools
AI 도구 활용법과 실용적인 프롬프트

- **[zero-capital-ai-monetization-prompts.md](./06_AI_Tools/zero-capital-ai-monetization-prompts.md)** - 무자본 AI 수익화 프롬프트 모음
- ChatGPT 활용법
- Claude 사용 경험
- Perplexity 활용 사례

## 🏷️ 주요 태그

### 기술 스택
- **EKS, Kubernetes**: Amazon EKS 기반 MLOps 인프라
- **Karpenter, Knative**: 자동 스케일링과 서버리스
- **FastAPI, SQLAlchemy**: Python 백엔드 개발
- **AWS**: 클라우드 인프라 및 서비스

### 카테고리별 분류
- **MLOps**: 머신러닝 운영 자동화
- **CostOptimization**: 클라우드 비용 최적화
- **Troubleshooting**: 문제 해결 과정
- **Development**: 개발 구현 과정
- **AI Tools**: AI 활용 및 자동화

## 📈 주요 성과

### 비용 최적화
- **70% 비용 절감**: Spot 인스턴스와 자동 스케일링 활용
- **리소스 효율성**: 유휴 리소스 자동 정리 시스템 구축

### 기술적 성취
- **이벤트 기반 스케일링**: Knative와 Karpenter 통합
- **완전 자동화**: GitOps 기반 배포 파이프라인
- **실시간 모니터링**: Prometheus + Grafana 구축

### 실무 경험
- **프로덕션 검증**: 실제 운영 환경에서의 검증된 솔루션
- **문제 해결**: 구체적인 문제 상황과 해결 과정 기록
- **비용 중심 사고**: 기술적 완성도와 비즈니스 가치의 균형

## 🔍 빠른 찾기

### 인기 문서
1. [Amazon EKS MLOps 비용 최적화](./01_Projects/amazon-eks-mlops-cost-optimization.md) - 70% 비용 절감 사례
2. [AI 수익화 프롬프트](./06_AI_Tools/zero-capital-ai-monetization-prompts.md) - 실용적인 AI 활용법
3. [Cursor SSH 문제 해결](./03_Troubleshooting/cursor-ssh-remote-ec2-connection-issues.md) - 개발 환경 이슈 해결

### 카테고리별 링크
- [프로젝트 목록](./taxonomy.md#projects) - 완료된 주요 프로젝트들
- [문제 해결 사례](./taxonomy.md#troubleshooting) - 실제 트러블슈팅 경험
- [학습 자료](./taxonomy.md#study) - 기술 학습 노트
- [아이디어 모음](./taxonomy.md#ideas) - 미래 프로젝트 아이디어

## 📊 통계

- **총 문서 수**: 70+ 페이지
- **주요 카테고리**: 6개 분야
- **실무 프로젝트**: 10+ 개
- **문제 해결 사례**: 15+ 개
- **기술 스택**: AWS, Kubernetes, Python, AI Tools

## 🎯 활용 방안

### 개발자를 위한 가이드
- MLOps 엔지니어 또는 Platform Engineer 학습 자료
- 클라우드 비용 최적화 실행 방안
- 실제 프로덕션 환경 운영 노하우

### 비즈니스 가치
- 스타트업/중소기업 효율적 ML 인프라 구축
- 클라우드 비용 최적화 구체적 방법론
- AI 도구 활용을 통한 생산성 향상

## 📞 연락처

이 블로그의 내용에 대한 질문이나 협업 제안이 있으시면 언제든 연락해 주세요.

---

## 📑 관련 문서

- [taxonomy.md](./taxonomy.md) - 태그 기반 문서 분류
- [hierarchy.md](./hierarchy.md) - 계층 구조 및 관계도
- [all_pages_data.json](./all_pages_data.json) - 전체 데이터 (JSON 형식)

---

*최종 업데이트: 2025-07-02*  
*데이터 소스: Notion 기술블로그 데이터베이스*  
*총 수집 페이지: 70+ 문서*