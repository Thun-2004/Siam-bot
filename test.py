import os
from service.database import getData
location = getData()


print(os.getenv("DB_URI"))