import json

with open("/Users/User/OneDrive - АО Казахстанско-Британский Технический Университет/Документы/GitHub/pp2/lab4/json/sample.json", encoding="utf-8") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<7}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")

    print(f"DN: {dn}, Description: {description}, Speed: {speed}, MTU: {mtu}")

    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<7}")