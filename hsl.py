import gtfs_kit as gk
from google.transit import gtfs_realtime_pb2
import requests

def getNextBusses():
    #feed = gk.read_feed("https://realtime.hsl.fi/realtime/trip-updates/v2/hsl", dist_units="km")

    resp = requests.get("https://realtime.hsl.fi/realtime/trip-updates/v2/hsl")

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(resp.content)

    from datetime import datetime, timezone,timedelta

    # parse current unix timestamp
    now_sec = int(datetime.now(timezone.utc).timestamp())

    upcoming = []

    for entity in feed.entity:
        if entity.HasField("trip_update"):
            tu = entity.trip_update
            for stu in tu.stop_time_update:
                
                if stu.stop_id == "1465101":  # your stop
                    # predicted departure time
                
                    if stu.departure and stu.departure.time:
                        depart = stu.departure.time

                        if 0 <= depart - now_sec <= 15 * 60:
                            upcoming.append((tu, stu))
    times = []
    for tu, stu in upcoming:
        # static trip info
        if tu.trip.route_id and (tu.trip.route_id == '1030') and stu.stop_id=='1465101':

            thisTime = datetime.fromtimestamp(stu.arrival.time, tz=timezone.utc) + timedelta(hours=2)
            times.append (thisTime.strftime("%H:%M"))

    times.reverse()
    return times