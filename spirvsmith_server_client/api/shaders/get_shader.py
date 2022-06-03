from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.shader_data import ShaderData
from ...types import Response


def _get_kwargs(
    shader_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/shaders/{shader_id}".format(client.base_url, shader_id=shader_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, ShaderData]]:
    if response.status_code == 200:
        response_200 = ShaderData.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, ShaderData]]:
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
) -> Response[Union[HTTPValidationError, ShaderData]]:
    """Get Shader

    Args:
        shader_id (str):

    Returns:
        Response[Union[HTTPValidationError, ShaderData]]
    """

    kwargs = _get_kwargs(
        shader_id=shader_id,
        client=client,
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
) -> Optional[Union[HTTPValidationError, ShaderData]]:
    """Get Shader

    Args:
        shader_id (str):

    Returns:
        Response[Union[HTTPValidationError, ShaderData]]
    """

    return sync_detailed(
        shader_id=shader_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    shader_id: str,
    *,
    client: Client,
) -> Response[Union[HTTPValidationError, ShaderData]]:
    """Get Shader

    Args:
        shader_id (str):

    Returns:
        Response[Union[HTTPValidationError, ShaderData]]
    """

    kwargs = _get_kwargs(
        shader_id=shader_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    shader_id: str,
    *,
    client: Client,
) -> Optional[Union[HTTPValidationError, ShaderData]]:
    """Get Shader

    Args:
        shader_id (str):

    Returns:
        Response[Union[HTTPValidationError, ShaderData]]
    """

    return (
        await asyncio_detailed(
            shader_id=shader_id,
            client=client,
        )
    ).parsed
