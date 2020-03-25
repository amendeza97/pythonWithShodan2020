import sys
from file_reader import FileReader
from shodan_search_client import ShodanSearchClient

SHODAN_API_KEY_PATH = 'api_key_shodan.txt'

if __name__ == '__main__':
    try:
        file_reader = FileReader(SHODAN_API_KEY_PATH)
        api_key = file_reader.read_first_line()
        shodan_search = ShodanSearchClient(api_key)
        shodan_search.search_host()
    except BaseException as error:
        print(str(error))
        sys.exit(1)