import sys
from file_reader import FileReader
from shodan_search_client import ShodanSearchClient
from exploit_client import ExploitClient

SHODAN_API_KEY_PATH = 'api_key_shodan.txt'

# Flags
SCAN_FLAG = '--scan'
IP_FLAG = '-i'
PORT_FLAG = '-p'

def __print_help():
    print('usage: python3 main.py <options>\n')
    print('options:')
    print('-h\tShows this help message and exit')
    print('-i <ip_address>\tTarget IP')
    print('-p <port>\tTarget port to attack')
    print('--scan\tScans ip addresses with shodan, this option needs shodan API key into file api_key_shodan.txt')

def __assert_args():
    if len(sys.argv) < 2:
        __print_help()
        raise BaseException('')
    if SCAN_FLAG in sys.argv:
        if len(sys.argv) > 2:
            raise BaseException("Error: execute '--scan' option without another flag")
    complete_params = len(sys.argv) is 5
    complete_flags = IP_FLAG in sys.argv and PORT_FLAG in sys.argv
    if complete_params and complete_flags:
        index_ip_flag = sys.argv.index(IP_FLAG)
        index_port_flag = sys.argv.index(PORT_FLAG)
        params_offset = index_ip_flag - index_port_flag
        flag_is_first_param = index_ip_flag is 1 or index_port_flag is 1
        if flag_is_first_param and params_offset is 1 or params_offset is -1:
            __print_help()
            raise BaseException('Bad usage')
    else:
        __print_help()
        raise BaseException('Bad usage')    

def __execute_exploit():
    ip = sys.argv[2] if IP_FLAG in sys.argv[1] else sys.argv[4]
    port = sys.argv[2] if PORT_FLAG in sys.argv[1] else sys.argv[4]
    password_disclosure = ExploitClient(ip, port)
    password_disclosure.exploit()
    print('Please wait')
    shodan_search.search_host(ip)


if __name__ == '__main__':
    print('Running...')
    try:
        __assert_args()
        file_reader = FileReader(SHODAN_API_KEY_PATH)
        api_key = file_reader.read_first_line()
        shodan_search = ShodanSearchClient(api_key)
        if SCAN_FLAG in sys.argv:
            pass
        else:
            __execute_exploit()
        sys.exit(0)
    except BaseException as error:
        print(str(error))
        sys.exit(1)