import requests

DEVELOPER_KEY = 'i-8pVNkWG9SUtbh3DJ8XY9c-vcKxoFFQ'
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'

def main():
    url = post_new_paste("this is the title" , "this\nis\nthe body", '1H',True)
    print(f'New paste URL; {url}')
def post_new_paste(title, body_text, expiration= '10M', listed=False) :
    """Posts a new public paste to PasteBin

    Args:
        title (str): paste title
        body_text (str): paste body text
        expiration (str, optional): Expiration date of paste (N = never, '10M' mintues. 1H, 1D, 1W, 2W, 1M, 6M, 1Y.) Default
        listed (bool, optional): _description_. Defaults to False.

    Returns:
        str : URL of the new Paste, if successful. None if unsucceful
    """
  
  
  # steup the ptams for the requests message
    paste_params = { 
         'api_dev_key' :  DEVELOPER_KEY,
         'api_option'  : 'paste',
         'api_paste_code': body_text, 
         'api_paste_name' : title,
         'api_paste_expire_date': expiration,
         'api_paste_private': 0 if listed else 1
                    
    }  
    
    print('sending POST request to PasteBin API ....', end='')
    #send the post request to the Pastebin Api
    resp_msg = requests.post (PASTEBIN_API_URL, data=paste_params)
    
    if resp_msg.ok:
        print('success')
        return resp_msg.text
    else:
        print ('fail')
        print (f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')
    
    
    
    
if __name__ == '__main__':
    main()