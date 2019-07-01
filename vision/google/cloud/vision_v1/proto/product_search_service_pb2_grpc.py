# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.vision_v1.proto import (
    product_search_service_pb2 as google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ProductSearchStub(object):
    """Manages Products and ProductSets of reference images for use in product
  search. It uses the following resource model:

  - The API has a collection of [ProductSet][google.cloud.vision.v1.ProductSet]
  resources, named `projects/*/locations/*/productSets/*`, which acts as a way
  to put different products into groups to limit identification.

  In parallel,

  - The API has a collection of [Product][google.cloud.vision.v1.Product]
  resources, named
  `projects/*/locations/*/products/*`

  - Each [Product][google.cloud.vision.v1.Product] has a collection of
  [ReferenceImage][google.cloud.vision.v1.ReferenceImage] resources, named
  `projects/*/locations/*/products/*/referenceImages/*`
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateProductSet = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/CreateProductSet",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.CreateProductSetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ProductSet.FromString,
        )
        self.ListProductSets = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/ListProductSets",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductSetsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductSetsResponse.FromString,
        )
        self.GetProductSet = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/GetProductSet",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.GetProductSetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ProductSet.FromString,
        )
        self.UpdateProductSet = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/UpdateProductSet",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.UpdateProductSetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ProductSet.FromString,
        )
        self.DeleteProductSet = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/DeleteProductSet",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.DeleteProductSetRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.CreateProduct = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/CreateProduct",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.CreateProductRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.Product.FromString,
        )
        self.ListProducts = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/ListProducts",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductsResponse.FromString,
        )
        self.GetProduct = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/GetProduct",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.GetProductRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.Product.FromString,
        )
        self.UpdateProduct = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/UpdateProduct",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.UpdateProductRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.Product.FromString,
        )
        self.DeleteProduct = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/DeleteProduct",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.DeleteProductRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.CreateReferenceImage = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/CreateReferenceImage",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.CreateReferenceImageRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ReferenceImage.FromString,
        )
        self.DeleteReferenceImage = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/DeleteReferenceImage",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.DeleteReferenceImageRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.ListReferenceImages = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/ListReferenceImages",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListReferenceImagesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListReferenceImagesResponse.FromString,
        )
        self.GetReferenceImage = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/GetReferenceImage",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.GetReferenceImageRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ReferenceImage.FromString,
        )
        self.AddProductToProductSet = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/AddProductToProductSet",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.AddProductToProductSetRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.RemoveProductFromProductSet = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/RemoveProductFromProductSet",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.RemoveProductFromProductSetRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.ListProductsInProductSet = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/ListProductsInProductSet",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductsInProductSetRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductsInProductSetResponse.FromString,
        )
        self.ImportProductSets = channel.unary_unary(
            "/google.cloud.vision.v1.ProductSearch/ImportProductSets",
            request_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ImportProductSetsRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class ProductSearchServicer(object):
    """Manages Products and ProductSets of reference images for use in product
  search. It uses the following resource model:

  - The API has a collection of [ProductSet][google.cloud.vision.v1.ProductSet]
  resources, named `projects/*/locations/*/productSets/*`, which acts as a way
  to put different products into groups to limit identification.

  In parallel,

  - The API has a collection of [Product][google.cloud.vision.v1.Product]
  resources, named
  `projects/*/locations/*/products/*`

  - Each [Product][google.cloud.vision.v1.Product] has a collection of
  [ReferenceImage][google.cloud.vision.v1.ReferenceImage] resources, named
  `projects/*/locations/*/products/*/referenceImages/*`
  """

    def CreateProductSet(self, request, context):
        """Creates and returns a new ProductSet resource.

    Possible errors:

    * Returns INVALID_ARGUMENT if display_name is missing, or is longer than
    4096 characters.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListProductSets(self, request, context):
        """Lists ProductSets in an unspecified order.

    Possible errors:

    * Returns INVALID_ARGUMENT if page_size is greater than 100, or less
    than 1.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetProductSet(self, request, context):
        """Gets information associated with a ProductSet.

    Possible errors:

    * Returns NOT_FOUND if the ProductSet does not exist.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateProductSet(self, request, context):
        """Makes changes to a ProductSet resource.
    Only display_name can be updated currently.

    Possible errors:

    * Returns NOT_FOUND if the ProductSet does not exist.
    * Returns INVALID_ARGUMENT if display_name is present in update_mask but
    missing from the request or longer than 4096 characters.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteProductSet(self, request, context):
        """Permanently deletes a ProductSet. Products and ReferenceImages in the
    ProductSet are not deleted.

    The actual image files are not deleted from Google Cloud Storage.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateProduct(self, request, context):
        """Creates and returns a new product resource.

    Possible errors:

    * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096
    characters.
    * Returns INVALID_ARGUMENT if description is longer than 4096 characters.
    * Returns INVALID_ARGUMENT if product_category is missing or invalid.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListProducts(self, request, context):
        """Lists products in an unspecified order.

    Possible errors:

    * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetProduct(self, request, context):
        """Gets information associated with a Product.

    Possible errors:

    * Returns NOT_FOUND if the Product does not exist.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateProduct(self, request, context):
        """Makes changes to a Product resource.
    Only the `display_name`, `description`, and `labels` fields can be updated
    right now.

    If labels are updated, the change will not be reflected in queries until
    the next index time.

    Possible errors:

    * Returns NOT_FOUND if the Product does not exist.
    * Returns INVALID_ARGUMENT if display_name is present in update_mask but is
    missing from the request or longer than 4096 characters.
    * Returns INVALID_ARGUMENT if description is present in update_mask but is
    longer than 4096 characters.
    * Returns INVALID_ARGUMENT if product_category is present in update_mask.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteProduct(self, request, context):
        """Permanently deletes a product and its reference images.

    Metadata of the product and all its images will be deleted right away, but
    search queries against ProductSets containing the product may still work
    until all related caches are refreshed.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateReferenceImage(self, request, context):
        """Creates and returns a new ReferenceImage resource.

    The `bounding_poly` field is optional. If `bounding_poly` is not specified,
    the system will try to detect regions of interest in the image that are
    compatible with the product_category on the parent product. If it is
    specified, detection is ALWAYS skipped. The system converts polygons into
    non-rotated rectangles.

    Note that the pipeline will resize the image if the image resolution is too
    large to process (above 50MP).

    Possible errors:

    * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096
    characters.
    * Returns INVALID_ARGUMENT if the product does not exist.
    * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing
    compatible with the parent product's product_category is detected.
    * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteReferenceImage(self, request, context):
        """Permanently deletes a reference image.

    The image metadata will be deleted right away, but search queries
    against ProductSets containing the image may still work until all related
    caches are refreshed.

    The actual image files are not deleted from Google Cloud Storage.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListReferenceImages(self, request, context):
        """Lists reference images.

    Possible errors:

    * Returns NOT_FOUND if the parent product does not exist.
    * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less
    than 1.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetReferenceImage(self, request, context):
        """Gets information associated with a ReferenceImage.

    Possible errors:

    * Returns NOT_FOUND if the specified image does not exist.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddProductToProductSet(self, request, context):
        """Adds a Product to the specified ProductSet. If the Product is already
    present, no change is made.

    One Product can be added to at most 100 ProductSets.

    Possible errors:

    * Returns NOT_FOUND if the Product or the ProductSet doesn't exist.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RemoveProductFromProductSet(self, request, context):
        """Removes a Product from the specified ProductSet.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListProductsInProductSet(self, request, context):
        """Lists the Products in a ProductSet, in an unspecified order. If the
    ProductSet does not exist, the products field of the response will be
    empty.

    Possible errors:

    * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ImportProductSets(self, request, context):
        """Asynchronous API that imports a list of reference images to specified
    product sets based on a list of image information.

    The [google.longrunning.Operation][google.longrunning.Operation] API can be
    used to keep track of the progress and results of the request.
    `Operation.metadata` contains `BatchOperationMetadata`. (progress)
    `Operation.response` contains `ImportProductSetsResponse`. (results)

    The input source of this method is a csv file on Google Cloud Storage.
    For the format of the csv file please see
    [ImportProductSetsGcsSource.csv_file_uri][google.cloud.vision.v1.ImportProductSetsGcsSource.csv_file_uri].
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ProductSearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateProductSet": grpc.unary_unary_rpc_method_handler(
            servicer.CreateProductSet,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.CreateProductSetRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ProductSet.SerializeToString,
        ),
        "ListProductSets": grpc.unary_unary_rpc_method_handler(
            servicer.ListProductSets,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductSetsRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductSetsResponse.SerializeToString,
        ),
        "GetProductSet": grpc.unary_unary_rpc_method_handler(
            servicer.GetProductSet,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.GetProductSetRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ProductSet.SerializeToString,
        ),
        "UpdateProductSet": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateProductSet,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.UpdateProductSetRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ProductSet.SerializeToString,
        ),
        "DeleteProductSet": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteProductSet,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.DeleteProductSetRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "CreateProduct": grpc.unary_unary_rpc_method_handler(
            servicer.CreateProduct,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.CreateProductRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.Product.SerializeToString,
        ),
        "ListProducts": grpc.unary_unary_rpc_method_handler(
            servicer.ListProducts,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductsRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductsResponse.SerializeToString,
        ),
        "GetProduct": grpc.unary_unary_rpc_method_handler(
            servicer.GetProduct,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.GetProductRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.Product.SerializeToString,
        ),
        "UpdateProduct": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateProduct,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.UpdateProductRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.Product.SerializeToString,
        ),
        "DeleteProduct": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteProduct,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.DeleteProductRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "CreateReferenceImage": grpc.unary_unary_rpc_method_handler(
            servicer.CreateReferenceImage,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.CreateReferenceImageRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ReferenceImage.SerializeToString,
        ),
        "DeleteReferenceImage": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteReferenceImage,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.DeleteReferenceImageRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "ListReferenceImages": grpc.unary_unary_rpc_method_handler(
            servicer.ListReferenceImages,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListReferenceImagesRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListReferenceImagesResponse.SerializeToString,
        ),
        "GetReferenceImage": grpc.unary_unary_rpc_method_handler(
            servicer.GetReferenceImage,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.GetReferenceImageRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ReferenceImage.SerializeToString,
        ),
        "AddProductToProductSet": grpc.unary_unary_rpc_method_handler(
            servicer.AddProductToProductSet,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.AddProductToProductSetRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "RemoveProductFromProductSet": grpc.unary_unary_rpc_method_handler(
            servicer.RemoveProductFromProductSet,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.RemoveProductFromProductSetRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "ListProductsInProductSet": grpc.unary_unary_rpc_method_handler(
            servicer.ListProductsInProductSet,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductsInProductSetRequest.FromString,
            response_serializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ListProductsInProductSetResponse.SerializeToString,
        ),
        "ImportProductSets": grpc.unary_unary_rpc_method_handler(
            servicer.ImportProductSets,
            request_deserializer=google_dot_cloud_dot_vision__v1_dot_proto_dot_product__search__service__pb2.ImportProductSetsRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.vision.v1.ProductSearch", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
