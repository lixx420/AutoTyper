import asyncio, time
import requests as r

"""
FILL THIS VARIABLES HERE
"""
token = "YOUR TOKEN HERE"
channel_id = "CHANNEL ID"



"""
DON'T EDIT ANYTHING HERE
"""
base_url = "https://discord.com/api/v9"
url = f"{base_url}/channels/{channel_id}/typing"
headers = {
    "authorization": token
}

async def main():
    print("Logging in...")
    res = r.get(f"{base_url}/users/@me", headers=headers)
    if res.status_code == 200:
        json = res.json()
        print(f"Logged in as {json['username']}#{json['discriminator']}")
        print(f"ID: {json['id']}\n")
    else:
        print(f"Failed to login. Code: {res.status_code}")
        print("Please check your token and try again.")
        exit(0)
    fail = 0
    type_count = 0
    while True:
        start = time.monotonic()
        try: res = r.post(url, headers=headers)
        except:
            fail += 1
            if fail >= 4:
                break
            print(f"Typing Failed. Retrying... {fail}/3")
        else:
            if res.status_code == 204:
                type_count += 1
                print(f"[{type_count}] Typing done! Elapsed: {int(round((time.monotonic() - start) * 1000))}ms Code: {res.status_code}")
            elif res.status_code == 401:
                print(f"{res.status_code} Unauthorized\nPlease check your token to continue.")
                break
            elif res.status_code == 400:
                print(f"{res.status_code} Bad Request\nPlease make sure that you put the correct channel id and try again.")
                break
            else:
                print("Typing Failed.")
                print(f"Code: {res.status_code}")
                break
        await asyncio.sleep(7)
        continue
    print("\n[Program Finished]")
    exit(0)

def run():
    try:
        print("Typing Bot v0.3 is starting...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[Process Killed]")
        exit(0)
    except Exception as error:
        print(f"\n[An Error Occured]:\n{error}")
        exit(0)

run()
