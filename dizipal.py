import requests

def findLink(n,k):
  for i in range(n,k):
    try:
      r = requests.get("https://dizipal"+str(i)+".com", allow_redirects=False, timeout=4.0)
      x = r.status_code
#      t = r.text
      a = r.headers['X-Pingback']
      if x == 200 and a == 'https://dizipal142.com/xmlrpc.php':
        return 'https://dizipal' + str(i) + '.com'
#    except KeyError:
#      html = """<!doctype html>
#<html lang="tr">
#<head>
#<script data-ad-client="ca-pub-5140063555116276" async #src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script> """
#      if x == 200 and t.startswith(html):
#        return 'https://dizipal' + str(i) + '.com'
    except:
      continue
  return "0"

