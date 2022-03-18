import urllib3

def findLink():
    for i in range(200, 250):
      try:        
        timeout = urllib3.util.Timeout(connect=0.2, read=3.0)
        proxy = urllib3.ProxyManager("https://localhost:3128/")
        http = urllib3.PoolManager(timeout=timeout)
        header = { 'host' : 'dizipal' + str(i) + '.com' }
        x = http.urlopen('GET', 'http://dizipal' + str(i) + '.com/', redirect="false", headers=header)
        s = x.data.decode()
        #print(x.headers)
        #print("\n")
        s1 = '\r<!doctype html>\n<html lang="tr">\n<head>'
        if s.startswith(s1) and x.headers['X-Pingback'] == 'https://dizipal142.com/xmlrpc.php':
          print(i)
          return 'http://dizipal' + str(i) + '.com'
      except:
        print("except")
    for i in range(100, 200):
      try:        
        timeout = urllib3.util.Timeout(connect=0.2, read=3.0)
        proxy = urllib3.ProxyManager("https://localhost:3128/")
        http = urllib3.PoolManager(timeout=timeout)
        header = { 'host' : 'dizipal' + str(i) + '.com' }
        x = http.urlopen('GET', 'http://dizipal' + str(i) + '.com/', redirect="false", headers=header)
        s = x.data.decode()
        #print(x.headers)
        #print("\n")
        s1 = '\r<!doctype html>\n<html lang="tr">\n<head>'
        if s.startswith(s1) and x.headers['X-Pingback'] == 'https://dizipal142.com/xmlrpc.php':
          print(i)
          return 'http://dizipal' + str(i) + '.com'
      except:
        print("except")    
