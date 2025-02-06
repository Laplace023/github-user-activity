#my get module for the project
import os
import json


def gitGet(argument, password):
    print(f"Fetching the event logs for {argument}...")
    
    #the api call, I still have to filter the events
    try:
        os.remove("tempData.json")
        output = os.system(f"""
        curl -L \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer {password}" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        https://api.github.com/users/{argument}/events \
        >>tempData.json
        """)
    #this writes the output to temp.json
    except:
        print("something is wrong")

    #writting it as json. I'll write it as a temporary json file
    #I have to change the output to a dictionary.
    with open("tempData.json", mode="r", encoding="utf-8") as jsonFile:
        listFile = json.load(jsonFile)
        print(type(listFile))
    for x in listFile:
        print(f"{x["created_at"]}, triggered {x["type"]} on {x["repo"]["name"]}")




if __name__ == "__main__":
    import sys
    gitGet(str(sys.argv[1]), str(sys.argv[2]))
#making it usable for testing