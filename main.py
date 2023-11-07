import pandas as pd
import numpy as np
from d3blocks import D3Blocks

# source: https://stackoverflow.com/questions/65030626/creating-chord-diagram-in-python/74404594#74404594
# https://pypi.org/project/d3blocks/

source = ['Nadal', 'Nadal', 'Nadal', 'Nadal',
        'Djokovic', 'Djokovic', 'Djokovic', 'Djokovic',
        'Federer', 'Federer', 'Federer', 'Federer',
        'Murray', 'Murray', 'Murray', 'Murray',
        'Alcaraz', 'Alcaraz', 'Alcaraz', 'Alcaraz']

target = ['Djokovic', 'Federer', 'Murray', 'Alcaraz',
        'Nadal', 'Federer', 'Murray', 'Alcaraz',
        'Djokovic', 'Nadal ', 'Murray', 'Alcaraz',
        'Djokovic', 'Nadal', 'Federer', 'Alcaraz',
        'Djokovic', 'Federer', 'Murray', 'Nadal']

weights = [59, 40, 24, 3,
         59, 50, 36, 4,
         50, 40, 25, 0,
         36, 24, 25, 2,
         4, 0, 2, 3]

df = pd.DataFrame(data=np.c_[source, target, weights], columns=['source','target','weight'])

# Initialize
d3 = D3Blocks(frame=False)
d3.chord(df, color='source', opacity='source', cmap='Set2')

# Edit any of the properties you want in the dataframe:
#d3.node_properties
#d3.node_properties.get('NL')['color'] = '#000000'
# {'US': {'id': 0, 'label': 'US', 'color': '#1f77b4', 'opacity': 0.8},
#  'UK': {'id': 1, 'label': 'UK', 'color': '#98df8a', 'opacity': 0.8},
#  'FR': {'id': 2, 'label': 'FR', 'color': '#8c564b', 'opacity': 0.8},
#  'NL': {'id': 3, 'label': 'NL', 'color': '#000000', 'opacity': 0.8},
#  'IT': {'id': 4, 'label': 'IT', 'color': '#9edae5', 'opacity': 0.8}}

# Plot again
#d3.show()
