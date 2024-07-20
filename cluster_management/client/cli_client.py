from cluster_management.interface.cleint_interface import ClientInterface

class Client:
    '''
    CLI client executes API's via command line interface
    '''
    def __init__(self, client_controller:ClientInterface) -> None:
        self.client = client_controller

    def run(self, action:str, group_id:str):
        '''
        Run the client to perform action
        Parameters:-    
            action: str = <create>/<delete>
            group_id: str = <group_id> 
        '''
        if action == "create":
            self.client.create_group(group_id)
        
        elif action == "delete":
            self.client.delete_group(group_id)
        
        else:
            print("Invalid action, use create/delete")