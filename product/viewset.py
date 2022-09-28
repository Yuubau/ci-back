from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

from product.models import Product
from product.serializers import CreateProductSerializer, ProductResponseSerializer


class ProductViewset(ViewSet):
    @swagger_auto_schema(responses={200: ProductResponseSerializer(many=True)})
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductResponseSerializer(queryset, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @swagger_auto_schema(responses={200: ProductResponseSerializer()})
    def retrieve(self, request, pk=None):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductResponseSerializer(queryset)

        return Response(data=serializer.data, status=HTTP_200_OK)

    @swagger_auto_schema(
        request_body=CreateProductSerializer,
        responses={201: openapi.Response("The product was created")},
    )
    def create(self, request):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            Product.objects.create(
                name=serializer.validated_data["name"],
                price=serializer.validated_data["price"],
                description=serializer.validated_data["description"],
            )

            return Response(status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
