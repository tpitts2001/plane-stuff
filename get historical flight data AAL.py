from traffic.data import opensky
from datetime import datetime, timedelta

flight = opensky.history(
    "2017-02-05 15:45",
    stop="2017-02-05 16:45",
    callsign="EZY158T",
    # returns a Flight instead of a Traffic
    return_flight=True
)
flight