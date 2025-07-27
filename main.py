from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
print("내 API 키:", api_key)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 모든 출처 허용 (로컬 개발용)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 데이터 구조
class QuestionRequest(BaseModel):
    question: str

# POST /ask 엔드포인트
@app.post("/ask")
async def ask(req: QuestionRequest):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": req.question}
        ]
    )
    return {"answer": response.choices[0].message.content}
