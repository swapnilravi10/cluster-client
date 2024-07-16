from cluster_management.interface.http_interface import HttpInterface
import httpx

class HttpxService(HttpInterface):
    '''
    The httpx client
    '''

    def post(self, url: str, json: dict):
        with httpx.Client() as client:
            return client.post(url, json)
    
    def get(self, url: str, json: dict):
        with httpx.Client() as client:
            return client.get(url, json)

    def delete(self, url: str, json: dict):
        with httpx.Client() as client:
            return client.delete(url, json)
    