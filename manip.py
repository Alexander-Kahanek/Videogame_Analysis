import pandas as pd

raw = pd.read_csv('vgsales.csv')

years = raw.groupby(['Year']).agg({'NA_Sales': 'sum', 'EU_Sales': 'sum',
                                   'JP_Sales': 'sum', 'Other_Sales': 'sum', 'Global_Sales': 'sum'}).reset_index()

plats = raw.groupby(['Year', 'Platform']).agg({'NA_Sales': 'sum', 'EU_Sales': 'sum',
                                               'JP_Sales': 'sum', 'Other_Sales': 'sum', 'Global_Sales': 'sum'}).reset_index()

top_plats = []

for year, df in plats.groupby(['Year']):
    df.index = df['Platform']

    NA, JP, EU, O, G = df[['NA_Sales', 'JP_Sales',
                           'EU_Sales', 'Other_Sales', 'Global_Sales']].idxmax()

    top_plats.append({
        "Year": year,
        "NA": NA,
        "JP": JP,
        "EU": EU,
        "Other": O,
        "Global": G
    })

plats = pd.DataFrame(top_plats)
combined = years.merge(plats, on='Year', how='right')

print('dataframes found and combined, printing head and saving new csv.')
print(combined.head())

combined.to_csv('year.sales.platforms.csv', index=False)
