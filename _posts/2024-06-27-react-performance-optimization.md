---
layout: post
title: "React 성능 최적화: 실전 가이드와 베스트 프랙티스"
date: 2024-06-27 16:45:00 +0900
categories: [React, 성능최적화]
tags: [react, performance, optimization, memo, usecallback, usememo, 최적화]
author: HoneyDanji
excerpt: "React 애플리케이션의 성능을 극대화하는 실전 기법들을 알아보겠습니다. 메모이제이션부터 코드 스플리팅까지 모든 것을 다룹니다."
---

# React 성능 최적화: 실전 가이드와 베스트 프랙티스

React 애플리케이션이 커질수록 성능 이슈는 피할 수 없는 문제가 됩니다. 이번 포스트에서는 **실전에서 바로 적용할 수 있는 React 성능 최적화 기법**들을 상세히 알아보겠습니다.

## 📋 목차

1. [성능 측정하기](#성능-측정하기)
2. [React.memo와 컴포넌트 메모이제이션](#reactmemo와-컴포넌트-메모이제이션)
3. [useMemo와 useCallback 활용](#usememo와-usecallback-활용)
4. [상태 관리 최적화](#상태-관리-최적화)
5. [렌더링 최적화](#렌더링-최적화)
6. [번들 크기 최적화](#번들-크기-최적화)
7. [실전 사례 분석](#실전-사례-분석)

## 성능 측정하기

최적화를 시작하기 전에 현재 성능을 정확히 측정하는 것이 중요합니다.

### React DevTools Profiler 활용

```jsx
// 성능 측정을 위한 컴포넌트 래핑
import { Profiler } from 'react';

function App() {
  const onRenderCallback = (id, phase, actualDuration, baseDuration, startTime, commitTime) => {
    console.log('성능 정보:', {
      id,           // 프로파일링된 컴포넌트 ID
      phase,        // "mount" (처음 렌더링) 또는 "update" (재렌더링)
      actualDuration, // 실제 렌더링 시간
      baseDuration,   // 메모이제이션 없이 예상되는 시간
      startTime,      // 렌더링 시작 시간
      commitTime      // React가 변경사항을 커밋한 시간
    });
  };

  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <Header />
      <MainContent />
      <Footer />
    </Profiler>
  );
}
```

### 커스텀 성능 훅

```jsx
// 컴포넌트 렌더링 시간 측정 훅
import { useEffect, useRef } from 'react';

function useRenderTimer(componentName) {
  const renderStartTime = useRef();
  
  // 렌더링 시작 시간 기록
  renderStartTime.current = performance.now();
  
  useEffect(() => {
    // 렌더링 완료 시간 계산
    const renderEndTime = performance.now();
    const renderTime = renderEndTime - renderStartTime.current;
    
    console.log(`${componentName} 렌더링 시간: ${renderTime.toFixed(2)}ms`);
  });
}

// 사용 예제
function ExpensiveComponent() {
  useRenderTimer('ExpensiveComponent');
  
  return <div>무거운 컴포넌트</div>;
}
```

## React.memo와 컴포넌트 메모이제이션

### 기본 사용법

```jsx
// ❌ 최적화 이전
function UserCard({ user, onEdit }) {
  console.log('UserCard 렌더링'); // 부모가 렌더링될 때마다 호출됨
  
  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      <button onClick={() => onEdit(user.id)}>편집</button>
    </div>
  );
}

// ✅ 최적화 이후
const UserCard = React.memo(function UserCard({ user, onEdit }) {
  console.log('UserCard 렌더링'); // props가 변경될 때만 호출됨
  
  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      <button onClick={() => onEdit(user.id)}>편집</button>
    </div>
  );
});
```

### 커스텀 비교 함수

```jsx
// 복잡한 객체 비교를 위한 커스텀 함수
const UserCard = React.memo(function UserCard({ user, settings }) {
  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      {settings.showAge && <p>나이: {user.age}</p>}
    </div>
  );
}, (prevProps, nextProps) => {
  // 사용자 정보와 관련 설정만 비교
  return (
    prevProps.user.id === nextProps.user.id &&
    prevProps.user.name === nextProps.user.name &&
    prevProps.user.email === nextProps.user.email &&
    prevProps.user.age === nextProps.user.age &&
    prevProps.settings.showAge === nextProps.settings.showAge
  );
});
```

## useMemo와 useCallback 활용

### useMemo: 값 메모이제이션

```jsx
import { useMemo, useState } from 'react';

function ProductList({ products, filters }) {
  const [sortBy, setSortBy] = useState('name');
  
  // ✅ 비용이 큰 계산 결과를 메모이제이션
  const filteredAndSortedProducts = useMemo(() => {
    console.log('필터링 및 정렬 수행'); // dependencies 변경 시에만 실행
    
    return products
      .filter(product => {
        return filters.category ? product.category === filters.category : true;
      })
      .filter(product => {
        return filters.priceRange ? 
          product.price >= filters.priceRange.min && 
          product.price <= filters.priceRange.max : true;
      })
      .sort((a, b) => {
        switch (sortBy) {
          case 'name':
            return a.name.localeCompare(b.name);
          case 'price':
            return a.price - b.price;
          case 'rating':
            return b.rating - a.rating;
          default:
            return 0;
        }
      });
  }, [products, filters, sortBy]); // 의존성 배열
  
  // ✅ 통계 계산도 메모이제이션
  const statistics = useMemo(() => {
    const totalProducts = filteredAndSortedProducts.length;
    const averagePrice = filteredAndSortedProducts.reduce((sum, product) => 
      sum + product.price, 0) / totalProducts;
    const averageRating = filteredAndSortedProducts.reduce((sum, product) => 
      sum + product.rating, 0) / totalProducts;
    
    return {
      totalProducts,
      averagePrice: averagePrice.toFixed(2),
      averageRating: averageRating.toFixed(1)
    };
  }, [filteredAndSortedProducts]);
  
  return (
    <div>
      <div className="statistics">
        <span>총 {statistics.totalProducts}개 상품</span>
        <span>평균 가격: {statistics.averagePrice}원</span>
        <span>평균 평점: {statistics.averageRating}점</span>
      </div>
      
      <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
        <option value="name">이름순</option>
        <option value="price">가격순</option>
        <option value="rating">평점순</option>
      </select>
      
      {filteredAndSortedProducts.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}
```

### useCallback: 함수 메모이제이션

```jsx
import { useCallback, useState } from 'react';

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [filter, setFilter] = useState('all');
  
  // ✅ 함수를 메모이제이션하여 자식 컴포넌트 불필요한 리렌더링 방지
  const handleAddTodo = useCallback((text) => {
    setTodos(prevTodos => [
      ...prevTodos,
      {
        id: Date.now(),
        text,
        completed: false,
        createdAt: new Date()
      }
    ]);
  }, []); // 의존성이 없으므로 한 번만 생성
  
  const handleToggleTodo = useCallback((id) => {
    setTodos(prevTodos =>
      prevTodos.map(todo =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  }, []); // setTodos는 안정적이므로 의존성에 포함하지 않음
  
  const handleDeleteTodo = useCallback((id) => {
    setTodos(prevTodos => prevTodos.filter(todo => todo.id !== id));
  }, []);
  
  // ✅ filter 상태에 따른 조건부 함수 메모이제이션
  const handleBulkAction = useCallback((action) => {
    switch (action) {
      case 'complete-all':
        setTodos(prevTodos => 
          prevTodos.map(todo => ({ ...todo, completed: true }))
        );
        break;
      case 'delete-completed':
        setTodos(prevTodos => 
          prevTodos.filter(todo => !todo.completed)
        );
        break;
      default:
        break;
    }
  }, []); // 액션에 따라 동적으로 처리하므로 의존성 없음
  
  // 필터링된 할 일 목록
  const filteredTodos = useMemo(() => {
    switch (filter) {
      case 'active':
        return todos.filter(todo => !todo.completed);
      case 'completed':
        return todos.filter(todo => todo.completed);
      default:
        return todos;
    }
  }, [todos, filter]);
  
  return (
    <div className="todo-app">
      <TodoInput onAddTodo={handleAddTodo} />
      <TodoFilter currentFilter={filter} onFilterChange={setFilter} />
      <TodoList 
        todos={filteredTodos}
        onToggleTodo={handleToggleTodo}
        onDeleteTodo={handleDeleteTodo}
      />
      <TodoActions onBulkAction={handleBulkAction} />
    </div>
  );
}
```

## 상태 관리 최적화

### 상태 분할과 지역화

```jsx
// ❌ 모든 상태를 최상위에서 관리 (불필요한 리렌더링 발생)
function App() {
  const [user, setUser] = useState(null);
  const [posts, setPosts] = useState([]);
  const [comments, setComments] = useState([]);
  const [uiState, setUiState] = useState({
    isModalOpen: false,
    selectedTab: 'posts',
    isLoading: false
  });
  
  return (
    <div>
      <Header user={user} />
      <PostList posts={posts} comments={comments} />
      <Modal isOpen={uiState.isModalOpen} />
    </div>
  );
}

// ✅ 상태를 사용하는 컴포넌트에서 지역적으로 관리
function App() {
  const [user, setUser] = useState(null);
  
  return (
    <div>
      <Header user={user} />
      <PostSection /> {/* posts 상태는 여기서 관리 */}
      <ModalSection /> {/* modal 상태는 여기서 관리 */}
    </div>
  );
}

function PostSection() {
  const [posts, setPosts] = useState([]);
  const [comments, setComments] = useState([]);
  
  return <PostList posts={posts} comments={comments} />;
}
```

### Context API 최적화

```jsx
// ✅ Context를 용도별로 분리
const UserContext = createContext();
const ThemeContext = createContext();
const PostsContext = createContext();

// Context Provider 최적화
function UserProvider({ children }) {
  const [user, setUser] = useState(null);
  
  // ✅ Context 값을 메모이제이션
  const contextValue = useMemo(() => ({
    user,
    setUser,
    login: (userData) => setUser(userData),
    logout: () => setUser(null)
  }), [user]);
  
  return (
    <UserContext.Provider value={contextValue}>
      {children}
    </UserContext.Provider>
  );
}

// ✅ Context 사용 시 필요한 값만 구독
function useUser() {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within UserProvider');
  }
  return context;
}

// 선택적 구독을 위한 커스텀 훅
function useUserName() {
  const { user } = useUser();
  return user?.name;
}
```

## 렌더링 최적화

### 가상화(Virtualization)

```jsx
import { FixedSizeList as List } from 'react-window';

// ✅ 대용량 리스트를 위한 가상화
function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      <ListItem item={items[index]} />
    </div>
  );
  
  return (
    <List
      height={600}        // 컨테이너 높이
      itemCount={items.length}
      itemSize={100}      // 각 아이템 높이
      width="100%"
    >
      {Row}
    </List>
  );
}

// 동적 높이를 위한 가변 가상화
import { VariableSizeList as List } from 'react-window';

function DynamicVirtualizedList({ items }) {
  const getItemSize = (index) => {
    // 아이템별로 다른 높이 반환
    return items[index].isExpanded ? 200 : 100;
  };
  
  const Row = ({ index, style }) => (
    <div style={style}>
      <ExpandableListItem item={items[index]} />
    </div>
  );
  
  return (
    <List
      height={600}
      itemCount={items.length}
      itemSize={getItemSize}
      width="100%"
    >
      {Row}
    </List>
  );
}
```

### 이미지 최적화

```jsx
import { useState, useRef, useEffect } from 'react';

// ✅ 지연 로딩 이미지 컴포넌트
function LazyImage({ src, alt, className, placeholder }) {
  const [isLoaded, setIsLoaded] = useState(false);
  const [isInView, setIsInView] = useState(false);
  const imgRef = useRef();
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true);
          observer.disconnect();
        }
      },
      { threshold: 0.1 }
    );
    
    if (imgRef.current) {
      observer.observe(imgRef.current);
    }
    
    return () => observer.disconnect();
  }, []);
  
  return (
    <div ref={imgRef} className={className}>
      {isInView && (
        <img
          src={src}
          alt={alt}
          onLoad={() => setIsLoaded(true)}
          style={{
            opacity: isLoaded ? 1 : 0,
            transition: 'opacity 0.3s ease'
          }}
        />
      )}
      {!isLoaded && isInView && (
        <div className="image-placeholder">
          {placeholder || '로딩 중...'}
        </div>
      )}
    </div>
  );
}

// ✅ WebP 포맷 지원 이미지
function OptimizedImage({ src, alt, className }) {
  const webpSrc = src.replace(/\.(jpg|jpeg|png)$/, '.webp');
  
  return (
    <picture>
      <source srcSet={webpSrc} type="image/webp" />
      <img src={src} alt={alt} className={className} />
    </picture>
  );
}
```

## 번들 크기 최적화

### 코드 스플리팅

```jsx
import { lazy, Suspense } from 'react';

// ✅ 라우트 기반 코드 스플리팅
const HomePage = lazy(() => import('./pages/HomePage'));
const AboutPage = lazy(() => import('./pages/AboutPage'));
const ProfilePage = lazy(() => import('./pages/ProfilePage'));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>페이지 로딩 중...</div>}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

// ✅ 컴포넌트 기반 코드 스플리팅
function AdminPanel() {
  const [showAdvanced, setShowAdvanced] = useState(false);
  
  const AdvancedSettings = lazy(() => import('./AdvancedSettings'));
  
  return (
    <div>
      <h2>관리자 패널</h2>
      <button onClick={() => setShowAdvanced(!showAdvanced)}>
        고급 설정 {showAdvanced ? '숨기기' : '보기'}
      </button>
      
      {showAdvanced && (
        <Suspense fallback={<div>고급 설정 로딩 중...</div>}>
          <AdvancedSettings />
        </Suspense>
      )}
    </div>
  );
}
```

### 라이브러리 최적화

```jsx
// ❌ 전체 라이브러리 import
import _ from 'lodash';
import * as dateFns from 'date-fns';

// ✅ 필요한 함수만 import
import debounce from 'lodash/debounce';
import format from 'date-fns/format';
import isAfter from 'date-fns/isAfter';

// ✅ Tree-shaking을 위한 ES 모듈 사용
import { debounce } from 'lodash-es';
import { format, isAfter } from 'date-fns';
```

## 실전 사례 분석

### 대용량 테이블 최적화

```jsx
import { useMemo, useState, useCallback } from 'react';
import { FixedSizeGrid as Grid } from 'react-window';

function DataTable({ data, columns }) {
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [filterText, setFilterText] = useState('');
  
  // ✅ 필터링과 정렬을 메모이제이션
  const processedData = useMemo(() => {
    let filteredData = data;
    
    // 필터링
    if (filterText) {
      filteredData = data.filter(row =>
        Object.values(row).some(value =>
          String(value).toLowerCase().includes(filterText.toLowerCase())
        )
      );
    }
    
    // 정렬
    if (sortConfig.key) {
      filteredData.sort((a, b) => {
        const aValue = a[sortConfig.key];
        const bValue = b[sortConfig.key];
        
        if (aValue < bValue) return sortConfig.direction === 'asc' ? -1 : 1;
        if (aValue > bValue) return sortConfig.direction === 'asc' ? 1 : -1;
        return 0;
      });
    }
    
    return filteredData;
  }, [data, filterText, sortConfig]);
  
  const handleSort = useCallback((columnKey) => {
    setSortConfig(prevConfig => ({
      key: columnKey,
      direction: prevConfig.key === columnKey && prevConfig.direction === 'asc' 
        ? 'desc' : 'asc'
    }));
  }, []);
  
  // ✅ 가상화된 셀 컴포넌트
  const Cell = ({ columnIndex, rowIndex, style }) => {
    const row = processedData[rowIndex];
    const column = columns[columnIndex];
    const value = row[column.key];
    
    return (
      <div style={style} className="table-cell">
        {column.render ? column.render(value, row) : value}
      </div>
    );
  };
  
  return (
    <div className="data-table">
      <div className="table-controls">
        <input
          type="text"
          placeholder="검색..."
          value={filterText}
          onChange={(e) => setFilterText(e.target.value)}
        />
      </div>
      
      <div className="table-header">
        {columns.map(column => (
          <button
            key={column.key}
            onClick={() => handleSort(column.key)}
            className="table-header-cell"
          >
            {column.title}
            {sortConfig.key === column.key && (
              <span>{sortConfig.direction === 'asc' ? ' ↑' : ' ↓'}</span>
            )}
          </button>
        ))}
      </div>
      
      <Grid
        className="table-body"
        columnCount={columns.length}
        columnWidth={150}
        height={400}
        rowCount={processedData.length}
        rowHeight={50}
        width={columns.length * 150}
      >
        {Cell}
      </Grid>
    </div>
  );
}
```

## 성능 최적화 체크리스트

### 🔍 **측정 및 분석**
- [ ] React DevTools Profiler로 성능 병목 지점 파악
- [ ] 브라우저 성능 도구로 렌더링 시간 측정
- [ ] 번들 분석기로 코드 크기 확인

### ⚡ **렌더링 최적화**
- [ ] React.memo로 불필요한 리렌더링 방지
- [ ] useMemo로 비용이 큰 계산 메모이제이션
- [ ] useCallback으로 함수 참조 안정화
- [ ] 상태를 사용하는 컴포넌트에서 지역적으로 관리

### 📦 **번들 최적화**
- [ ] 코드 스플리팅으로 초기 로딩 시간 단축
- [ ] Tree-shaking으로 사용하지 않는 코드 제거
- [ ] 라이브러리 선택적 import 적용

### 🖼️ **리소스 최적화**
- [ ] 이미지 지연 로딩 구현
- [ ] WebP 포맷 등 최적화된 이미지 포맷 사용
- [ ] 대용량 리스트에 가상화 적용

## 마무리

React 성능 최적화는 **측정 → 분석 → 최적화 → 검증**의 반복 과정입니다. 

⚠️ **주의사항**: 
- 모든 곳에 최적화를 적용하지 마세요 (과도한 최적화는 오히려 성능 저하 가능)
- 실제 성능 문제가 있는 곳부터 최적화하세요
- 최적화 후 반드시 성능 개선을 측정하세요

다음 포스트에서는 **Next.js SSR 최적화 기법**에 대해 알아보겠습니다!

---

*이 포스트가 도움이 되셨나요? React 성능 최적화 관련 질문이 있으시면 댓글로 남겨주세요! 🚀*