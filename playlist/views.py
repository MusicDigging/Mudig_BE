from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlaylistSerializer
from .models import Playlist

# Create your views here.

class PlaylistView(APIView):
    @extend_schema(
        summary="플리 목록 조회",  # summary : 해당 method 요약
        description="플리 목록 조회",  # description: 해당 method 설명
        tags=["Playlist"],  # tags : 문서상 보여줄 묶음의 단위
        responses=PlaylistSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                summary="summary example",
                name="success_example",
                value={
                    "id": 1,
                    "created_at": "2023-08-24T10:01:38",
                    "updated_at": "2023-08-28T10:01:28",
                    "writer": "User001",
                    "title": "title001",
                },
            ),
        ],

        # parameters=[
        #     OpenApiParameter(
        #         name="path_parameter",
        #         type=str,
        #         location=OpenApiParameter.PATH,
        #         description="아이디 입니다.",
        #         required=True,
        #     ),
        #     OpenApiParameter(
        #         name="text_parameter",
        #         type=str,
        #         description="text_param 입니다.",
        #         required=False,
        #     ),
        #     OpenApiParameter(
        #         name="select_parameter",
        #         type=str,
        #         description="first_param 입니다.",

        #         #enum : 받을 수 있는 값을 제한함
        #         enum=['선택1', '선택2', '선택3'],
        #         examples=[
        #             OpenApiExample(
        #                 name="Select Parameter Example",
        #                 summary="요약1",
        #                 description="설명글은 길게 작성합니다",
        #                 value="선택1",
        #             ),
        #             OpenApiExample(
        #                 "Select Parameter Example2",
        #                 summary="요약2",
        #                 description="두번째 설명글은 더 길게 작성합니다",
        #                 value="선택4",
        #             ),
        #         ],
        #     ),
        #     OpenApiParameter(
        #         name="date_parameter",
        #         type=OpenApiTypes.DATE,
        #         location=OpenApiParameter.QUERY,
        #         description="date filter",
        #         examples=[
        #             OpenApiExample(
        #                 name="이것은 Query Parameter Example입니다.",
        #                 summary="요약입니다",
        #                 description="설명글은 길게 작성합니다",
        #                 value="1991-03-02",
        #             ),
        #             OpenApiExample(
        #                 name="이것은 Query Parameter Example2입니다.",
        #                 summary="두번째 요약입니다",
        #                 description="두번째 설명글은 더 길게 작성합니다",
        #                 value="1993-08-30",
        #             ),
        #         ],
        #     ),
        # ],
    )
    def get(self, request):
        try:
            queryset = Playlist.objects.all()
            serializer = PlaylistSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)