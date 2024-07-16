import pytest
from cluster_management.controller.cluster_client_controller import ClusterClientController 

@pytest.mark.asyncio
async def test_create_group():
    # Mock the httpx.AsyncClient responses here
    controller = ClusterClientController()
    await controller.create_group('testgroup')

@pytest.mark.asyncio
async def test_delete_group():
    # Mock the httpx.AsyncClient responses here
    controller = ClusterClientController()
    await controller.delete_group('testgroup')