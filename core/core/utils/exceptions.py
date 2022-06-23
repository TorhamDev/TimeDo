from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response


class YouAreNotOwnerOfThisTimer(APIException):
    status_code = 403
    default_detail = 'You are not owner of this timer'
    default_code = 'not_timer_owner'
