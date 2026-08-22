import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#It reads the csv file "medical_examination"
df = pd.read_csv('medical_examination.csv')

#It calculates the ratio of weight per height divided by 100, and finally raisedd in the second power
bmi = df['weight']/((df['height']/ 100)**2)
#We create a new column including only the values over 25 bmi and saves all the values as integers
df['overweight'] = (bmi>25).astype(int)

#If cholesterol is over 1 it returns True and replaces the cholysterol value with 1. Otherwise it replaces the cholysterol value with 0
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
#If gluc is over 1 it returns True and replaces the gluc value with 1. Otherwise it replaces the gluc value with 0
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    #It reshapes the dataframe. Before that we had 1 row per patient. Now we are having 6 rows per patient
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    #
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7
    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )



    # 8
    fig = g.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        vmin=-0.16,
        vmax=0.32,
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )



    # 16
    fig.savefig('heatmap.png')
    return fig
