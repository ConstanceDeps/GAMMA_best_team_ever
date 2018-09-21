import pandas as pd
import os

df = pd.read_excel(os.path.join('C:\\Users', 'IONIZATION_case_daily_production_data.xlsx'), 'Production')

df['galvanized_production'] = df['galvanized_1_production']+df['galvanized_2_production']+df['galvanized_3_production']

df_grouped = df.groupby(['year', 'month']).sum()

asset1 = df_grouped['slab_production'][18:24].mean()
asset2 = df_grouped['pickled_production'][18:24].mean()
asset3 = df_grouped['galvanized_production'][18:24].mean()

print('MONTHLY VOLUMES\nSlab production: {:.1f} \nPickled production: {:.1f} \nGalvanized production: {:.1f}.'.format(asset1, asset2, asset3))