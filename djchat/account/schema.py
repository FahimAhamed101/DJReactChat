from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from .serializers import AccountSerializer

account_docs = extend_schema(
    responses=AccountSerializer(),
    parameters=[
        OpenApiParameter(
            name='userId',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Retrieve a user by Id.'
        ),
    ],
)