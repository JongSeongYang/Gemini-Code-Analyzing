import pathlib
import textwrap

import google.generativeai as genai
import aspose.words as aw
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

# C 파일 읽어오기
filename = 'tr_FNCE70OP0008R.h'
f = open(filename, 'rt', encoding='UTF8')     # mode = 부분은 생략해도 됨
lines = f.read()
header_txt = ""

for line in lines:
    header_txt += line
# print(header_txt)

model = genai.GenerativeModel('gemini-pro') # 텍스트 전용 모델
# 텍스트 생성
request = "아래 C 코드 Input, Output 정리해서 한국어와 영어 두 개 만들어줘\n"
response = model.generate_content(request + header_txt)

# 답변 내용 보기
print(response.text)
to_markdown(response.text)

