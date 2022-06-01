from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.execution_queue import ExecutionQueue
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    queue_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/queues/{queue_id}".format(client.base_url, queue_id=queue_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExecutionQueue, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ExecutionQueue.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExecutionQueue, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    queue_id: str,
    *,
    client: Client,
) -> Response[Union[ExecutionQueue, HTTPValidationError]]:
    """Get Queue

    Args:
        queue_id (str):

    Returns:
        Response[Union[ExecutionQueue, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    queue_id: str,
    *,
    client: Client,
) -> Optional[Union[ExecutionQueue, HTTPValidationError]]:
    """Get Queue

    Args:
        queue_id (str):

    Returns:
        Response[Union[ExecutionQueue, HTTPValidationError]]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: Client,
) -> Response[Union[ExecutionQueue, HTTPValidationError]]:
    """Get Queue

    Args:
        queue_id (str):

    Returns:
        Response[Union[ExecutionQueue, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    queue_id: str,
    *,
    client: Client,
) -> Optional[Union[ExecutionQueue, HTTPValidationError]]:
    """Get Queue

    Args:
        queue_id (str):

    Returns:
        Response[Union[ExecutionQueue, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
        )
    ).parsed
