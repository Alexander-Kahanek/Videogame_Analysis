import pandas as pd

raw = pd.read_csv('vgsales.csv')
# print(raw.head())
years = raw.groupby(['Year']).agg({'NA_Sales': 'sum', 'EU_Sales': 'sum',
                                   'JP_Sales': 'sum', 'Other_Sales': 'sum', 'Global_Sales': 'sum'}).reset_index()

plats = raw.groupby(['Year', 'Platform']).agg({'NA_Sales': 'sum', 'EU_Sales': 'sum',
                                               'JP_Sales': 'sum', 'Other_Sales': 'sum', 'Global_Sales': 'sum'}).reset_index()

# print(pub.head())

top_plats = []

for year, df in plats.groupby(['Year']):
    df.index = df['Platform']
    # NA = df.iloc[df['NA_Sales'].idxmax()]['Platform']
    NA, JP, EU, O, G = df[['NA_Sales', 'JP_Sales',
                           'EU_Sales', 'Other_Sales', 'Global_Sales']].idxmax()
    # print(year, NA, JP, EU, O,  G)
    top_plats.append({
        "Year": year,
        "NA": NA,
        "JP": JP,
        "EU": EU,
        "Other": O,
        "Global": G
    })

plats = pd.DataFrame(top_plats)
comb = years.merge(plats, on='Year', how='right')

print(comb.head())
# print(years.head(), '\n', plats.head())

comb.to_csv('year.sales.platforms.csv', index=False)

# print(comb['NA'].unique())
# print(comb['JP'].unique())
# print(comb['EU'].unique())
# print(comb['Other'].unique())
# print(comb['Global'].unique())
# print(raw['Platform'].unique())
