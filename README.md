# HoneyDanji 기술 블로그

Jekyll과 GitHub Pages를 이용한 개인 기술 블로그입니다.

## 🚀 기능

- **반응형 디자인**: 모바일, 태블릿, 데스크톱 모든 기기에서 최적화된 화면
- **다크 모드 지원**: 사용자 환경에 맞는 테마 자동 적용
- **빠른 로딩**: 최적화된 CSS와 JavaScript로 빠른 페이지 로딩
- **SEO 최적화**: 검색 엔진 최적화를 위한 메타 태그 및 구조화 데이터
- **소셜 미디어 연동**: 포스트 공유 기능 및 소셜 미디어 링크
- **카테고리 및 태그**: 체계적인 포스트 분류 시스템
- **댓글 시스템**: Disqus 연동을 통한 독자와의 소통
- **RSS 피드**: 구독자를 위한 RSS 피드 제공

## 🛠️ 기술 스택

- **Jekyll**: 정적 사이트 생성기
- **GitHub Pages**: 무료 호스팅 서비스
- **Liquid**: 템플릿 엔진
- **Sass**: CSS 전처리기
- **JavaScript**: 인터랙션 및 사용자 경험 개선

## 📁 프로젝트 구조

```
blog/
├── _layouts/           # 레이아웃 템플릿
│   ├── default.html   # 기본 레이아웃
│   ├── post.html      # 포스트 레이아웃
│   └── page.html      # 페이지 레이아웃
├── _includes/         # 재사용 가능한 컴포넌트
├── _posts/           # 블로그 포스트 (Markdown)
├── _sass/            # Sass 스타일시트
├── assets/           # 정적 자산
│   ├── css/          # CSS 파일
│   ├── js/           # JavaScript 파일
│   └── images/       # 이미지 파일
├── _config.yml       # Jekyll 설정 파일
├── Gemfile          # Ruby 의존성 관리
├── index.html       # 홈페이지
├── about.md         # 소개 페이지
├── posts.html       # 포스트 목록 페이지
├── categories.html  # 카테고리 페이지
└── tags.html        # 태그 페이지
```

## 🚀 로컬 개발 환경 설정

### 1. 저장소 클론
```bash
git clone https://github.com/honeydanji/blog.git
cd blog
```

### 2. Ruby 및 Jekyll 설치
```bash
# Ruby 설치 (macOS)
brew install ruby

# Ruby 설치 (Ubuntu)
sudo apt-get install ruby-full

# Bundler 설치
gem install bundler
```

### 3. 의존성 설치
```bash
bundle install
```

### 4. 로컬 서버 실행
```bash
bundle exec jekyll serve
```

브라우저에서 `http://localhost:4000`으로 접속하여 확인할 수 있습니다.

## ✍️ 포스트 작성하기

### 1. 새 포스트 파일 생성
`_posts` 디렉토리에 다음 형식으로 파일을 생성합니다:
```
YYYY-MM-DD-post-title.md
```

### 2. Front Matter 설정
포스트 상단에 다음과 같은 메타데이터를 추가합니다:

```yaml
---
layout: post
title: "포스트 제목"
date: 2024-06-27 14:00:00 +0900
categories: [카테고리1, 카테고리2]
tags: [태그1, 태그2, 태그3]
author: HoneyDanji
excerpt: "포스트 요약 내용"
---
```

### 3. 마크다운으로 내용 작성
Front Matter 아래에 마크다운 문법으로 포스트 내용을 작성합니다.

## 🎨 커스터마이징

### 색상 테마 변경
`assets/css/style.css` 파일의 CSS 변수를 수정하여 색상 테마를 변경할 수 있습니다:

```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #1e40af;
  --accent-color: #3b82f6;
  /* ... */
}
```

### 소셜 미디어 링크 설정
`_config.yml` 파일에서 소셜 미디어 정보를 설정합니다:

```yaml
github_username: your-github-username
twitter_username: your-twitter-username
linkedin_username: your-linkedin-username
```

### 네비게이션 메뉴 수정
`_config.yml` 파일의 `navigation` 섹션에서 메뉴를 수정할 수 있습니다:

```yaml
navigation:
  - title: Home
    url: /
  - title: About
    url: /about/
  - title: Posts
    url: /posts/
```

## 🚀 배포

이 블로그는 GitHub Actions를 통해 자동으로 GitHub Pages에 배포됩니다.

### 배포 과정
1. `main` 브랜치에 코드를 푸시
2. GitHub Actions가 자동으로 Jekyll 빌드 실행
3. 생성된 정적 파일을 GitHub Pages에 배포

### 수동 배포 (선택사항)
```bash
# 빌드
bundle exec jekyll build

# 배포 (GitHub Pages의 경우 자동화되어 있음)
```

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 🤝 기여하기

기여를 환영합니다! 다음과 같은 방법으로 기여할 수 있습니다:

1. 이슈 제기
2. 기능 개선 제안
3. 풀 리퀘스트 제출

### 개발 워크플로우
1. 저장소를 포크합니다
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)
5. 풀 리퀘스트를 생성합니다

## 📞 연락처

문의사항이나 피드백이 있으시면 언제든 연락주세요:

- **Email**: contact@honeydanji.dev
- **GitHub**: [@honeydanji](https://github.com/honeydanji)
- **Twitter**: [@honeydanji](https://twitter.com/honeydanji)

---

**Happy Blogging! 🎉**