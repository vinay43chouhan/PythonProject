import os
import json


class SchemaMappingManager:
    _instance = None
    _is_init_done = False
    _schema_dir = 'files'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SchemaMappingManager, cls).__new__(cls)
        return cls._instance

    def init(self):
        if SchemaMappingManager._is_init_done:
            return
        # Initialize your singleton instance here if needed
        # f = open('schema.json', "r")
        # data = json.loads(f.read())
        if os.path.exists(SchemaMappingManager._schema_dir) and os.path.isdir(SchemaMappingManager._schema_dir):
            for filename in os.listdir(SchemaMappingManager._schema_dir):
                if filename.endswith(".json"):
                    full_path = os.path.join(SchemaMappingManager._schema_dir, filename)
                    with open(full_path, "r") as file:
                        data = json.load(file)
                        self.store_data(data)

    def store_data(self, data):
        try:
            # Try to access the key 'name' in the dictionary
            value = data["compatible_devices"]
            print(f"The value of 'name' is: {value}")
            for item in value:
                device_class = ""
                device_class = device_class + item["OUI"]
                device_class = device_class + item["product_code"]
                device_class = device_class + item["firmware_version"]
                self.schemaDB[device_class] = data["device_schema_mapping"]
        except KeyError:
            # If the key doesn't exist, handle the KeyError here
            print("The key 'compatible_devices' does not exist in the dictionary.")

    def __init__(self):
        self.schemaDB = {}

        self.init()

    def get_schema_mapping(self, device_class):
        try:
            dc = self.schemaDB[device_class]
            return self.schemaDB[device_class]
        except KeyError:
            print(device_class," does not exist.")


if __name__ == '__main__':
    obj = SchemaMappingManager()
    cr_value = obj.get_schema_mapping("B4EEB4HB5GGW1.1.7-D")
    print(cr_value)

    inp = {
        "uid": "gwc1e2e30fc4034889a131cf68cbc28b7d",
        "lan_ip": "172.30.55.1",
        "WLAN_SSID_2G": "xu_wifi_8b7d",
        "WLAN_SSID_5G": "xu_wifi_8b7d",
        "WLAN_channel_2G": "3",
        "WLAN_channel_5G": "auto",
        "WLAN_password_2G": "mmqzohm2",
        "WLAN_password_5G": "mmqzohm2",
        "WLAN_security_2G": "psk2",
        "WLAN_security_5G": "psk2",
        "GUEST_password_2G": "mmqzohm2",
        "GUEST_password_5G": "mmqzohm2",
        "GUEST_security_2G": "none",
        "GUEST_security_5G": "none",
        "local_admin_password": "admin",
        "local_admin_username": "admin"
    }
    out = {}
    for i in inp.keys():
        for k in cr_value.keys():
            if i == k:
                out[i] = cr_value[k]

    print(out)
