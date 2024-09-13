from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from drf_spectacular.utils import extend_schema
from .models import Server, Category
from .serializers import SeverSerializer, CategorySerializer
from .schema import server_list_docs

# Create your views here.


class CategoryListViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


# class that provide CRUD operations
class ServerListViewSet(viewsets.ViewSet):

    queryset = Server.objects.all()
    # permission_classes = [IsAuthenticated]

    # GET - get a list as a response
    @server_list_docs
    def list(self, request):
        """
        Retrieve a list of servers based on optional query parameters.

        This method retrieves a list of servers based on the provided query parameters. The supported query parameters
        include 'category', 'qty', 'by_user', 'server_id', and 'with_num_members'.

        Args:

            request (Request): The request object containing query parameters.

        Returns:

            Response: A response containing serialized server data.

        Raises:

            AuthenticationFailed: If 'by_user' or 'by_server' parameters are provided but the user is not authenticated.
            ValidationError: If 'by_server' parameter is provided but the value is not valid, or if the server with the provided ID does not exist.

        Note:

            - 'category': Filters servers by category name.
            - 'qty': Limits the number of servers returned.
            - 'by_user': Filters servers by the authenticated user if provided.
            - 'server_id': Retrieves a specific server by its ID.
            - 'with_num_members': Annotates the queryset with the number of members in each server if 'true'.

        Examples:

            1. To retrieve a list of servers belonging to a specific category:

                GET /api/servers/select/?category=gaming

            2. To retrieve a list of servers with a limit on the number returned:

                GET /api/servers/select/?qty=10

            3. To retrieve a list of servers filtered by the authenticated user:

                GET /api/servers/select/?by_user=true

            4. To retrieve a specific server by its ID:

                GET /api/servers/select/?server_id=1

            5. To retrieve a list of servers with the number of members annotated:

                GET /api/servers/select/?with_num_members=true

            6. To retrieve a specific server by its ID with number of members

                GET /api/servers/select/?with_num_members=true&server_id=1

        """

        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_server = request.query_params.get("server_id")
        with_num_members = request.query_params.get("with_num_members") == "true"

        # if (by_user or by_server) and (not request.user.is_authenticated):
        #     raise AuthenticationFailed()

        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        if category:

            # fiter all servers by category ID (category in Server model is Foreign key which contains PK of category)
            # self.queryset = self.queryset.filter(category= category)

            # fiter all servers by category name (category in Server model is Foreign key which contains PK of category)
            self.queryset = self.queryset.filter(category__name=category)

        if by_server:
            previous_queries = self.queryset
            try:
                self.queryset = self.queryset.filter(id=by_server)
                if not self.queryset.exists() and not previous_queries.exists():
                    raise ValidationError(
                        detail=f"Server with id {by_server} is not found"
                    )
                if not self.queryset.exists() and previous_queries.exists():
                    raise ValidationError(
                        detail=f"Related data for server with id {by_server} is not found"
                    )
            except ValueError:
                raise ValidationError(detail="Server value error")

        if with_num_members:
            # with execution of below, self.queryset gets a field called num_members with the corresponding value
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if qty:
            # The [: int(qty)] part in Python is called slicing. It allows you to retrieve a portion of a sequence, such as a list or a queryset in this case
            self.queryset = self.queryset[: int(qty)]

        serializer = SeverSerializer(
            self.queryset, many=True, context={"num_members": with_num_members}
        )
        return Response(serializer.data)