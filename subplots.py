import matplotlib
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime

df = pd.read_csv('data.csv')

matplotlib.rcParams['font.family'] = 'Arial'


def create_plot(plt,k):
    parties = set(df['Party'])
    party_colors = {
        'Democratic': 'blue',
        'Republican': 'red',
        'Democratic-Republican': 'green',
        'Whig': 'orange',
        'Other': 'purple'
    }

    # Create empty lists to store line objects for legend
    legend_elements = []
    for party in party_colors:
        color = party_colors.get(party, '')
        line = matplotlib.lines.Line2D([0], [0], color=color, label=party)
        legend_elements.append(line)

    # Before the plotting loop, create lists to store all dates and scores
    all_dates = []
    all_scores = []

    for i in range(len(df)):
        start_date = datetime.strptime(df.iloc[i, 2], '%m/%d/%Y')
        end_date = datetime.strptime(df.iloc[i, 3], '%m/%d/%Y')
        score = df.iloc[i, k]
        
        # Add dates and scores to our lists
        all_dates.extend([start_date, end_date])
        all_scores.extend([score, score])

        # Use party_colors dictionary to get color, defaulting to 'purple' for unknown parties
        color = party_colors.get(df.iloc[i, 4], 'purple')

        # print(start_date, end_date, df.iloc[i, 1])
        plt.plot(
            [start_date, end_date], 
            [score, score], 
            '-', 
            color=color,
        )
        initials = ''.join(word[0] for word in df.iloc[i, 1].split())
        plt.annotate(
        initials,  # The label text
        (start_date, score),  # The data point to annotate
        textcoords="offset points",  # Offset the text
        xytext=(5, 5),  # Position the text 10 points above the data point
        ha="center",  # Horizontal alignment
        )

    # Add dotted trend line
    plt.plot(all_dates, all_scores, ':', color='gray', alpha=0.5, label='Trend')

    plt.grid(axis='x', color='0.95')
    # plt.legend(handles=legend_elements, title='Party')
    plt.set_title(df.columns[k] + ' Performance by Presidential Term')
    plt.set_ylim(0, 100)
    plt.set_xlim(datetime(1776, 7, 4), datetime(2025, 1, 20))
    plt.set_ylabel((df.columns[k]) + ' Score')
    plt.set_xlabel('Date')


fig, axes = plot.subplots(2, 2, figsize=(10, 8))

k = 14
for i in range(2):
    for j in range(2):
        create_plot(axes[i, j], k)
        k += 1

plot.show()
