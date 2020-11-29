import pandas as pd
import glob

'''
NOTES:
- Data available for Counties:
    Alpine, Contra Costa (2016), Del Norte, El Dorado (2010), Kings, Lassen, Los Angeles Basin (2018),
    Merced (1999), Placer, Plumas, Riverside (2015), Sacramento (2015), San Benito (1998), 
    San Joaquin (2016), Shasta (2013), Siskiyou (2019), Solano (2009), Tehama, Tulare (2018),
    Ventura (2014), Yolo (2011)

- For Counties with multiple city names, the most recently dated one (with complete data) is chosen
- Using Avg Max Temp (F) in place of Avg Temp (F)
- No Wind Run (miles) attribute in CIMIS
'''

'''
CIMIS Columns:
0 Month Year
1 Total ETo (in)
2 Total Precip (in)
3 Avg Sol Rad (Ly/day)
4 Avg Vap Pres (mBars)
5 Avg Max Air Temp (F)
6 Avg Min Air Temp (F)
7 Avg Max Rel Hum (%)
8 Avg Min Rel Hum (%)
9 Avg Rel Hum (%)
10 Avg Dew Point (F)
11 Avg Wind Speed (mph)
12 Avg Soil Temp (F)
'''

'''
Saving:
Precip (in)             --> 2
Avg Air Temp (F)        --> 5
Avg Rel Hum (%)         --> 9
Avg Wind Speed (mph)    --> 11
Wind Run (miles) --> not available
'''
counties_list = ['Alpine', 'Calaveras', 'CentralCal', 'CentralCoastValleys', 'Colusa', 'Contra Costa', 
    'Del Norte', 'El Dorado', 'Glenn', 'GreatBasin', 'InlandSoCal', 'Inyo', 'Kings', 'Lake', 'Lassen', 
    'LosAngelesBasin', 'Madera', 'Mariposa', 'Merced', 'Mexico', 'Mono', 'NorthCoastValleys', 'Placer', 
    'Plumas', 'Riverside', 'Sacramento', 'SacramentoValley', 'San Benito', 'San Francisco Bay', 'San Joaquin', 
    'SanFranciscoBay', 'ShastaCascade', 'SierraFoothill', 'SierraFoothillFoothill', 'Siskiyou', 'Solano', 
    'SouthCoastValleys', 'Stanislaus', 'State of Oregon', 'State of SierraFoothillFoothill', 'Tehama', 
    'Tulare', 'Tuolumne', 'Ventura', 'Yolo']

months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

column_headers = ['County', 'Month', 'Year', 'Precip (in)', 'Avg Air Temp (F)', 'Avg Rel Hum (%)', 'Avg Wind Speed (mph)' ]
        
files_list = glob.glob("data/CIMISReports/old/*.txt")
def main():

    for filename in files_list:
        
        end_county_name = filename.index('.')
        county_name = filename[ 22:end_county_name ]
        data = {}
        
        # Initialize columns
        for header in column_headers:
            data[header] = []

        # Read each file
        with open(filename, "r") as infile:
            print("Opening", filename)

            lines = infile.read().splitlines()

            # Collect the necessary data
            count = 0
            
            for line in lines:
                line = line.strip()
                #data['County'].append(county_name)
                if count == 0 and line[0:3] in months_list:
                    data['County'].append(county_name)
                    data['Month'].append(line[0:3])
                    data['Year'].append(line[4:])
                elif count == 2:
                    data['Precip (in)'].append(line)
                elif count == 5:
                    data['Avg Air Temp (F)'].append(line)
                elif count == 9:
                    data['Avg Rel Hum (%)'].append(line)
                elif count == 11:
                    data['Avg Wind Speed (mph)'].append(line)
                elif count == 13:
                    count = 0
                    continue
                    
                count += 1

            # Write this to a dataframe and csv file
            df = pd.DataFrame(data = data)
            df.to_csv("data/CIMISReports/new/" + county_name + '_weather.csv', header=column_headers, index=None, sep=',')

if __name__ == "__main__":
    main()
    print("DONE")