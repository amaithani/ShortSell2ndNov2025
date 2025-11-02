import pandas as pd
from dhanhq import dhanhq

def get_instrument_df():
    """
    Downloads the instrument list from Dhan and returns it as a Pandas DataFrame.
    """
    try:
        df = pd.read_csv("https://images.dhan.co/api-data/api-scrip-master.csv")
        return df
    except Exception as e:
        print(f"Error downloading instrument list: {e}")
        return None

def get_security_id(instrument_df, symbol, exchange_segment="NSE_EQ"):
    """
    Gets the security ID for a given symbol from the instrument DataFrame.
    """
    if instrument_df is None:
        return None
    try:
        security_id = instrument_df[
            (instrument_df['SEM_TRADING_SYMBOL'] == symbol) &
            (instrument_df['SEM_EXCH_ID'] == exchange_segment)
        ]['SEM_SMST_SECURITY_ID'].iloc[0]
        return str(security_id)
    except IndexError:
        return None

def fetch_historical_daily(dhan_client, security_id, exchange_segment, from_date, to_date):
    """
    Fetches daily historical data from the Dhan API.
    """
    return dhan_client.historical_daily_data(
        security_id=security_id,
        exchange_segment=exchange_segment,
        instrument_type='EQUITY',
        expiry_code=0,
        from_date=from_date,
        to_date=to_date
    )

def fetch_historical_intraday(dhan_client, security_id, exchange_segment, from_date, to_date, interval="5"):
    """
    Fetches intraday historical data from the Dhan API.
    """
    return dhan_client.intraday_daily_minute_charts(
        security_id=security_id,
        exchange_segment=exchange_segment,
        instrument_type='EQUITY',
        expiry_code=0,
        from_date=from_date,
        to_date=to_date
    )
