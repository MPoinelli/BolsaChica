import datetime
import pandas as pd
import cartopy

# Getting the current date and time of today and yesterday (defined as 24 hours ago)
today = datetime.datetime.utcnow().replace(microsecond=0, second=0, minute=0)
yesterday = datetime.datetime.utcnow().replace(microsecond=0, second=0, minute=0) - datetime.timedelta(days=1)

today_url = today.strftime("%Y-%m-%dT%H:%M:%S").replace(':','%3A')
yesterday_url = yesterday.strftime("%Y-%m-%dT%H:%M:%S").replace(':','%3A')

print(today_url)
print(yesterday_url)

# Create URL
URL_erdapp = "http://erddap.cdip.ucsd.edu/erddap/tabledap/"
URL_parameters = "wave_agg.csv?station_id%2Ctime%2CwaveHs%2CwaveTp%2CwaveTa%2CwaveDp&"
URL_stationID = "station_id=%22028%22&"
URL_time = "time%3E2022-04-10T00%3A00%3A00Z&time%3C2022-04-11T%3A00%3A00%3A00Z&"
URL_order = "waveFlagPrimary=1&orderByMax(%22time%2Cstation_id%22)"

URL = URL_erdapp + URL_parameters + URL_stationID + URL_time + URL_order
df = pd.read_csv(URL)


