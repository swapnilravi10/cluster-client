
from unittest.mock import AsyncMock, patch
from cluster_management.controller.cluster_client_controller import ClusterClientController
from cluster_management.service.httpx_service import HttpxService
import pytest

@pytest.mark.asyncio
@patch('cluster_management.service.httpx_service.HttpxService')
async def test_create_group_success(MockHttpxService):
    # Arrange
    mock_http_client = MockHttpxService.return_value
    mock_http_client.post = AsyncMock()
    controller = ClusterClientController(mock_http_client, hosts=['http://host1', 'http://host2'])

    # Act
    await controller.create_group('test-group')

    # Assert
    mock_http_client.post.assert_any_await('http://host1/v1/group/', json={'groupId': 'test-group'})
    mock_http_client.post.assert_any_await('http://host2/v1/group/', json={'groupId': 'test-group'})

@pytest.mark.asyncio
@patch('cluster_management.service.httpx_service.HttpxService')
async def test_create_group_failure(MockHttpxService):
    # Arrange
    mock_http_client = MockHttpxService.return_value
    mock_http_client.post = AsyncMock(side_effect=Exception('Failed to create group'))
    mock_http_client.delete = AsyncMock()
    controller = ClusterClientController(mock_http_client, hosts=['http://host1', 'http://host2'])

    # Act
    await controller.create_group('test-group')

    # Assert
    mock_http_client.post.assert_any_await('http://host1/v1/group/', json={'groupId': 'test-group'})
    mock_http_client.delete.assert_any_await('http://host1/v1/group/', json={'groupId': 'test-group'})
    mock_http_client.delete.assert_any_await('http://host2/v1/group/', json={'groupId': 'test-group'})

@pytest.mark.asyncio
@patch('cluster_management.service.httpx_service.HttpxService')
async def test_delete_group_success(MockHttpxService):
    # Arrange
    mock_http_client = MockHttpxService.return_value
    mock_http_client.delete = AsyncMock()
    controller = ClusterClientController(mock_http_client, hosts=['http://host1', 'http://host2'])

    # Act
    await controller.delete_group('test-group')

    # Assert
    mock_http_client.delete.assert_any_await('http://host1/v1/group/', json={'groupId': 'test-group'})
    mock_http_client.delete.assert_any_await('http://host2/v1/group/', json={'groupId': 'test-group'})

@pytest.mark.asyncio
@patch('cluster_management.service.httpx_service.HttpxService')
async def test_delete_group_failure(MockHttpxService):
    # Arrange
    mock_http_client = MockHttpxService.return_value
    mock_http_client.delete = AsyncMock(side_effect=Exception('Failed to delete group'))
    controller = ClusterClientController(mock_http_client, hosts=['http://host1'])

    # Act
    await controller.delete_group('test-group')

    # Assert
    mock_http_client.delete.assert_any_await('http://host1/v1/group/', json={'groupId': 'test-group'})