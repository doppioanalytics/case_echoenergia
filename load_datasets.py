import pandas as pd
import os
import glob

# Usar glob para conseguir todos os .csvs na pasta do repo
path = "C:\\Users\\Gustavo\\Desktop\\case_echoenergia\\datasets"
csv_files = glob.glob(os.path.join(path, "*.csv"))

# Inserir todos os dfs em uma lista
df = [pd.read_csv(f) for f in csv_files]

# Concatenar todos os dataframes em um consolidado
df_consolidado = pd.concat(df)

# Transformar df em .parquet
df_consolidado.to_parquet('df_consolidado.parquet', engine='pyarrow')

df_parquet = pd.read_parquet('df_consolidado.parquet')

print(df_parquet.head())



