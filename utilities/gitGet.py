#my get module for the project
import os


def gitGet(argument, password):
    print(argument)
    
    #the api call, I still have to filter the events
    os.system(f"""
    curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer {password}" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/users/{argument}/events
    """)



if __name__ == "__main__":
    import sys
    gitGet(str(sys.argv[1]), str(sys.argv[2]))
#making it usable for testing