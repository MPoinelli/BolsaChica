import datetime
import csv
import pandas as pd

from io import StringIO
import csv
import requests

# Getting the current date
# and time
dt = datetime.datetime.now(datetime.timezone.utc)

# Create URL
URL_erdapp      = "http://erddap.cdip.ucsd.edu/erddap/tabledap/"
URL_parameters  = "wave_agg.csv?station_id%2Ctime%2CwaveHs%2CwaveTp%2CwaveTa%2CwaveDp&"
URL_constraints = "station_id=%22028%22&time%3E2022-04-10T00%3A00%3A00Z&time%3C2022-04-11T%3A00%3A00%3A00Z&"
URL_order       = "waveFlagPrimary=1&orderByMax(%22time%2Cstation_id%22)"

URL = URL_erdapp + URL_parameters + URL_constraints + URL_order

# Download file and convert to dataframe
with requests.Session() as s:
    
    download = s.get(URL)
    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    df = pd.DataFrame(cr)