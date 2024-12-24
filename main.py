import json
import requests

def get_ip() -> str:
    my_ip = requests.get("https://api.ipify.org").text
    return str(my_ip)


def renew_ddns(token, domain_name, zone_id, record_id, my_ip) -> None:
    url = "https://api.cloudflare.com/client/v4/zones/%s/dns_records/%s" % (zone_id, record_id)
    headers = {
        "Authorization": "Bearer "+ str(token),
        "Content-Type": "application/json",
    }
    payload = {"type": "A", "name": domain_name, "content": my_ip, "proxied": True} #不要proxy就把這裡的True改成False
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        print(url)
        print("status_code = " + str(response.status_code))
        print("content = " + str(response.content))


def main():
    my_profile = open(r"C:\Users\jayce\config2.json", "r") #這裡更改config.json的路徑
    my_profile_json = json.load(my_profile)
    my_profile.close()
    token = my_profile_json["token"]
    domain_name = my_profile_json["domain_name"]
    zone_id = my_profile_json["zone_id"] 
    record_id = my_profile_json["record_id"]
    my_ip = get_ip() 
    renew_ddns(token, domain_name, zone_id, record_id, my_ip)

if __name__ == "__main__":
    main()