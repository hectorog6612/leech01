import os

API_ID = API_ID = 26344154

API_HASH = os.environ.get("API_HASH", "d501ddb111d2a4edd76bc33ffc2c8d39")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7046531161:AAEqRq6enen9AYn93lPe7sCpjq8162Rw54s")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 803626605))

LOG = -1002122751557

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-4142006950').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "803626605").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


