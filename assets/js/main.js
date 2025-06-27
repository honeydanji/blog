// HoneyDanji Tech Blog - Main JavaScript

(function() {
  'use strict';

  // DOM ready
  document.addEventListener('DOMContentLoaded', function() {
    initializeTheme();
    initializeSmoothScroll();
    initializeCodeHighlight();
    initializeImageLazyLoading();
    initializeSearchFunctionality();
    initializeProgressBar();
    initializeTocGeneration();
  });

  // Theme management
  function initializeTheme() {
    const themeToggle = document.getElementById('theme-toggle');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Check for saved theme preference or default to system preference
    const savedTheme = localStorage.getItem('theme');
    const systemTheme = prefersDark.matches ? 'dark' : 'light';
    const currentTheme = savedTheme || systemTheme;
    
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    if (themeToggle) {
      themeToggle.addEventListener('click', toggleTheme);
    }
    
    // Listen for system theme changes
    prefersDark.addEventListener('change', function(e) {
      if (!localStorage.getItem('theme')) {
        document.documentElement.setAttribute('data-theme', e.matches ? 'dark' : 'light');
      }
    });
  }

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  }

  // Smooth scrolling for anchor links
  function initializeSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
      link.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        const target = document.querySelector(href);
        
        if (target) {
          e.preventDefault();
          const headerOffset = 80;
          const elementPosition = target.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
          
          window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  // Enhanced code highlighting and copy functionality
  function initializeCodeHighlight() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(block => {
      // Add copy button to code blocks
      const copyButton = document.createElement('button');
      copyButton.className = 'copy-code-btn';
      copyButton.innerHTML = '📋';
      copyButton.title = '코드 복사';
      
      const pre = block.parentNode;
      pre.style.position = 'relative';
      pre.appendChild(copyButton);
      
      copyButton.addEventListener('click', function() {
        const code = block.textContent;
        
        if (navigator.clipboard) {
          navigator.clipboard.writeText(code).then(() => {
            showCopyFeedback(copyButton);
          });
        } else {
          // Fallback for older browsers
          const textArea = document.createElement('textarea');
          textArea.value = code;
          document.body.appendChild(textArea);
          textArea.select();
          document.execCommand('copy');
          document.body.removeChild(textArea);
          showCopyFeedback(copyButton);
        }
      });
    });
  }

  function showCopyFeedback(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '✅';
    button.classList.add('copied');
    
    setTimeout(() => {
      button.innerHTML = originalText;
      button.classList.remove('copied');
    }, 2000);
  }

  // Image lazy loading
  function initializeImageLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
      const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.remove('lazy');
            imageObserver.unobserve(img);
          }
        });
      });
      
      images.forEach(img => imageObserver.observe(img));
    } else {
      // Fallback for browsers without IntersectionObserver
      images.forEach(img => {
        img.src = img.dataset.src;
        img.classList.remove('lazy');
      });
    }
  }

  // Search functionality (simple client-side search)
  function initializeSearchFunctionality() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (searchInput && searchResults) {
      let searchData = [];
      
      // Load search data (you would typically fetch this from a JSON file)
      fetchSearchData().then(data => {
        searchData = data;
      });
      
      let searchTimeout;
      searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value.trim();
        
        if (query.length > 2) {
          searchTimeout = setTimeout(() => {
            performSearch(query, searchData, searchResults);
          }, 300);
        } else {
          searchResults.innerHTML = '';
          searchResults.style.display = 'none';
        }
      });
      
      // Hide search results when clicking outside
      document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
          searchResults.style.display = 'none';
        }
      });
    }
  }

  async function fetchSearchData() {
    try {
      const response = await fetch('/search.json');
      return await response.json();
    } catch (error) {
      console.log('Search data not available');
      return [];
    }
  }

  function performSearch(query, data, resultsContainer) {
    const results = data.filter(item => 
      item.title.toLowerCase().includes(query.toLowerCase()) ||
      item.content.toLowerCase().includes(query.toLowerCase()) ||
      item.tags.some(tag => tag.toLowerCase().includes(query.toLowerCase()))
    ).slice(0, 5);
    
    if (results.length > 0) {
      resultsContainer.innerHTML = results.map(result => `
        <div class="search-result">
          <h4><a href="${result.url}">${highlightSearchTerm(result.title, query)}</a></h4>
          <p>${highlightSearchTerm(result.excerpt, query)}</p>
        </div>
      `).join('');
      
      resultsContainer.style.display = 'block';
    } else {
      resultsContainer.innerHTML = '<div class="search-result">검색 결과가 없습니다.</div>';
      resultsContainer.style.display = 'block';
    }
  }

  function highlightSearchTerm(text, term) {
    const regex = new RegExp(`(${term})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
  }

  // Reading progress bar
  function initializeProgressBar() {
    const progressBar = document.getElementById('reading-progress');
    
    if (progressBar) {
      window.addEventListener('scroll', updateProgressBar);
    }
  }

  function updateProgressBar() {
    const progressBar = document.getElementById('reading-progress');
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    
    progressBar.style.width = scrolled + '%';
  }

  // Table of contents generation
  function initializeTocGeneration() {
    const content = document.querySelector('.post-content');
    const tocContainer = document.getElementById('table-of-contents');
    
    if (content && tocContainer) {
      const headings = content.querySelectorAll('h1, h2, h3, h4, h5, h6');
      
      if (headings.length > 0) {
        const toc = generateTableOfContents(headings);
        tocContainer.innerHTML = toc;
        tocContainer.style.display = 'block';
      }
    }
  }

  function generateTableOfContents(headings) {
    let toc = '<ul class="toc-list">';
    
    headings.forEach((heading, index) => {
      const level = parseInt(heading.tagName.substring(1));
      const text = heading.textContent;
      const id = `heading-${index}`;
      
      heading.id = id;
      
      toc += `<li class="toc-item toc-level-${level}">
        <a href="#${id}">${text}</a>
      </li>`;
    });
    
    toc += '</ul>';
    return toc;
  }

  // Utility functions
  function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }

  function throttle(func, limit) {
    let inThrottle;
    return function() {
      const args = arguments;
      const context = this;
      if (!inThrottle) {
        func.apply(context, args);
        inThrottle = true;
        setTimeout(() => inThrottle = false, limit);
      }
    };
  }

  // Performance monitoring
  function trackPerformance() {
    if ('performance' in window) {
      window.addEventListener('load', function() {
        setTimeout(function() {
          const perfData = performance.getEntriesByType('navigation')[0];
          console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart);
        }, 0);
      });
    }
  }

  // Initialize performance tracking
  trackPerformance();

  // Expose utilities to global scope if needed
  window.BlogUtils = {
    debounce,
    throttle,
    toggleTheme
  };

})();