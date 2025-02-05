#my get module for the project
import os
import json


def gitGet(argument, password):
    print(f"Fetching the event logs for {argument}...")
    
    #the api call, I still have to filter the events
    try:
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




if __name__ == "__main__":
    import sys
    gitGet(str(sys.argv[1]), str(sys.argv[2]))
#making it usable for testing