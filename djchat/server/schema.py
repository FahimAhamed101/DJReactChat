from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from .serializers import SeverSerializer, ChannelSerializer

server_list_docs = extend_schema(
    responses=SeverSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name='category',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='Retrieve list of servers by category.'
        ),
        OpenApiParameter(
            name='qty',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Retrieve specified number of servers'
        ),
        OpenApiParameter(
            name='by_user',
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description='Retrieve servers belongs to user'
        ),
        OpenApiParameter(
            name='server_id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Retrieve specific server by its ID'
        ),
        OpenApiParameter(
            name='with_num_members',
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description='Retrieve a server with its number of members'
        ),
    ],
)