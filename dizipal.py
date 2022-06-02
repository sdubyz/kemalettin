import requests

def findLink(n,k):
  for i in range(n,k):
    try:
      r = requests.get("https://dizipal"+str(i)+".com", allow_redirects=False, timeout=4.0)
      x = r.status_code
      t = r.text
      html = "DiziPAL - dizi, film ve anime izle"
      # a = r.headers['X-Pingback']
      # print("Status code: " + str(i) + " - " + str(x) + " - " + a + "\n")
      # nameFile = 'dizipal.txt'
      # file1 = open(nameFile, "r")
      # prev = file1.read() + '/xmlrpc.php'
      #f ile1.close()
      if x == 200 and html in t:
        return 'https://dizipal' + str(i) + '.com'
    except:
      continue
  return "0"

