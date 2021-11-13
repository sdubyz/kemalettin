import urllib3
from bs4 import BeautifulSoup

def currency():
  http = urllib3.PoolManager()
  url = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"
  response = http.request('GET', url)
  a = BeautifulSoup(response.data, features="html5lib")

  # print(a.prettify())
  all_div2 = a.find_all('div')
  all_div = str(all_div2)
  keyword = '<div class="text-xl font-semibold text-white" data-socket-attr="s" data-socket-key="USD" data-socket-type="C">'
  before_key, keyword, after_key = all_div.partition(keyword)
  keyword2 = '</div>'
  curr, keyword2, after_key2 = after_key.partition(keyword2)


  return curr
#print(curr)