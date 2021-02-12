from kavenegar import *
import urllib
import csv

test = False
#file="190+.csv"
url = "http://encinowear.com/tmp/210.csv"
list2 = urllib.request.urlopen(url)
list1 = list2.read()
s = list1.decode('utf-8')
a = s.split("\n")

for line in a:

    b = line.split(",")
    if (len(b) > 2):
        print('receptor : {} , name : {} , token2 : {}'.format(b[0],b[1], b[2]))

if test == False:
    for line in a:
        b = line.split(",")
        print('receptor : {} , name : {} , token2: {}'.format(b[0], b[1], b[2]))
        try:
            api = KavenegarAPI(
                '5877764937446349654450616A424C35756750464F62626431464F587678616866572F6B37344B6A576F383D/')
            params = {

                'receptor': b[0],
                'token': b[1],  # Array of String

                'token2': "encino10",
                'template': "DiscountCode"

            }
            response = api.verify_lookup(params)
            print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)
