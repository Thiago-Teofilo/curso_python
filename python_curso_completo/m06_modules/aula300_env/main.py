import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('USER_NAME'))
print(os.getenv('USER_EMAIL'))
print(os.getenv('USER_PASSWORD'))