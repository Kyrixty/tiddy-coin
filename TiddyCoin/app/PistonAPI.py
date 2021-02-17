import requests
import json

POSTUrl = "https://emkc.org/api/v1/piston/execute"
GETUrl = "https://emkc.org/api/v1/piston/versions"

class Piston:
    '''
    Sends POST requests to the Piston API.
    Ensures security regarding executing the
    client's submitted code, as it is never 
    executed locally.

    Code must run in under 3 seconds.
    '''

    def sendSource(sourceCode: str, language: str, args: list):
        content = {
            "language": language,
            "source": r"{}".format(sourceCode),
            "args": args
        }

        response = requests.post(POSTUrl, content)

        return response.json()
    
    def get_languages(show_results=False):
        response = requests.get(GETUrl)

        if show_results:
            print(response.json())

        return response.json()
    
    def test():
        '''
        Sends basic python3 source code,
        expects output 'hello'.
        '''
        content = {
            "language": "python3",
            "source": "print('hello')",
            "args": []
        }

        response = requests.post(POSTUrl, content)

        print(response.json())

        if response.json()["output"]=="hello":
            return True