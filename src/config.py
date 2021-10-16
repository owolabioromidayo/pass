import dotenv, os

class ConfigService:
    def __init__(self):
        dotenv.load_dotenv()
        print(os.getenv('MASTER'))

    def get(self, key):
        return os.getenv(key)



print(type(ConfigService().get('sdfsdf')))

