import requests

r = requests.get('https://pypi.org')
if r.status_code==200:
    with open('inet.html', 'w', encoding='utf8') as outfile:
        # outfile.write(r.text)
        # pass
        ...


# print(r.text)