from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.shader_data import ShaderData
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/shaders/next_mismatch".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ShaderData]:
    if response.status_code == 200:
        response_200 = ShaderData.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ShaderData]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[ShaderData]:
    """Get Next Mismatch

    Returns:
        Response[ShaderData]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[ShaderData]:
    """Get Next Mismatch

    Returns:
        Response[ShaderData]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[ShaderData]:
    """Get Next Mismatch

    Returns:
        Response[ShaderData]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[ShaderData]:
    """Get Next Mismatch

    Returns:
        Response[ShaderData]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
