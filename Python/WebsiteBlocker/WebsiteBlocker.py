from datetime import datetime as dt
import time

hostFilePath = r"C:\Windows\System32\drivers\etc\hosts"
hostTestPath = r"hosts"
redirectIP = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com", "www.instagram.com", ]

# Change to desired test path for testing
path = hostFilePath

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14) :
        print("Working hours")

        with open(path, 'r+') as fileHandle:
            fileContent = fileHandle.read()
            print(fileContent)

            for website in websiteList:
                if website in fileContent:
                    pass
                else:
                    fileHandle.write(redirectIP + ' ' + website + '\n')


    else:
        print("Non Working hours")

        with open(path, 'r+') as fileHandle:
            fileContent = fileHandle.readlines();
            # print(fileContent)

            fileHandle.seek(0)

            for line in fileContent:
                if not any(website in line for website in websiteList):
                    fileHandle.write(line)

            fileHandle.truncate()



    time.sleep(5)

