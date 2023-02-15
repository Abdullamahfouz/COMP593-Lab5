import requests
DAD_JOKES_API_URL = 'https://icanhazdadjoke.com/'
DAD_JOKES_SEARCH_URL = f'{DAD_JOKES_API_URL}/search'

def main():
   jokes_list = search_for_dad_jokes('cow')
   print(*jokes_list, sep='\n' )
   return
def search_for_dad_jokes(search_term):
     # setup the header parameters 
    header_pram = {
        'Accept': 'application/json'
     }
    #setup the wuery string params
    query_str_params ={
        'term' : search_term
    }
    
    print('sending GET request to Dad Jokes API ....', end='')
    
    resp_msg = requests.get (DAD_JOKES_SEARCH_URL, headers=header_pram, params=query_str_params)
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        jokes_portion = body_dict["results"]
        jokes_list = [j['joke'] for j  in jokes_portion]
        return jokes_list
    
    else:
        print ('fail')
        print (f'Status code: {resp_msg.status_code} ({resp_msg.reason})')


def get_random_dad_joke():
    """Get a random dad joke 
    Returns:
        str: dad jokes
    """
    # setup the header parameters 
    header_pram = {
        'Accept': 'application/json'
     }
    print('sending GET request to Dad Jokes API ....', end='')
    #send the get request to the Pastebin Api
    resp_msg = requests.get (DAD_JOKES_API_URL, headers=header_pram)
    
    if resp_msg.ok:
        print('success')
        joke_dict = resp_msg.json()
        return joke_dict['joke']
    else:
        print ('fail')
        print (f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
       
    
    
    









    
if __name__ == '__main__':
    main()