import sys
from cluster_management.client.cli_client import Client
from cluster_management.controller.cluster_client_controller import ClusterClientController
from cluster_management.service.httpx_service import HttpxService
from cluster_management.constants import HOSTS

class Executor:

    @staticmethod
    def execute():
        '''
        This is function executes the API to create or delete a group on a cluster
        '''

        # Check if all the required parameters are submitted by the user
        if len(sys.argv) != 3:
            print("Usage: python client.py <create|delete> <groupId>")
            sys.exit(1)

        action = sys.argv[1] # get user entered action
        group_id = sys.argv[2] # get user entered group_id

        client_controller = ClusterClientController(HttpxService, hosts=HOSTS)
        client = Client(client_controller)
        client.run(action=action, group_id=group_id)

Executor.execute()