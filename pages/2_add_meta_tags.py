import os
import shutil
import streamlit
from bs4 import BeautifulSoup
import streamlit as st


# Streamlit index.html 경로 동적 탐색
streamlit_static_dir = os.path.join(os.path.dirname(streamlit.__file__), 'static')
streamlit_path = os.path.join(streamlit_static_dir, 'index.html')

# 원본 index.html 백업 생성
shutil.copy2(streamlit_path, streamlit_path + '.bak')

# 원본 index.html 읽기
with open(streamlit_path, 'r') as file:
    html_content = file.read()

# HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# 새 메타태그 정의
meta_tags = [
    # 일반 SEO
    {'name': 'description', 'content': '스트림릿 SEO 테스트'},
    
    # Open Graph: 카카오톡 SEO에 영향을 주는 부분
    {'property': 'og:type', 'content': 'website'},
    {'property': 'og:url', 'content': 'http://url:8501'},
    {'property': 'og:title', 'content': '스트림릿 SEO 테스트'},
    {'property': 'og:description', 'content': '스트림릿 SEO 테스트'},
]

# head에 새 메타태그 추가
for tag in meta_tags:
    new_tag = soup.new_tag('meta')
    for key, value in tag.items():
        new_tag[key] = value
    soup.head.append(new_tag)

# 수정된 HTML 저장
with open(streamlit_path, 'w') as file:
    file.write(str(soup))