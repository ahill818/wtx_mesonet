import pandas as pd
import datetime as dt


import pandas as pd
import datetime as dt

class SNFile(object):
    ''' For reading in a raw sticknet data file and correctly 
    parsing the date and time 
    '''
    def __init__(self, filename):
        self.year = int('20'+filename[-8:-6])
        self.filename = filename

    def parse(self, day, hrmin):
        # Converting from Julian Day with CST to standard datetime and UTC
        return (dt.datetime(self.year, 1, 1, int(hrmin)/100, int(hrmin)%100) 
              + dt.timedelta(int(day)-1) + dt.timedelta(hours=6))

    def read(self):
        meso2 = pd.read_csv(self.filename, sep=',', parse_dates=[[1,2]], 
            date_parser=self.parse, header=None)
        return meso2