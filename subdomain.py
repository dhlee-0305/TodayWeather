import requests
import json
from elapsed import elapsed
from logger import getLogger

log = getLogger('subdomain')

@elapsed
def subdomain(domain):
    log = getLogger('subdomain')

    if len(domain) > 1:
        response = requests.get("http://api.subdomain.center/?domain="+domain).json()
        result = "\n".join(response)
    else:
        result = 'usage: subdomain(domain)'

    if len(result) == 0:
        result = 'no result'

    return result

if __name__ == '__main__':
    domain = 'starbucks.co.kr'
    result = subdomain(domain)
    log.debug(result)
    print(result)