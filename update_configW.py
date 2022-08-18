'''execute this script when adding new crosschain asset'''
from monitor_utility import UpdateConfigUtility
import requests
import json
class UPDATE_CONFIG:
    def __init__(self,access_token):
        self.update2github = UpdateConfigUtility.UploadConfigToGitHub(access_token)

    def update_nodes(self,new_node):
        '''
        :param new_node: json_str
                {	"XRP": {
                    "main": ["wss://s1.ripple.com/"],
                    "test": ["wss://nodes-testnet.wandevs.org/xrp"]
                }
        :return:
        '''
        nodes = requests.get('https://raw.githubusercontent.com/Nevquit/configW/main/rpc_for_monitor.json').json()
        nodes.update(json.loads(new_node))
        content =  json.dumps(nodes)
        self.update2github.uploadFile('https://api.github.com/repos/Nevquit/configW/contents/rpc_for_monitor.json',content)


if __name__ == '__main__':
    nodes = '''
                {"testinggggg": {
                "main": ["wss://s1.ripple.com/"],
                "test": ["wss://nodes-testnet.wandevs.org/xrp"]
            }}
    '''
    with open('.access_token.json','r') as f:
        ac_token = json.load(f)['ac_token']
    update = UPDATE_CONFIG(ac_token)
    update.update_nodes(nodes)

