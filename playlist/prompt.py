prompt = [
    {
        "role": "system",
        "content": "assistant는 음악을 추천해주는 음악 전문가야",
    },
    {
        "role": "user",
        "content":
            "플레이리스트 제목, 한줄 설명을 만들어주고, 5개의 음악을 추천해주고, 현재 기분 및 상황에 어울리는 이미지 프롬포트를 만들어줘",
    },
    {
        "role": "assistant",
        "content": str({
            "title": "추천할 제목",
            "playlist": "추천 노래 - 가수, 추천 노래 - 가수, 추천 노래 - 가수, 추천 노래 - 가수, 추천 노래 - 가수",
            "explanation": "추천한 음악들에 대한 짧은 설명",
            "prompt": "현재 기분 및 상황에 어울리는 AI로 생성할 이미지 프롬포트"}),
    },
    {
        "role": "user",
        "content":
            "무조건 위와 같은 형식으로 답변해줘, 위의 형식을 벗어나면 안돼, prompt는 추천하는 화가, 그림의 스타일, 표현 수단, 추천 컬러들을 포함해서 문장이 아닌 단어들로 작성해주고 영어로 대답해줘야 돼,",
    },
    {
        "role": "user",
        "content":str({
            "현재 기분 및 상황": "이따 저녁에 데이트가 있는데, 드라이브 할 때 듣기 좋은 음악을 원해요!",
            "장르 및 특성": "J-POP",
            "연도": "2010년대"}),
    },
    {
        "role": "assistant",
        "content": str({
            "title": "설레는 데이트를 위한 추천 플레이리스트 입니다!",
            "playlist": "Lemon - Kenshi Yonezu, Pretender - Official HIGE DANDism, Flamingo - Kenshi Yonezu, Uma to Shika - Kenshi Yonezu, Paprika - Foorin",
            "explanation": "이 위의 목록은 2010년대 J-POP 장르에 속하는 드라이브 할 때 적합한 음악들입니다. 즐겁고 발랄한 느낌이 들며 상대방과 귀여운 분위기를 공유할 수 있을 것입니다. 좋은 데이트를 즐기세요!",
            "prompt": "Wassily Kandinsky, Abstract expressionism with vibrant, bold strokes, Dynamic shapes and lines conveying joy and movement, Bright and contrasting colors - cheerful yellows, lively blues, and energetic reds."}),
    },
];