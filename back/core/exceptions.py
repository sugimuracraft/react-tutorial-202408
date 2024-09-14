from fastapi import status
from fastapi.exceptions import HTTPException


def raise_http_404_not_found():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=[
            {
                "type": "not found",
                "loc": [
                    "path",
                    "id",
                ],
                "msg": "Not found",
            },
        ],
    )
