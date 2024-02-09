from ACTUAL_PROGRAM import get_data as gd
from ACTUAL_PROGRAM import model as md
import variables

###########################################################################
run_data_gathering_process = 'n'
###########################################################################


if run_data_gathering_process == 'y':
    gd.get_historical_flight_data_int()
    gd.get_historical_flight_data()
    gd.filter_and_combine_historical_flight_data()

elif run_data_gathering_process == 'n':
    md
elif run_data_gathering_process == 't':
    gd.get_historical_flight_data_test()
else:
    print('No process defined in Main.py')