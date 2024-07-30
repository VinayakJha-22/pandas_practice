import pandas as pd
from datetime import datetime


class Dataframe:

    def dateModify(self, value):
        return datetime.strptime(value, '%d-%m-%Y').date()


if __name__ == "__main__":
    # learning series
    data_row = {
        "name": "Vinayak",
        "age": 25,
        "gender": "Male",
        "salary": 100000
    }
    ser = pd.Series(data_row)

    # learning dataframe
    data_dict = {
        "name": ["Vinayak", "Shreya", "Ruchika", "Pandey"],
        "age": [25, 25, 26, 26],
        "gender": ['M', 'F', 'F', 'M'],
        "salary": [85000, 55000, 50000, 80000]
    }
    df = pd.DataFrame(data_dict)
    df1 = df
    # aggregation operation
    df = pd.concat([df, df1.agg({'age': ['mean'], 'salary': ['mean']})])
    df = pd.concat([df, df1.agg({'salary': ['sum']})])
    df = pd.concat([df, df1.agg({'salary': ['max']})])

    # filtration operation
    flag = []
    for i, row in df.iterrows():
        if row['gender'] == 'M':
            flag.append(True)
        else:
            flag.append(False)
    df['male_resource'] = pd.Series(flag)

    # change nan value to other value
    df = df.fillna(0)

    # changing datatype of a column
    df['age'] = df['age'].astype(int)
    df['salary'] = df['salary'].astype(int)

    # reading data from CSV
    raw_data = pd.read_csv('./election_data.csv', encoding='cp1252')
    print(raw_data.columns)
    Obj = Dataframe()
    raw_data['Date'] = raw_data['Date'].apply(Obj.dateModify)

    # reading data in chunks
    i = 0
    for chunk in pd.read_csv('./election_data.csv', chunksize=10, encoding='cp1252'):
        print(i)
        print(chunk)
        print('')
        i += 1
    print(df)





