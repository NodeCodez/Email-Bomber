import requests

   form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key, 
            "pageurl": pageurl, 
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"
    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status']==0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            status = 1