import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime

df = pd.read_csv('data.csv')

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

for i in range(len(df)):
    start_date = datetime.strptime(df.iloc[i, 2], '%m/%d/%Y')
    end_date = datetime.strptime(df.iloc[i, 3], '%m/%d/%Y')

    # Use party_colors dictionary to get color, defaulting to 'purple' for unknown parties
    color = party_colors.get(df.iloc[i, 4], 'purple')

    print(start_date, end_date, df.iloc[i, 1])
    plt.plot(
        [start_date, end_date], 
        [df.iloc[i, 5], df.iloc[i, 5]], 
        '-', 
        color=color,
    )
    initials = ' '.join(word[0] for word in df.iloc[i, 1].split())
    plt.annotate(
    initials,  # The label text
    (start_date, df.iloc[i, 5]),  # The data point to annotate
    textcoords="offset points",  # Offset the text
    xytext=(0, 5),  # Position the text 10 points above the data point
    ha="center",  # Horizontal alignment
    )

plt.grid(axis='x', color='0.95')
plt.legend(handles=legend_elements, title='Party')
plt.title('Presidential Performance')
plt.ylim(0, 1000)
plt.xlim(datetime(1789, 4, 30), datetime(2024, 1, 20))
plt.ylabel('Presidential Performance by Presidential Term')
plt.show()
