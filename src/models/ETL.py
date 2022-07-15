from fileinput import filename
import pandas as pd

class ETL(filename: str):
    
    def load_csv() -> pd.DataFrame:
        df=pd.read_csv()
        return df

    def process(dataframe) -> pd.DataFrame:
        df=process(dataframe)
        return df

    def __init__(self) -> None:
        self.filename=filename
        pass


    