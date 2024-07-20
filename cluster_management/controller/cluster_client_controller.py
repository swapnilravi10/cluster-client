from typing import List
from cluster_management.interface.http_interface import HttpInterface
import httpx

class ClusterClientController:
    '''
    Cluster client performs actions
    '''
    def __init__(self, http_client:HttpInterface, hosts:List[str]) -> None:
        self.http_client = http_client
        self.hosts = hosts

    async def create_group(self, group_id):
        '''
        Create a group in a cluster
        Parameters:-
            group_id:str
        '''
        try:
            await self._perform_action_on_all_nodes('create', group_id)
            print(f'Group {group_id} created successfully.')
        
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
            await self._perform_action_on_all_nodes('delete', group_id)
        except Exception as exc:
            print(f'An error occurred: {exc}')
            await self._perform_action_on_all_nodes('delete', group_id)
        
    async def delete_group(self, group_id: str):
        '''
        Delete a group in a cluster
        Parameters:-
            group_id:str
        '''
        try:
            await self._perform_action_on_all_nodes('delete', group_id)
            print(f'Group {group_id} deleted successfully.')

        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
            await self._perform_action_on_all_nodes('delete', group_id)
        except Exception as exc:
            print(f'An error occurred: {exc}')

    
    async def _perform_action_on_all_nodes(self, action: str, group_id: str):
        for host in self.hosts:
            await self._perform_action(host, action, group_id) 
    
    async def _perform_action(self, host: str, action: str, group_id: str):
        url = f'{host}/v1/group/'
        data = {'groupId': group_id}
        response = None

        if action == 'create':
            response = await self.http_client.post(url, json=data)
        elif action == 'delete':
            response = await self.http_client.delete(url, json=data)
        
        response.raise_for_status()
        return response.json()