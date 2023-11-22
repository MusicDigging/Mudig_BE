from drf_spectacular.utils import OpenApiExample, extend_schema, OpenApiParameter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Avg, Min, Max, Sum 
from .serializers import MusicSerializer, PlaylistSerializer
from .models import Music
import random

###################
# schema-option 정리
# responses=ClassroomSerializer,
# methods=["GET", "POST", "DELETE", "PUT", "PATCH"],
# auth=["string"],
# operation_id: Optional[str] = None,
# parameters: Optional[List[Union[OpenApiParameter, _SerializerType]]] = None,
# request: Any = empty,
# auth: Optional[List[str]] = None,
# deprecated: Optional[bool] = None,
# exclude: bool = False,
# operation: Optional[Dict] = None,
# methods: Optional[List[str]] = None,
# versions: Optional[List[str]] = None,
# examples: Optional[List[OpenApiExample]] = None,

# operation_id : 자동으로 설정되는 id 값, 대체로 수동할당하여 쓰진 않음
# parameters : 해당 path로 받기로 예상된 파라미터 값 (Serializer or OpenApiParameter 사용)
# request : 요청시 전달될 content의 형태
# responses : 응답시 전달될 content의 형태
# auth : 해당 method에 접근하기 위한 인증방법
# description: 해당 method 설명
# summary : 해당 method 요약
# deprecated : 해당 method 사용여부
# tags : 문서상 보여줄 묶음의 단위
# exclude : 문서에서 제외여부
# operation : ??? json -> yaml 하기위한 dictionary???
# methods : 요청 받을 Http method 목록
# versions : 문서화 할때 사용할 openAPI 버전
# examples : 요청/응답에 대한 예시
####################

# Create your views here.

class RandomMovieView(APIView):
    @extend_schema(
        summary="랜덤 뮤비",  # summary : 해당 method 요약
        description="랜덤 뮤비를 불러오는 API 입니다.",  # description: 해당 method 설명
        tags=["RandomMovie"],  # tags : 문서상 보여줄 묶음의 단위
        responses=MusicSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                summary="summary example",
                name="success_example",
                value=[{
                    "id": 14,
                    "title": "Snowman",
                    "artist": "Sia",
                    "thumbnail": "https://i.ytimg.com/vi/gset79KMmt0/mqdefault.jpg",
                    "information": "https://www.youtube.com/embed/yuFI5KSPAt4",
                    "created_at": "2023-08-24T10:01:38",
                },{
                    "id": 7,
                    "title": "Snow",
                    "artist": "Red Hot Chili Peppers",
                    "thumbnail": "https://i.ytimg.com/vi/yuFI5KSPAt4/mqdefault.jpg",
                    "information": "https://www.youtube.com/embed/yuFI5KSPAt4",
                    "created_at": "2023-08-24T10:01:38",
                },{
                    "id": 15,
                    "title": "Winter Song",
                    "artist": "Sara Bareilles",
                    "thumbnail": "https://i.ytimg.com/vi/budTp-4BGM0/mqdefault.jpg",
                    "information": "https://www.youtube.com/embed/yuFI5KSPAt4",
                    "created_at": "2023-08-24T10:01:38",
                }],
            ),
        ],
    )
    def get(self, request):
        try:
            max_id = Music.objects.all().aggregate(max_id=Max("id"))['max_id'] # id Max 값 가져오기
            all_musiclist = [i for i in range(1,max_id+1)] # 모든 뮤직 리스트
            already_musiclist = [4,5,6] # 이미 본 리스트들
            result = list(set(all_musiclist) - set(already_musiclist)) # 리스트 차집합
            
            random_musics = random.sample(result,3) # 랜덤 3개 뽑기
            queryset = Music.objects.filter(id__in=random_musics) # 해당 리스트를 검색
            # queryset = Music.objects.exclude(id__in=random_musics) # exclud 해당 리스트를 제외하고 검색

            serializer = MusicSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
        
class EventPlaylistGenerate(APIView):
    @extend_schema(
        summary="이벤트성 플레이리스트 생성 기능",  # summary : 해당 method 요약
        description="이벤트성으로 한 문장으로 플레이리스트 생성 기능에 대한 API 입니다.",  # description: 해당 method 설명
        tags=["EventPlaylistGenerate"],  # tags : 문서상 보여줄 묶음의 단위
        responses=PlaylistSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                summary="summary example",
                name="success_example",
                value={
                    "id": 1,
                    "title": "Example Title 01",
                    "writer": "user01",
                    "thumbnail": "Karlo/url",
                    "music": [{
                        "id": 1,
                        "title": "Snowman",
                        "artist": "Sia",
                        "thumbnail": "https://i.ytimg.com/vi/gset79KMmt0/mqdefault.jpg",
                        "information": "https://www.youtube.com/embed/yuFI5KSPAt4",
                        "created_at": "2023-08-24T10:01:38"},],
                    "created_at": "2023-08-24T10:01:38",
                },
            ),
        ],
    )
    def post(self, request):
        try:
            queryset = Music.objects.all()
            serializer = MusicSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)