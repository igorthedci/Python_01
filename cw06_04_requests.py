import requests
# resp = requests.get('http://wikipedia.org')
# print(resp)
# print(resp.text)
# print(resp.status_code)
# print(resp.headers)
# print(resp.url)
#
# resp = requests.get('http://api.github.com/events')
# print(resp)
# print(resp.__doc__)
# print(resp.text)
# print(resp.status_code)
# print(resp.headers)
# print(resp.url)
#
url = 'http://httpbin.org/get'
dict_params = {"name": "Olena", "q": "Python"}
headers = {'User-Agent': 'cw06_04'}
r = requests.get(url, headers=headers, params=dict_params)
print(r.text)
print(r.url)
#
r_dict = r.json()
print(type(r_dict))
print(r_dict['headers']['Host'])
print(r.url)
#
url = 'http://httpbin.org/get'
dict_params = {"name": "Olena", "q": "Python"}
headers = {'User-Agent': 'cw06_04'}
r = requests.post(url, headers=headers, params=dict_params, data={"username": '111', password='***'})
print(r.status_code)
#