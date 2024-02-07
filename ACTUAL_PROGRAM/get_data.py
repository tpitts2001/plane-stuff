import variables
from ACTUAL_PROGRAM.DATA_GATHERING import historical_flight_data as hfd

###########################################################################
#main methods

def get_historical_flight_data():
    hfd.download_and_format_historical_flight_data()
    return

###########################################################################
#test methods

def get_historical_flight_data_test():
    hfd.test_method()
    return