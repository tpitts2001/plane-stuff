import pandas as pd

# Data from the table
data = {
    "Field Number": [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
        "31", "32"
    ],
    "Field Name": [
        "Date of Data: Year", "Date of Data: Month", "Origin Airport: Alpha Code",
        "Origin Airport: Unique Numeric Code", "Origin Airport: World Area Code",
        "Origin Airport: City Name", "Destination Airport: Alpha Code",
        "Destination Airport: Numeric Code", "Destination Airport: World Area Code",
        "Destination Airport: City Name", "Carrier: Alpha Code", "Carrier: Entity Code",
        "Official OAI Group Code", "Distance", "Service Class", "Aircraft Type: Group",
        "Aircraft Type: Type", "Aircraft Type: Configuration", "Departures Performed",
        "Departures Scheduled", "Available Capacity: Payload Pounds",
        "Available Seats", "Middle Cabin (No Longer Reported)",
        "Coach Cabin (No Longer Reported)", "Passengers Transported",
        "Middle Cabin (No Longer Reported)", "Coach Cabin (No Longer Reported)",
        "Freight Transported", "Mail Transported", "Ramp – Ramp in minutes",
        "Airborne – in minutes", "Carrier’s World Area Code"
    ],
    "Field Length": [
        "4", "2", "3", "5", "3", "35", "3", "5", "3", "35",
        "3", "5", "1", "5", "1", "1", "3", "1", "5", "5",
        "10", "7", "0", "0", "7", "0", "0", "10", "10", "10",
        "10", "3"
    ],
    "Data Type": [
        "NUMERIC", "NUMERIC", "CHARACTER", "NUMERIC", "NUMERIC", "CHARACTER",
        "CHARACTER", "NUMERIC", "NUMERIC", "CHARACTER", "CHARACTER", "CHARACTER",
        "NUMERIC", "NUMERIC", "CHARACTER", "NUMERIC", "NUMERIC", "NUMERIC",
        "NUMERIC", "NUMERIC", "NUMERIC", "NUMERIC", "NUMERIC", "NUMERIC",
        "NUMERIC", "NUMERIC", "NUMERIC", "NUMERIC", "NUMERIC", "NUMERIC",
        "NUMERIC", "NUMERIC"
    ],
    "Description": [
        "Century & Year (e.g., 1999)", "Month of the year (01-12)",
        "Airport Code exists in the Airports support file",
        "Airports Support table", "WAC Support table data that is linked","airport support table","airport code, exists in airports support file","airports support code","wac support table data that is linked with airports","airports support table","this code matches up with whats in cardecodes for the carrier",
        "Carriers report their T100 using their unique CarDecode Entity Code(s) A carrier can have more than one of these.",
        "1 = Large Regional Carrier - $20 million to $100 million in revenue"
        "2 = National Carrier - $100 million to $1 billion in revenue"
        "3 = Major Carrier - Over $1 billion in revenue"
        "4 = Medium Regional Carrier - Under $20 million in revenue"
        "5 = Small Certificated Carrier"
        "6 = Commuter Carrier"
        "7 = Foreign Carrier"
        "8 = All Cargo Carrier - Domestic Only"
        "9 = Essential Air Service - Air Taxi"
        "See Note G below.",
        "The great circle distance in statute miles between the Origin and Destination airports.",
        "null",
        "This code indicates the general category of aircraft type reported. See Note J below",
        "This code indicates the specific make and model of the aircraft. The Field Length was previously 2 in the Aircraft Types Support table. It was changed to be 3. See Note J below",
        "Cabin Configuration Codes (See Note J below):"
        "• 1 = Passenger"
        "• 2 = Cargo"
        "• 3 = Combination Passenger/Cargo on maindeck"
        "• 4 = Float/Amphibious Passenger/Cargo",
        "null","null","null",
        "Previously named First Cabin - Since 2002, Carriers only report total available seats ",
        "null","null",
        "Previously named First Cabin - Since 2002, Carriers only report total passengers transported",
        "null", "null", "null","null",
        "Elapsed Time in Minutes",
        "Elapsed Time in Minutes",
        "See Note P below."
    ]
}
# Creating a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'flight_data/legend-tabl-int-seg.csv'
df.to_csv(csv_file_path, index=False)

csv_file_path