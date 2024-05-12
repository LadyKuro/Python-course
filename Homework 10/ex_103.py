import pandas as pd

data = {
    'Name': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'],
    'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'],
    'Weight': [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.01, 14.01, 16.00, 18.99, 20.18]
}

df = pd.DataFrame(data, index=range(1, 11))
print(df)
