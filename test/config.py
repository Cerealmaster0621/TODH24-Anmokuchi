import os
from dotenv import load_dotenv
load_dotenv()

MONGODBPW = os.getenv("MONGODBPW")
MONGODBUN = os.getenv("MONGODBUN")