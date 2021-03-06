import shodan
import os

class ShodanSearchClient:
    
    API_KEY = None

    def  __init__(self, api_key):
        self.API_KEY = api_key
    
    def __assert_api_key(self):
        if not self.API_KEY or len(self.API_KEY) == 0:
            raise ValueError('Shodan API key is invalid')
        else:
            self.API_KEY = self.API_KEY.lstrip()
            self.API_KEY = self.API_KEY.replace('\n', '')

    def display_device_info(self, device_info):
        print('DEVICE INFORMATION')
        print('Ip address: {}'.format(device_info['ip_str']))
        print('Country: {}'.format(device_info['country_name']))
        print('City: {}'.format(device_info['city']))
        print('Isp: {}'.format(device_info['isp']))
        print('Latitude: {}'.format(device_info['latitude']))
        print('Longitude: {}'.format(device_info['longitude']))
        print('Ports: {}'.format(device_info['ports']))
        print('Postal code: {}'.format(device_info['postal_code']))
        print('Org: {}'.format(device_info['org']))
        print('Hostnames: {}'.format(device_info['hostnames']))
        print('Asn: {}'.format(device_info['asn']))
        data = device_info['data']
        data = data[0]
        print('Device type: {}'.format(data['devicetype']))
        print(data['data'])

    def search_host(self, host_ip):
        self.__assert_api_key()
        try:
            api = shodan.Shodan(self.API_KEY)
            results = api.host(host_ip)
            self.display_device_info(results)
        except shodan.APIError as error:
            raise BaseException(error)
    
    def scan_go_ahead_devices(self):
        self.__assert_api_key()        
        print('Scanning, please wait')
        command = 'entropy -b 2 -v --shodan {}'.format(self.API_KEY)
        result = os.popen(command).read()
        print(result)
