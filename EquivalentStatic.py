#BNBC page:3186, pdf page: 604
import sqlite3
import pandas as pd 

con = sqlite3.connect("EquivalentSeismic.db")
cur = con.cursor()
district = "Dhaka"
def get_zone_coefficient(zone):
    res = cur.execute("SELECT coefficients FROM zonecoefficient WHERE zones = :zone", {'zone': zone})
    return res.fetchone()

def building_period(building_height,**coefficient):
    return coefficient["Ct"]*building_height**coefficient["m"]
seismic_parameters = {
    "Zone Coefficient": get_zone_coefficient(district),
    "Response Reduction Factor": 8,
    "Site Coefficient": 1.15,
    "Building Period": 1, #TODO set computation period
    }

def compute_normalized_accel(**kargs):
    if 0<T and T<=TB:
        return S*(1+T/TB(2.5*eta - 1))
    elif TB<T and T<=TC:
        return 2.5*S*eta
    elif TC<T and T<=TD:
        return 2.5*S*eta*(TC/T)
    elif TD<T and T<=TL:
        return 2.5*S*eta*(TC*TD/T**2)

class DesignSpectrum:
    def __init__(self, **kargs):
        self.zone_coefficient = kargs["Zone Coefficient"]
        #self.