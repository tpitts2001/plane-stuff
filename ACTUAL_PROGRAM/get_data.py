import variables
from ACTUAL_PROGRAM.DATA_GATHERING import historical_flight_data as hfd

###########################################################################
#main methods

def get_historical_flight_data():
    hfd.download_and_format_historical_flight_data()
    return

def get_historical_flight_data_int():
    hfd.download_and_format_historical_flight_data_int()
    return

def filter_and_combine_historical_flight_data():
    hfd.filter_and_combine()
    return

###########################################################################
#test methods

def get_historical_flight_data_test():
    hfd.test_method()
    return