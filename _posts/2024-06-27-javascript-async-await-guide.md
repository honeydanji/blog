---
layout: post
title: "JavaScript Async/Await 완벽 가이드"
date: 2024-06-27 15:30:00 +0900
categories: [JavaScript, 프론트엔드]
tags: [javascript, async, await, promise, 비동기, 프론트엔드]
author: HoneyDanji
excerpt: "JavaScript의 Async/Await 문법을 완벽하게 이해하고 실무에서 효과적으로 활용하는 방법을 알아보겠습니다."
---

# JavaScript Async/Await 완벽 가이드

비동기 프로그래밍은 현대 JavaScript 개발에서 필수적인 개념입니다. 이번 포스트에서는 **Async/Await** 문법을 깊이 있게 다뤄보겠습니다.

## 목차

1. [Async/Await란?](#asyncawait란)
2. [Promise와의 차이점](#promise와의-차이점)
3. [기본 사용법](#기본-사용법)
4. [에러 처리](#에러-처리)
5. [실전 예제](#실전-예제)
6. [성능 최적화](#성능-최적화)
7. [주의사항](#주의사항)

## Async/Await란?

**Async/Await**는 ES2017(ES8)에서 도입된 문법으로, 비동기 코드를 동기 코드처럼 작성할 수 있게 해주는 syntactic sugar입니다.

### 장점

- **가독성 향상**: 코드가 동기적으로 보여 이해하기 쉬움
- **디버깅 용이**: 스택 트레이스가 명확함
- **에러 처리 간소화**: try-catch 블록 사용 가능

## Promise와의 차이점

### Promise 방식
```javascript
function fetchUserData(userId) {
  return fetch(`/api/users/${userId}`)
    .then(response => response.json())
    .then(user => {
      return fetch(`/api/posts/${user.id}`);
    })
    .then(response => response.json())
    .then(posts => {
      console.log('사용자 포스트:', posts);
      return posts;
    })
    .catch(error => {
      console.error('에러 발생:', error);
      throw error;
    });
}
```

### Async/Await 방식
```javascript
async function fetchUserData(userId) {
  try {
    const userResponse = await fetch(`/api/users/${userId}`);
    const user = await userResponse.json();
    
    const postsResponse = await fetch(`/api/posts/${user.id}`);
    const posts = await postsResponse.json();
    
    console.log('사용자 포스트:', posts);
    return posts;
  } catch (error) {
    console.error('에러 발생:', error);
    throw error;
  }
}
```

## 기본 사용법

### 1. 함수 선언
```javascript
// 함수 선언식
async function myAsyncFunction() {
  // 비동기 작업
}

// 함수 표현식
const myAsyncFunction = async function() {
  // 비동기 작업
};

// 화살표 함수
const myAsyncFunction = async () => {
  // 비동기 작업
};
```

### 2. Await 키워드
```javascript
async function example() {
  // Promise를 반환하는 함수 대기
  const result = await someAsyncOperation();
  
  // 결과 사용
  console.log(result);
}
```

### 3. 반환값
```javascript
async function getData() {
  return "Hello World"; // Promise.resolve("Hello World")와 동일
}

getData().then(result => {
  console.log(result); // "Hello World"
});
```

## 에러 처리

### Try-Catch 블록
```javascript
async function handleErrors() {
  try {
    const response = await fetch('/api/data');
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('데이터 조회 실패:', error.message);
    
    // 에러 타입별 처리
    if (error instanceof TypeError) {
      console.error('네트워크 오류');
    } else if (error instanceof SyntaxError) {
      console.error('JSON 파싱 오류');
    }
    
    throw error; // 상위로 에러 전파
  }
}
```

### 여러 Promise 에러 처리
```javascript
async function multipleOperations() {
  try {
    const [user, posts, comments] = await Promise.all([
      fetchUser(),
      fetchPosts(),
      fetchComments()
    ]);
    
    return { user, posts, comments };
  } catch (error) {
    // 하나라도 실패하면 여기서 처리
    console.error('작업 중 하나가 실패:', error);
    throw error;
  }
}
```

## 실전 예제

### 1. API 호출과 데이터 변환
```javascript
class UserService {
  constructor(baseURL) {
    this.baseURL = baseURL;
  }
  
  async fetchUserProfile(userId) {
    try {
      // 사용자 기본 정보 조회
      const userResponse = await fetch(`${this.baseURL}/users/${userId}`);
      const user = await userResponse.json();
      
      // 사용자 통계 정보 조회
      const statsResponse = await fetch(`${this.baseURL}/users/${userId}/stats`);
      const stats = await statsResponse.json();
      
      // 데이터 병합 및 변환
      return {
        id: user.id,
        name: user.name,
        email: user.email,
        joinDate: new Date(user.createdAt),
        postCount: stats.posts,
        followerCount: stats.followers
      };
    } catch (error) {
      console.error('사용자 프로필 조회 실패:', error);
      return null;
    }
  }
}
```

### 2. 순차적 vs 병렬 처리
```javascript
// ❌ 순차적 처리 (느림)
async function sequentialProcessing() {
  const user = await fetchUser();        // 1초 소요
  const posts = await fetchPosts();      // 1초 소요
  const comments = await fetchComments(); // 1초 소요
  
  return { user, posts, comments }; // 총 3초 소요
}

// ✅ 병렬 처리 (빠름)
async function parallelProcessing() {
  const [user, posts, comments] = await Promise.all([
    fetchUser(),        // 이 셋이 동시에 실행
    fetchPosts(),       // 이 셋이 동시에 실행
    fetchComments()     // 이 셋이 동시에 실행
  ]);
  
  return { user, posts, comments }; // 총 1초 소요
}
```

### 3. 조건부 비동기 처리
```javascript
async function conditionalAsync(userType) {
  let userData;
  
  if (userType === 'premium') {
    userData = await fetchPremiumUserData();
  } else if (userType === 'standard') {
    userData = await fetchStandardUserData();
  } else {
    userData = await fetchBasicUserData();
  }
  
  // 공통 후처리
  const processedData = await processUserData(userData);
  return processedData;
}
```

## 성능 최적화

### 1. Promise.all 활용
```javascript
// 🚀 성능 최적화된 데이터 로딩
async function loadDashboardData() {
  const startTime = performance.now();
  
  try {
    // 독립적인 데이터들을 병렬로 처리
    const [
      userData,
      analyticsData,
      notificationsData,
      settingsData
    ] = await Promise.all([
      fetchUserData(),
      fetchAnalytics(),
      fetchNotifications(),
      fetchSettings()
    ]);
    
    const endTime = performance.now();
    console.log(`데이터 로딩 완료: ${endTime - startTime}ms`);
    
    return {
      user: userData,
      analytics: analyticsData,
      notifications: notificationsData,
      settings: settingsData
    };
  } catch (error) {
    console.error('대시보드 데이터 로딩 실패:', error);
    throw error;
  }
}
```

### 2. 타임아웃 처리
```javascript
function withTimeout(promise, timeoutMs) {
  return Promise.race([
    promise,
    new Promise((_, reject) => 
      setTimeout(() => reject(new Error('Timeout')), timeoutMs)
    )
  ]);
}

async function fetchWithTimeout() {
  try {
    const data = await withTimeout(
      fetch('/api/slow-endpoint'),
      5000 // 5초 타임아웃
    );
    return await data.json();
  } catch (error) {
    if (error.message === 'Timeout') {
      console.error('요청 시간 초과');
    }
    throw error;
  }
}
```

### 3. 재시도 로직
```javascript
async function fetchWithRetry(url, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url);
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      
      return await response.json();
    } catch (error) {
      console.log(`시도 ${attempt}/${maxRetries} 실패:`, error.message);
      
      if (attempt === maxRetries) {
        throw new Error(`${maxRetries}번 재시도 후 실패: ${error.message}`);
      }
      
      // 지수 백오프 (exponential backoff)
      const delay = Math.pow(2, attempt) * 1000;
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}
```

## 주의사항

### 1. 병렬 처리 실수
```javascript
// ❌ 잘못된 방법 - 순차 처리됨
async function wrongWay() {
  const result1 = await asyncOperation1();
  const result2 = await asyncOperation2(); // operation1 완료 후 시작
  return [result1, result2];
}

// ✅ 올바른 방법 - 병렬 처리
async function rightWay() {
  const promise1 = asyncOperation1();
  const promise2 = asyncOperation2(); // 즉시 시작
  
  const [result1, result2] = await Promise.all([promise1, promise2]);
  return [result1, result2];
}
```

### 2. 에러 처리 누락
```javascript
// ❌ 에러 처리 없음
async function withoutErrorHandling() {
  const data = await fetchData(); // 에러 발생 시 크래시
  return data;
}

// ✅ 적절한 에러 처리
async function withErrorHandling() {
  try {
    const data = await fetchData();
    return data;
  } catch (error) {
    console.error('데이터 조회 실패:', error);
    return null; // 기본값 반환
  }
}
```

### 3. 메모리 누수 방지
```javascript
// 큰 데이터 처리 시 주의
async function processLargeData() {
  try {
    const largeData = await fetchLargeDataset();
    const processedData = await processData(largeData);
    
    // 명시적으로 메모리 해제
    largeData.length = 0; // 배열 비우기
    
    return processedData;
  } catch (error) {
    console.error('대용량 데이터 처리 실패:', error);
    throw error;
  }
}
```

## 마무리

Async/Await는 JavaScript 비동기 프로그래밍의 게임 체인저입니다. 올바르게 사용하면:

- 📖 **가독성이 크게 향상**됩니다
- 🛠️ **디버깅이 훨씬 쉬워**집니다  
- ⚡ **성능 최적화**가 가능합니다
- 🔒 **에러 처리**가 간단해집니다

다음 포스트에서는 **JavaScript 모듈 시스템**에 대해 알아보겠습니다. 궁금한 점이 있으시면 댓글로 남겨주세요!

---

*이 포스트가 도움이 되셨나요? 공유해주시면 더 많은 개발자들에게 도움이 될 수 있습니다! 🙌*