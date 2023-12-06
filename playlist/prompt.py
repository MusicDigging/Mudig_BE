prompt = [
    {
        "role": "system",
        "content": "assistant는 음악을 추천해주는 음악 전문가야, 그리고 감성적인 글을 잘쓰는 사람이야",
    },
    {
        "role": "user",
        "content":
            """플레이리스트 제목, 한줄 설명을 감성적인 분위기가 느껴지게 만들어주고, 
            5개의 음악을 추천해주고, 이 플레이리스트에 어울리는 이미지 프롬포트와 키워드 3개를 알려줘""",
    },
    {
        "role": "assistant",
        "content": str({
            "title": "추천할 제목",
            "playlist": [
                {"song": "음악 1","singer": "가수 1"},
                {"song": "음악 2","singer": "가수 2"},
                {"song": "음악 3","singer": "가수 3"},
                {"song": "음악 4","singer": "가수 4"},
                {"song": "음악 5","singer": "가수 5"},],
            "explanation": "추천한 음악들에 대한 짧은 설명",
            "prompt": "현재 해당 플레이리스트와 어울리는 AI로 생성할 이미지 프롬포트",
            "keyword": "키워드1,키워드2,키워드3"}),
    },
    {
        "role": "user",
        "content":
            """무조건 위와 같은 형식으로 답변해줘, 위의 형식을 벗어나면 안돼, prompt는 추천하는 화가, 그림의 스타일, 표현 수단, 추천 컬러들을 포함해서 문장이 아닌 단어들로 작성해주고 무조건 영어로 대답해줘야 돼 그리고 prompt하고 답변에만 작은따음표 붙혀야돼! 음악, 가수 에서 sia feat. sam smith 이렇게 json에러 안나게 작은따음표 큰따음표, : 이런거 붙히지 말아줘 , 내용 중간에 강조하려고 큰따음표, 작은 따음표 절대 붙이지마
            explanation\": \"감정을 자극하는 Pop 장르의 노래 중 \"don\'t\"이 들어간 이렇게 답변하지말고 don\'t 이렇게만 해줘
            내용 중간에 무조건 큰따음표, 작은따음표 쓰면 안돼"""
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
            "playlist":[
                {"song": "Lemon","singer": "Kenshi Yonezu"},
                {"song": "Pretender","singer": "Official HIGE DANDism"},
                {"song": "Flamingo","singer": "Kenshi Yonezu"},
                {"song": "Uma to Shika","singer": "Kenshi Yonezu"},
                {"song": "Paprika","singer": "Foorin"},],
            "explanation": "이 위의 목록은 2010년대 J-POP 장르에 속하는 드라이브 할 때 적합한 음악들입니다. 즐겁고 발랄한 느낌이 들며 상대방과 귀여운 분위기를 공유할 수 있을 것입니다. 좋은 데이트를 즐기세요!",
            "prompt": "Wassily Kandinsky, Abstract expressionism with vibrant, bold strokes, Dynamic shapes and lines conveying joy and movement, Bright and contrasting colors - cheerful yellows, lively blues, and energetic reds.",
            "keyword": "드라이브,데이트,저녁"}),
    },
];

event_prompt = [
    {
        "role": "system",
        "content": "assistant는 음악을 추천해주는 음악 전문가야, 그리고 감성적인 글을 잘쓰는 사람이야",
    },
    {
        "role": "user",
        "content":
            """플레이리스트 제목, 한줄 설명을 감성적인 분위기가 느껴지게 만들어주고, 
            5개의 음악을 추천해주고, 이 플레이리스트에 어울리는 이미지 프롬포트와 키워드 3개를 알려줘""",
    },
    {
        "role": "assistant",
        "content": str({
            "title": "추천할 제목",
            "playlist": [
                {"song": "음악 1","singer": "가수 1"},
                {"song": "음악 2","singer": "가수 2"},
                {"song": "음악 3","singer": "가수 3"},
                {"song": "음악 4","singer": "가수 4"},
                {"song": "음악 5","singer": "가수 5"},],
            "explanation": "추천한 음악들에 대한 짧은 설명",
            "prompt": "현재 해당 플레이리스트와 어울리는 AI로 생성할 이미지 프롬포트",
            "keyword": "키워드1,키워드2,키워드3"}),
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
            "장르 및 특성": "J-POP",}),
    },
    {
        "role": "assistant",
        "content": str({
            "title": "설레는 데이트를 위한 추천 플레이리스트 입니다!",
            "playlist":[
                {"song": "Lemon","singer": "Kenshi Yonezu"},
                {"song": "Pretender","singer": "Official HIGE DANDism"},
                {"song": "Flamingo","singer": "Kenshi Yonezu"},
                {"song": "Uma to Shika","singer": "Kenshi Yonezu"},
                {"song": "Paprika","singer": "Foorin"},],
            "explanation": "이 위의 목록은 2010년대 J-POP 장르에 속하는 드라이브 할 때 적합한 음악들입니다. 즐겁고 발랄한 느낌이 들며 상대방과 귀여운 분위기를 공유할 수 있을 것입니다. 좋은 데이트를 즐기세요!",
            "prompt": "Wassily Kandinsky, Abstract expressionism with vibrant, bold strokes, Dynamic shapes and lines conveying joy and movement, Bright and contrasting colors - cheerful yellows, lively blues, and energetic reds.",
            "keyword": "드라이브,데이트,저녁"}),
    },
];