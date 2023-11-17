import openai
import json
from .prompt import prompt
import os

def get_music_recommendation(situatuons, feature, year):
    openai.api_key = os.environ["OPEN_API_KEY"]  # 여기에 실제 API 키를 넣어주세요

    # 모델 - GPT 3.5 Turbo 선택
    model = "gpt-3.5-turbo"
    # 질문 작성하기
    query = {
        "role": "user",
        "content": str({
            "현재 기분 및 상황": situatuons,
            "장르 및 특성": feature,
            "연도": year
        }),
    }

    questions = {
        "role": "user",
        "content": str(query),
    }

    prompt.append(questions)
    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        timeout = 600
    )
    answer = response['choices'][0]['message']['content']

    return answer