# REST API 호출, 이미지 파일 처리에 필요한 라이브러리
import requests
import json
import urllib
from PIL import Image
import os
import io
from .uploads import S3ImgUploader 

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY =  os.environ['KARLO_API_KEY']
# 이미지 생성하기 요청
negative_prompt = "nsfw, low res, text, fullbody, extra digit, fewer digits, cropped face, worst quality, low quality, normal quality, watermark, blurry, hands, face distortion, distorted face, poorly drawn face, framework, tacky, hole, ugly, realistic" # 얘는 일단 고정

def t2i(prompt):
    r = requests.post(
        'https://api.kakaobrain.com/v2/inference/karlo/t2i',
        json = {
            'prompt': prompt,
            'negative_prompt': negative_prompt
        },
        headers = {
            'Authorization': f'KakaoAK {REST_API_KEY}',
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    # print('resopnsse', response)
    # result = Image.open(urllib.request.urlopen(response.get("images")[0].get("image")))
    result_image_data = urllib.request.urlopen(response.get("images")[0].get("image")).read()
    
    # print('result_image_data', result_image_data)
    uploader = S3ImgUploader(io.BytesIO(result_image_data))
    uploaded_url = uploader.upload('karlo')
    # print('resut', result)
    # result.save('./output/result.png', 'png') # 저장
    # result.show()
    return uploaded_url

# 프롬프트에 사용할 제시어
# prompt = "A cat with white fur"

# prompt = "'Vincent van Gogh, Impressionism with soft, blended brushstrokes, Serene and peaceful landscapes, Cool and calming color palette - shades of blues, greens, and grays." # GPT로 생성한 프롬포트로 요청


# 이미지 생성하기 REST API 호출
# response = t2i(prompt, negative_prompt)

# 응답의 첫 번째 이미지 생성 결과 출력하기