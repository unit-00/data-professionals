import requests
import time

def fetch_zipcode_zippo(pc):
    """
    pc: iterable of postal code
    ---
    returns a tuple of errors and fetched results
    """
    results = {}
    errors = []
    
    for i, post in enumerate(pc):
        if (post not in results):
            try:
                r = requests.get(f'http://api.zippopotam.us/us/{post}')
                results[post] = r.json()
            except:
                print('Some error has happened')
                print(i, post)
                errors.append(post)

        time.sleep(.2)
        if (i % 10 == 9):
            time.sleep(5)

        if (i % 50 == 0):
            print(f'{i} requests are done')
        

    return (errors, results)

def fetch_zipcode_ci(pc):
    links = {}
    errors = []
    url = 'https://www.ciclt.net/sn/clt/capitolimpact/gw_ziplist.aspx?ClientCode=capitolimpact&ZipCode='
    
    for i, l in enumerate(pc):
        try:
            r = requests.get(url + l)
            links[l] = r.content
        except:
            print('Error has occurred')
            print(i)
            print(l)
            errors.append(l)

        time.sleep(.2)

        if (i % 10 == 9):
            time.sleep(5)
        if (i % 20 == 0):
            print(f'{i} requests are done.')
    
    return errors, links