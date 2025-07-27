from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 입력 데이터 구조 정의
class ChatRequest(BaseModel):
    question: str

# 기본 응답 처리 로직
@app.post("/chat")
def chat_response(req: ChatRequest):
    q = req.question.replace(" ", "") # 띄어쓰기 써도 인식되게끔

    # 키워드 기반 응답 예시
    if "학사일정" in q:
        return {"answer": "2025년 1학기 종강일은 6월 20일입니다."}
    elif "등록금" in q:
        return {"answer": "등록금 납부 기간은 2025년 2월 10일부터 2월 17일까지입니다."}
    elif "도서관" in q:
        return {"answer": "도서관 운영 시간은 평일 9시부터 22시까지입니다."}
    else:
        return {"answer": "죄송합니다. 해당 질문에 대한 정보가 없습니다."}
