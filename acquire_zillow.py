import pandas as pd
import env
import os

def get_connection(db, username=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'


def get_new_zillow_data():
    
    sql = '''
    select 
    bedroomcnt as bedroom,bathroomcnt as bathroom, calculatedfinishedsquarefeet as square_ft,yearbuilt, fips,
    taxvaluedollarcnt as house_value, taxamount as tax
    FROM zillow.properties_2017
    left join zillow.predictions_2017 using (parcelid)
    WHERE propertylandusetypeid = 261 and transactiondate like "2017%%"
    '''
    
    return pd.read_sql(sql, get_connection('zillow'))