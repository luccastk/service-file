import pandas as pd

class CSVToDataFrame:
    def __init__(self, file):
        self.file = file

    def parse(self) -> pd.DataFrame:
        df = pd.read_csv(self.file, delimiter=',', dtype=str, encoding='utf-8').iloc[:-1]
        df = df.where(pd.notnull(df), None)
        df['validity'] = df['validity'].replace('-', None)
        return df