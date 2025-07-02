#!/usr/bin/env python3
"""
Script to systematically collect all pages from Notion database
and organize them into a comprehensive dataset
"""

import json
from typing import List, Dict, Any

# All page data we've collected so far from the API calls
PAGES_DATA = [
    # From first batch
    {
        "id": "224393a5-a797-80ce-b03a-f99ec3525efa",
        "title": "FAIL……",
        "tags": [],
        "parent_relations": [],
        "child_relations": ["206393a5-a797-809a-9d43-f42fdacc2f97", "178393a5-a797-8040-9441-d6f7176f45c8", "1aa393a5-a797-8087-b47a-cc1d13bb0337"],
        "created_time": "2025-07-02T04:15:00.000Z",
        "last_edited_time": "2025-07-02T04:15:00.000Z",
        "url": "https://www.notion.so/FAIL-224393a5a79780ceb03af99ec3525efa"
    },
    {
        "id": "21f393a5-a797-800b-9600-e182d7442516",
        "title": "Resume",
        "tags": [],
        "parent_relations": [],
        "child_relations": [],
        "created_time": "2025-06-27T07:49:00.000Z",
        "last_edited_time": "2025-06-27T07:49:00.000Z",
        "url": "https://www.notion.so/Resume-21f393a5a797800b9600e182d7442516"
    },
    {
        "id": "21f393a5-a797-8061-a1ce-e97828e7c7d0",
        "title": "claud code로 한 것",
        "tags": [],
        "parent_relations": ["21f393a5-a797-809c-bb5b-f8da6d3531fb"],
        "child_relations": [],
        "created_time": "2025-06-27T06:02:00.000Z",
        "last_edited_time": "2025-06-27T06:03:00.000Z",
        "url": "https://www.notion.so/claud-code-21f393a5a7978061a1cee97828e7c7d0"
    },
    {
        "id": "21f393a5-a797-80bb-8f21-d2669e75f8df",
        "title": "Perplexity",
        "tags": [],
        "parent_relations": ["21f393a5-a797-8000-91a3-e971cf9a2564"],
        "child_relations": [],
        "created_time": "2025-06-27T05:43:00.000Z",
        "last_edited_time": "2025-06-27T05:43:00.000Z",
        "url": "https://www.notion.so/Perplexity-21f393a5a79780bb8f21d2669e75f8df"
    },
    {
        "id": "21f393a5-a797-80d9-a9ff-e8e36afa1022",
        "title": "1. 무자본 무경험인 사람이 AI로 한달에 10만원부터 벌기 프롬프트",
        "tags": [],
        "parent_relations": ["21f393a5-a797-802a-8890-f478f7c2896c"],
        "child_relations": [],
        "created_time": "2025-06-27T02:26:00.000Z",
        "last_edited_time": "2025-06-27T02:33:00.000Z",
        "url": "https://www.notion.so/1-AI-10-21f393a5a79780d9a9ffe8e36afa1022"
    },
    {
        "id": "21f393a5-a797-802a-8890-f478f7c2896c",
        "title": "Chat GPT",
        "tags": [],
        "parent_relations": ["21f393a5-a797-8000-91a3-e971cf9a2564"],
        "child_relations": ["21f393a5-a797-80d9-a9ff-e8e36afa1022"],
        "created_time": "2025-06-27T02:25:00.000Z",
        "last_edited_time": "2025-06-27T05:44:00.000Z",
        "url": "https://www.notion.so/Chat-GPT-21f393a5a797802a8890f478f7c2896c"
    },
    {
        "id": "21f393a5-a797-809c-bb5b-f8da6d3531fb",
        "title": "CLAUD",
        "tags": [],
        "parent_relations": ["21f393a5-a797-8000-91a3-e971cf9a2564"],
        "child_relations": ["21f393a5-a797-8061-a1ce-e97828e7c7d0"],
        "created_time": "2025-06-27T02:25:00.000Z",
        "last_edited_time": "2025-06-27T06:02:00.000Z",
        "url": "https://www.notion.so/CLAUD-21f393a5a797809cbb5bf8da6d3531fb"
    },
    {
        "id": "21f393a5-a797-8000-91a3-e971cf9a2564",
        "title": "AI",
        "tags": [],
        "parent_relations": [],
        "child_relations": ["21f393a5-a797-809c-bb5b-f8da6d3531fb", "21f393a5-a797-802a-8890-f478f7c2896c", "21f393a5-a797-80bb-8f21-d2669e75f8df"],
        "created_time": "2025-06-27T02:25:00.000Z",
        "last_edited_time": "2025-06-27T05:43:00.000Z",
        "url": "https://www.notion.so/AI-21f393a5a797800091a3e971cf9a2564"
    },
    {
        "id": "21e393a5-a797-80f5-82e7-f359ea8f316b",
        "title": "문제정의",
        "tags": [],
        "parent_relations": ["21e393a5-a797-8063-be1c-c458672c8fdf"],
        "child_relations": [],
        "created_time": "2025-06-26T09:00:00.000Z",
        "last_edited_time": "2025-06-26T09:00:00.000Z",
        "url": "https://www.notion.so/21e393a5a79780f582e7f359ea8f316b"
    },
    {
        "id": "21e393a5-a797-8063-be1c-c458672c8fdf",
        "title": "[DEV] EKS 클러스터 리소스 효율성 해결",
        "tags": [],
        "parent_relations": ["1de393a5-a797-8061-b68f-d78fbb2b353b"],
        "child_relations": ["21e393a5-a797-80f5-82e7-f359ea8f316b"],
        "created_time": "2025-06-26T08:35:00.000Z",
        "last_edited_time": "2025-06-26T09:00:00.000Z",
        "url": "https://www.notion.so/DEV-EKS-21e393a5a7978063be1cc458672c8fdf"
    }
]

def create_hierarchical_structure(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create a hierarchical structure showing parent-child relationships"""
    pages_by_id = {page['id']: page for page in pages}
    
    # Find root pages (no parents)
    root_pages = [page for page in pages if not page['parent_relations']]
    
    def build_tree(page_id: str, visited: set = None) -> Dict[str, Any]:
        if visited is None:
            visited = set()
        
        if page_id in visited:
            return {'id': page_id, 'title': '(circular reference)', 'children': []}
        
        visited.add(page_id)
        page = pages_by_id.get(page_id, {})
        
        children = []
        for child_id in page.get('child_relations', []):
            if child_id in pages_by_id:
                children.append(build_tree(child_id, visited.copy()))
        
        return {
            'id': page_id,
            'title': page.get('title', 'Unknown'),
            'tags': page.get('tags', []),
            'children': children
        }
    
    hierarchy = []
    for root_page in root_pages:
        hierarchy.append(build_tree(root_page['id']))
    
    return {'root_pages': hierarchy, 'total_pages': len(pages)}

def create_summary_text(pages: List[Dict[str, Any]], hierarchy: Dict[str, Any]) -> str:
    """Create a text summary of all pages and their relationships"""
    summary_lines = []
    summary_lines.append("=== NOTION 기술블로그 DATABASE SUMMARY ===")
    summary_lines.append(f"Total Pages: {len(pages)}")
    summary_lines.append(f"Root Pages: {len(hierarchy['root_pages'])}")
    summary_lines.append("")
    
    def format_tree(node: Dict[str, Any], level: int = 0) -> List[str]:
        indent = "  " * level
        lines = []
        title = node.get('title', 'Unknown')
        tags = node.get('tags', [])
        tag_str = f" [{', '.join(tags)}]" if tags else ""
        lines.append(f"{indent}- {title}{tag_str}")
        
        for child in node.get('children', []):
            lines.extend(format_tree(child, level + 1))
        
        return lines
    
    summary_lines.append("=== HIERARCHICAL STRUCTURE ===")
    for root in hierarchy['root_pages']:
        summary_lines.extend(format_tree(root))
    
    summary_lines.append("")
    summary_lines.append("=== ALL PAGES (CHRONOLOGICAL) ===")
    sorted_pages = sorted(pages, key=lambda p: p.get('created_time', ''), reverse=True)
    for page in sorted_pages:
        tags_str = f" [{', '.join(page.get('tags', []))}]" if page.get('tags') else ""
        parent_count = len(page.get('parent_relations', []))
        child_count = len(page.get('child_relations', []))
        rel_str = f" (P:{parent_count}, C:{child_count})" if parent_count > 0 or child_count > 0 else ""
        summary_lines.append(f"- {page['title']}{tags_str}{rel_str}")
    
    return "\n".join(summary_lines)

# Create the hierarchical structure
hierarchy = create_hierarchical_structure(PAGES_DATA)
summary_text = create_summary_text(PAGES_DATA, hierarchy)

# Prepare the comprehensive data structure
comprehensive_data = {
    "database_info": {
        "database_id": "be81096a-2515-4eb1-bcc0-bba5bfdb3d59",
        "name": "기술블로그",
        "total_pages": len(PAGES_DATA),
        "collection_date": "2025-07-02",
        "status": "partial_collection"
    },
    "hierarchy": hierarchy,
    "all_pages": PAGES_DATA,
    "summary": summary_text
}

print(f"Collected {len(PAGES_DATA)} pages")
print(f"Found {len(hierarchy['root_pages'])} root pages")
print("\nHierarchy preview:")
print(summary_text[:1000] + "..." if len(summary_text) > 1000 else summary_text)