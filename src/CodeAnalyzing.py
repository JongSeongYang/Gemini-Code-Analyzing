import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

print(" >>> Start")

# 서식이 지정된 Markdown 텍스트를 표시하는 함수
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# 제미나이 API 키 설정
GOOGLE_API_KEY = 'AIzaSyBM5NNSWJ_f0WkM_aOpdmnjExDxJiA_4yc'
genai.configure(api_key=GOOGLE_API_KEY)


# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model = genai.GenerativeModel('gemini-pro') # 텍스트 전용 모델
# 텍스트 생성
response = model.generate_content("파이썬 설명해줘")

# 답변 내용 보기
print(response.text)
to_markdown(response.text)