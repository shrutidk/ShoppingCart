from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


def base_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # check that a ValidationError exception is raised
    if isinstance(exc, ValidationError):
        # here prepare the 'custom_error_response' and
        # set the custom response data on response object
        if response.data.get("product", None):
            response.data = response.data["product"][0]


    return response