import variables
import os
import re
from collections import defaultdict
import glob
from ACTUAL_PROGRAM.DATA_GATHERING import historical_flight_data as hfd

historical_flight_data_downloaded_file_path_os_path = os.path.realpath('../'+variables.historical_flight_data_downloaded_file_path)



hfd.move_first_10_chars_to_back(historical_flight_data_downloaded_file_path_os_path)


