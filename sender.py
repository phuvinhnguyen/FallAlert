from OnlineDatabase import GitHubManager
import requests
import json

GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'

def get_location():
    try:
        response = requests.get('http://ipinfo.io/')
        data = response.json()
        return json.dumps(data, indent=4)
    except requests.RequestException as e:
        return json.dumps({'error': 'Failed to get information from IP geolocation service'}, indent=4)

def public_calling():
    manager = GitHubManager(GITHUB_TOKEN)
    manager.push(
        'phuvinhnguyen/FallAlert',
        f'customer/warning.txt',
        get_location()
        )
    
if __name__ == '__main__':
    public_calling()