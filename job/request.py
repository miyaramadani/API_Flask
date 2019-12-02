import requests

# URL
url = 'http://localhost:5001/api/'

# Change the value of experience that you want to test
# payload = {'exp':2.7}

r = requests.post(url,json={'nilai':[[80, 99, 99, 90 ,100]]})
                
print(r.json())
