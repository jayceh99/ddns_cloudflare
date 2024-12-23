import json
import requests
import socket


def get_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    print(s.getsockname()[0])
    s.close()
    return str(ip_address)


def set_ip(current_ip: str) -> None:
    """
    sets the ip in via cloudflare api
    """

    zone_id = "47a57834d9050c00c383ec74f72e9bb7"
    record_id = "557c214b1e7dc6dad84a033f4799b510"
    print(zone_id)
    url = (
        "https://api.cloudflare.com/client/v4/zones/%(zone_id)s/dns_records/%(record_id)s"
        % {"zone_id": zone_id, "record_id": record_id}
    )

    api_key = "tiH0FbjpD-5h9AfNsKopRQ-Y8dQYOBm2YdQRVlOE"
    record_name = "jayce-h.cc"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {"type": "A", "name": record_name, "content": current_ip}
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        print(f"Error retrieving DNS record.")
        print(f"url={url}")
        print(f"headers={headers}")
        print(f"payload={payload}")
        print(f"response.status_code={response.status_code}")
        print(json.dumps(json.loads(response.content), indent = 2))
        exit(1)


def main():
    current_ip = get_ip()
    my_profile = open("/opt/my_profile.json", "r")
    my_profile_json = json.load(my_profile)
    my_profile.close()
    api_key = my_profile_json["api_key"]
    domain_name = my_profile_json["record_name"]
    zone_id = my_profile_json["zone_id"] 
    record_id = my_profile_json["record_id"] 
    set_ip(current_ip , api_key , domain_name , zone_id, record_id)


if __name__ == "__main__":
    main()