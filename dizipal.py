import requests

def findLink():
  for i in range(200,250):
    try:    
      r = requests.get("https://dizipal"+str(i)+".com", allow_redirects=False)
      x = r.status_code
      #print(x)
      a = r.headers['X-Pingback']
      if x == 200 and a == 'https://dizipal142.com/xmlrpc.php':
        return 'https://dizipal' + str(i) + '.com'
    except:
      #print(i)
      continue
  for i in range(100,200):
    try:    
      r = requests.get("https://dizipal"+str(i)+".com", allow_redirects=False)
      x = r.status_code
      #print(x)
      a = r.headers['X-Pingback']
      if x == 200 and a == 'https://dizipal142.com/xmlrpc.php':
        return 'https://dizipal' + str(i) + '.com'
    except:
      #print(i)
      continue
  for i in range(200,400):
    try:    
      r = requests.get("https://dizipal"+str(i)+".com", allow_redirects=False)
      x = r.status_code
      #print(x)
      a = r.headers['X-Pingback']
      if x == 200 and a == 'https://dizipal142.com/xmlrpc.php':
        return 'https://dizipal' + str(i) + '.com'
    except:
      #print(i)
      continue
