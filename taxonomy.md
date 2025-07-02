# 기술 블로그 분류 체계 (Taxonomy)

## 📊 태그 기반 문서 분류

이 문서는 Notion 기술 블로그의 모든 콘텐츠를 태그와 카테고리별로 체계적으로 분류한 것입니다.

## 🗂️ 주요 카테고리

### Projects (PRO)
프로덕션 환경에서 진행된 실무 프로젝트들

#### MLOps 및 클라우드 인프라
- **[Amazon EKS 기반 MLOps 인프라 비용 최적화](./01_Projects/amazon-eks-mlops-cost-optimization.md)**
  - 태그: `EKS`, `Karpenter`, `Knative`, `MLOps`, `CostOptimization`
  - 성과: 70% 비용 절감, 자동 스케일링 구현
  - 난이도: ⭐⭐⭐⭐⭐

#### AI 서비스 개발
- **유기동물 입양 추천 시스템**
  - 태그: `AI`, `MachineLearning`, `RecommendationSystem`
  - 상태: 진행 중 (Interruption)
  - 난이도: ⭐⭐⭐⭐

#### 창업 및 비즈니스
- **AI 활용해서 1인 개발부터 창업까지**
  - 태그: `Startup`, `AI`, `Business`
  - 목표: AI 기반 1인 개발 워크플로우 구축
  - 난이도: ⭐⭐⭐

### Development (DEV)
개발 과정과 구현 세부사항

#### 인프라 개발
- **[EKS 클러스터 리소스 효율성 해결](./02_Development/eks-cluster-resource-efficiency.md)**
  - 태그: `EKS`, `Kubernetes`, `ResourceOptimization`
  - 기술: Cluster Autoscaler, Karpenter, HPA
  - 난이도: ⭐⭐⭐⭐

#### 백엔드 개발
- **FastAPI + SQLAlchemy 비동기 설정**
  - 태그: `FastAPI`, `SQLAlchemy`, `AsyncProgramming`
  - 기술: 비동기 데이터베이스 연결, ORM 최적화
  - 난이도: ⭐⭐⭐

- **FastAPI + Celery 설정**
  - 태그: `FastAPI`, `Celery`, `TaskQueue`
  - 기술: 비동기 작업 처리, 백그라운드 작업
  - 난이도: ⭐⭐⭐

- **Middleware 활용 요청별 session 관리**
  - 태그: `FastAPI`, `Middleware`, `SessionManagement`
  - 기술: 커스텀 미들웨어, 세션 관리
  - 난이도: ⭐⭐

### Troubleshooting (TB)
실제 마주한 문제들과 해결 과정

#### 개발 환경 이슈
- **[Cursor SSH Remote EC2 접속 오류](./03_Troubleshooting/cursor-ssh-remote-ec2-connection-issues.md)**
  - 태그: `SSH`, `EC2`, `VSCode`, `Cursor`, `Development`
  - 문제: IDE 리소스 오버헤드로 인한 접속 불안정
  - 해결: 툴 특성 이해 및 적절한 대안 선택
  - 난이도: ⭐⭐

#### 클라우드 인프라 이슈
- **EKS 치명적인 오류**
  - 태그: `EKS`, `Kubernetes`, `Troubleshooting`
  - 상태: 해결 완료
  - 난이도: ⭐⭐⭐⭐⭐

- **ColdStart 문제**
  - 태그: `EKS`, `Knative`, `ColdStart`, `Performance`
  - 문제: 서버리스 환경에서의 콜드 스타트 지연
  - 난이도: ⭐⭐⭐⭐

- **Knative 프로비저닝 문제**
  - 태그: `EKS`, `Knative`, `Provisioning`
  - 문제: 리소스 프로비저닝 실패
  - 난이도: ⭐⭐⭐⭐

- **ALB - Grafana 라우팅 문제**
  - 태그: `EKS`, `Grafana`, `ALB`, `Routing`
  - 문제: 로드 밸런서 라우팅 설정 오류
  - 난이도: ⭐⭐⭐

### Study (STDY)
기술 학습 및 연구 내용

#### API 개발
- **[FastAPI MCP 사용](./04_Study/fastapi-mcp-usage.md)**
  - 태그: `FastAPI`, `MCP`, `API`, `Development`
  - 내용: Model Context Protocol과 FastAPI 통합
  - 레벨: 중급

#### 인프라 학습
- **Kubernetes 학습 노트**
  - 태그: `Kubernetes`, `ContainerOrchestration`
  - 내용: 기본 개념부터 고급 운영까지
  - 레벨: 초급-고급

#### 데이터베이스
- **SQLAlchemy ORM vs Raw SQL 비교**
  - 태그: `SQLAlchemy`, `Database`, `Performance`
  - 내용: ORM과 Raw SQL의 성능 비교 분석
  - 레벨: 중급

### Ideas (IDEA)
미래 프로젝트 아이디어와 기술적 가능성

#### 개발 도구 혁신
- **[파이썬 가상환경별 코파일럿 지정](./05_Ideas/python-virtual-env-copilot-assignment.md)**
  - 태그: `Python`, `VirtualEnv`, `Copilot`, `ProductIdea`
  - 아이디어: 프로젝트별 맞춤형 AI 코딩 어시스턴트
  - 잠재성: ⭐⭐⭐⭐⭐

#### AI 통합 솔루션
- **MCP + Claude 통합**
  - 태그: `MCP`, `Claude`, `AIIntegration`
  - 아이디어: Model Context Protocol과 Claude 결합
  - 잠재성: ⭐⭐⭐⭐

#### 자동화 도구
- **n8n 활용 디자인 자동화**
  - 태그: `n8n`, `Automation`, `Design`
  - 아이디어: 워크플로우 자동화를 통한 디자인 프로세스 개선
  - 잠재성: ⭐⭐⭐

- **n8n + MCP + Claude 결합**
  - 태그: `n8n`, `MCP`, `Claude`, `Automation`
  - 아이디어: 완전 자동화된 AI 워크플로우
  - 잠재성: ⭐⭐⭐⭐⭐

### AI_Tools
AI 도구 활용법과 실용적인 프롬프트

#### 비즈니스 활용
- **[무자본 AI 수익화 프롬프트](./06_AI_Tools/zero-capital-ai-monetization-prompts.md)**
  - 태그: `AI`, `ChatGPT`, `Monetization`, `Prompts`, `BusinessStrategy`
  - 내용: 실용적인 AI 활용 프롬프트 7가지
  - 활용도: ⭐⭐⭐⭐⭐

#### AI 플랫폼별 활용
- **ChatGPT 활용법**
  - 태그: `ChatGPT`, `Prompts`, `Productivity`
  - 내용: 효과적인 프롬프트 작성법
  - 활용도: ⭐⭐⭐⭐

- **Claude 사용 경험**
  - 태그: `Claude`, `CodeGeneration`, `Development`
  - 내용: 개발 도구로서의 Claude 활용
  - 활용도: ⭐⭐⭐⭐

- **Perplexity 활용 사례**
  - 태그: `Perplexity`, `Research`, `Information`
  - 내용: 리서치 도구로서의 Perplexity 활용
  - 활용도: ⭐⭐⭐

## 🏷️ 태그별 인덱스

### 기술 스택 태그

#### 클라우드 & 인프라
- `AWS` (15+ 문서)
- `EKS` (12+ 문서) 
- `Kubernetes` (10+ 문서)
- `EC2` (8+ 문서)
- `Karpenter` (5+ 문서)
- `Knative` (5+ 문서)

#### 개발 프레임워크
- `FastAPI` (8+ 문서)
- `SQLAlchemy` (4+ 문서)
- `Python` (15+ 문서)
- `Celery` (3+ 문서)

#### AI & 머신러닝
- `AI` (10+ 문서)
- `MLOps` (6+ 문서)
- `ChatGPT` (5+ 문서)
- `Claude` (4+ 문서)
- `MachineLearning` (5+ 문서)

#### 모니터링 & 관찰성
- `Prometheus` (3+ 문서)
- `Grafana` (4+ 문서)
- `Monitoring` (6+ 문서)

### 카테고리 태그

#### 프로젝트 타입
- `Projects` (12+ 문서)
- `Development` (15+ 문서)
- `Troubleshooting` (18+ 문서)
- `Study` (12+ 문서)
- `Ideas` (8+ 문서)

#### 난이도별 분류
- `Beginner` (8+ 문서)
- `Intermediate` (25+ 문서)
- `Advanced` (20+ 문서)
- `Expert` (10+ 문서)

#### 상태별 분류
- `완료` (40+ 문서)
- `진행중` (15+ 문서)
- `계획` (10+ 문서)
- `중단` (5+ 문서)

## 📈 인기 태그 순위

1. **EKS** (12 문서) - Amazon EKS 관련 모든 내용
2. **Troubleshooting** (18 문서) - 문제 해결 사례들
3. **AWS** (15 문서) - Amazon Web Services 활용
4. **Python** (15 문서) - Python 개발 관련
5. **AI** (10 문서) - AI 도구 및 활용법
6. **Kubernetes** (10 문서) - 컨테이너 오케스트레이션
7. **FastAPI** (8 문서) - 백엔드 API 개발
8. **MLOps** (6 문서) - 머신러닝 운영 자동화
9. **Development** (15 문서) - 개발 과정 및 구현
10. **CostOptimization** (5 문서) - 비용 최적화 전략

## 🔍 검색 가이드

### 주제별 검색
```markdown
# 클라우드 비용 최적화 관련 문서
태그: CostOptimization, AWS, EKS

# AI 도구 활용법
태그: AI, ChatGPT, Claude, Prompts

# 실무 트러블슈팅 사례
태그: Troubleshooting, Production, Issues

# 백엔드 개발 가이드
태그: FastAPI, Python, SQLAlchemy, API
```

### 난이도별 검색
```markdown
# 초보자용 문서
태그: Beginner, Tutorial, Guide

# 고급 기술 문서
태그: Advanced, Expert, Production

# 실무 경험 공유
태그: Experience, RealWorld, LessonsLearned
```

---

*이 분류 체계는 지속적으로 업데이트되며, 새로운 콘텐츠가 추가될 때마다 확장됩니다.*