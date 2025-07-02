---
title: "[TB] cursor(vscode) ssh remote로 ec2 ssh 접속 오류"
tags: [Troubleshooting, SSH, EC2, VSCode, Cursor, Development]
created: 2025-06-26T07:12:00.000Z
updated: 2025-06-26T07:13:00.000Z
parent: "관련 프로젝트"
children: []
url: "https://www.notion.so/TB-cursor-vscode-ssh-remote-ec2-ssh-21e393a5a79780e09ff3e5b0a6c572af"
notion_id: "21e393a5-a797-80e0-9ff3-e5b0a6c572af"
category: "troubleshooting"
level: 2
---

# Cursor SSH Remote 접속 이슈 완전 정복 🚀

최근 개발 환경을 모던하게 업그레이드하려다 예상치 못한 벽에 부딪혔습니다. Cursor(VS Code 기반)의 SSH Remote 기능으로 EC2에 접속하던 중 갑작스럽게 서버가 멈추는 현상이 발생했어요. 같은 이슈로 고생하실 분들을 위해 완전한 해결 가이드를 정리해봤습니다.

## 🔍 문제 상황

- **툴**: Cursor + SSH Remote Extension
- **타겟**: AWS EC2 (Bastion Server)
- **증상**: 초기 접속은 성공하지만 갑작스럽게 서버 응답 중단
- **터미널**: 특별한 에러 메시지 없음

처음엔 네트워크 이슈인 줄 알았는데, 기존에 사용하던 XShell로는 정상 접속이 되더라고요. 뭔가 Cursor 특유의 문제인 것 같아서 본격적인 디버깅에 돌입했습니다.

## 🕵️ 원인 분석

퍼플렉시티와 AWS 커뮤니티를 뒤져가며 찾아낸 핵심 원인은 두 가지였습니다:

### 1️⃣ tar 패키지 누락 이슈

```shell
# EC2에 tar 패키지가 없어서 발생하는 문제
sudo apt update
sudo apt install tar -y
```

VS Code 계열 에디터들은 SSH 접속 시 서버에 자체 패키지를 설치해야 하는데, 이때 tar 압축 해제가 필수입니다. 많은 EC2 AMI에서 tar가 기본 설치되지 않아 발생하는 클래식한 이슈였네요.

### 2️⃣ 인스턴스 스펙 + 인덱싱 오버헤드

더 심각한 문제는 여기서 시작됩니다:

- **인스턴스 스펙**: t3.micro (1 vCPU, 1GB RAM)
- **Cursor의 동작**: 홈 디렉토리 전체 인덱싱 수행
- **프로젝트 규모**: EKS 관련 소스코드 + 설정 파일들

Cursor는 접속과 동시에 파일 인덱싱을 시작하는데, 작은 인스턴스에서 대용량 프로젝트를 인덱싱하면 메모리와 CPU가 한계에 도달합니다.

## 📊 리소스 사용량 분석

```shell
# 인덱싱 중 리소스 모니터링
htop
iostat -x 1
free -h
```

실제로 모니터링해보니:

- **CPU 사용률**: 90%+ 지속
- **메모리 사용률**: Swap 영역까지 사용
- **I/O Wait**: 높은 디스크 읽기 작업

t3.micro로는 감당하기 어려운 워크로드였습니다.

## 🛠️ 해결 방안들

### 방법 1: 인스턴스 업그레이드

```shell
# t3.micro → t3.small 이상으로 업그레이드
# 2 vCPU, 2GB RAM 이상 권장
```

### 방법 2: 워크스페이스 분리

```shell
# 가벼운 작업용 디렉토리 생성
mkdir ~/workspace-light
cd ~/workspace-light
# Cursor에서 이 디렉토리만 열기
```

### 방법 3: 인덱싱 최적화

```json
// .vscode/settings.json
{
  "files.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/.git": true,
    "**/logs": true
  },
  "files.watcherExclude": {
    "**/node_modules/**": true
  }
}
```

### 방법 4: 툴 선택 재고려

## 🤔 현실적인 결론

모든 해결책을 검토한 결과, **기존 XShell 사용 유지**를 선택했습니다.

**이유:**

- ✅ 안정적인 접속 (리소스 오버헤드 없음)
- ✅ 빠른 응답성
- ✅ 배터리 친화적
- ✅ 검증된 워크플로우

**Cursor의 장점들:**

- 🎯 통합 개발 환경
- 🎯 Git 통합
- 🎯 확장성
- 🎯 모던 UI/UX

하지만 **베스천 서버 작업**의 특성상 파일 편집보다는 **시스템 관리**가 주목적이라 굳이 고사양이 필요한 IDE를 사용할 이유가 없었습니다.

## 💡 교훈과 팁

1. **인스턴스 스펙은 용도에 맞게**: 베스천 서버라면 접속만 되면 충분
2. **툴의 특성 이해**: IDE는 편리하지만 리소스 오버헤드가 있음
3. **상황별 적절한 툴 선택**: 개발용과 관리용을 구분하자
4. **비용 최적화**: t3.micro로도 충분한 작업에 더 큰 인스턴스는 낭비

## 🎯 최종 권장사항

| 용도 | 인스턴스 타입 | 권장 툴 |
|------|---------------|---------|
| 베스천/관리 서버 | t3.micro | 전용 SSH 클라이언트 |
| 개발 서버 | t3.small+ | Cursor/VS Code |
| 프로덕션 워크로드 | 요구사항에 따라 | 상황별 선택 |

결국 **적재적소**가 답이네요. 모던한 툴이 항상 옳은 건 아니라는 걸 다시 한번 깨달았습니다. 🚀

---

*혹시 비슷한 이슈를 겪고 계신다면, 인스턴스 스펙과 프로젝트 사이즈를 먼저 체크해보세요!*

## 관련 태그

- #SSH #EC2 #Troubleshooting
- #VSCode #Cursor #RemoteDevelopment
- #AWS #ResourceOptimization
- #DeveloperExperience