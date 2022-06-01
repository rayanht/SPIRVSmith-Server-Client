from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.buffer_submission import BufferSubmission
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    shader_id: str,
    *,
    client: Client,
    json_body: BufferSubmission,
) -> Dict[str, Any]:
    url = "{}/buffers/{shader_id}".format(client.base_url, shader_id=shader_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    shader_id: str,
    *,
    client: Client,
    json_body: BufferSubmission,
) -> Response[Union[Any, HTTPValidationError]]:
    """Post Buffers

    Args:
        shader_id (str):
        json_body (BufferSubmission):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        shader_id=shader_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    shader_id: str,
    *,
    client: Client,
    json_body: BufferSubmission,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Post Buffers

    Args:
        shader_id (str):
        json_body (BufferSubmission):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        shader_id=shader_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    shader_id: str,
    *,
    client: Client,
    json_body: BufferSubmission,
) -> Response[Union[Any, HTTPValidationError]]:
    """Post Buffers

    Args:
        shader_id (str):
        json_body (BufferSubmission):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        shader_id=shader_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    shader_id: str,
    *,
    client: Client,
    json_body: BufferSubmission,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Post Buffers

    Args:
        shader_id (str):
        json_body (BufferSubmission):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            shader_id=shader_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
