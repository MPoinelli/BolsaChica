import datetime
import csv

from io import StringIO
import csv
import requests

# Getting the current date
# and time
dt = datetime.datetime.now(datetime.timezone.utc)

# Download file
CSV_URL = "http://erddap.cdip.ucsd.edu/erddap/tabledap/wave_agg.csv?station_id%2Ctime%2CwaveHs%2CwaveTp%2CwaveTa%2CwaveDp&station_id=%22028%22&time%3E2022-04-10T00%3A00%3A00Z&time%3C2022-04-11T%3A00%3A00%3A00Z&waveFlagPrimary=1&orderByMax(%22time%2Cstation_id%22)"

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)