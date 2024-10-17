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

# 모델 종류 리스트
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
model = genai.GenerativeModel('gemini-pro') # 텍스트 전용 모델

while True:
    try:
        # file name 입력 받기
        # input_filename = 'tr_FNCE70OP0008R'
        input_filename = input(">> TR Name : ")

        # C 파일 읽어 오기
        filename = input_filename + '.h'
        f = open(filename, 'rt', encoding='UTF8')
        lines = f.read()
        header_txt = ""

        for line in lines:
            header_txt += line
        # print(header_txt)
    except:
        print(">> [Error] File Open/Read Fail!!\n")
        continue
    try:
        # 텍스트 생성
        request = "아래 C 코드 Input, Output을 IN/OUT구분, 그리드구분, 필드명, 타입(사이즈), 설명 항목으로 정리해서 한국어 csv로 만들어줘.\n"
        # request = "Organize the C code input and output below into IN/OUT division, grid division, field name, type (size), and description items and format them in Korean in csv format.\n"
        response = model.generate_content(request + header_txt)
        break
    except:
        print(">> [Error] Fail Get Respoonse!!\n")
        continue
        # 답변 내용 보기
        # print(response.text)

to_markdown(response.text)

# 저장
w = open(input_filename + '.md', 'w')
w.writelines(response.text)
w.close()

# 마크 다운 저장
doc = aw.Document(input_filename + ".md")
doc.save(input_filename + ".pdf")

print(">> Program END \n")