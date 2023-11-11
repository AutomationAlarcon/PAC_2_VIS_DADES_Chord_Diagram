import pandas as pd
import numpy as np
from d3blocks import D3Blocks

# source: https://stackoverflow.com/questions/65030626/creating-chord-diagram-in-python/74404594#74404594
# https://pypi.org/project/d3blocks/
# https://d3blocks.github.io/d3blocks/pages/html/d3graph.html

source = ['Novak Djokovic', 'Novak Djokovic', 'Novak Djokovic', 'Novak Djokovic', 'Novak Djokovic',
          'Novak Djokovic', 'Novak Djokovic', 'Novak Djokovic', 'Novak Djokovic', 'Novak Djokovic']

target = ['Rafael Nadal', 'Roger Federer', 'Andy Murray', 'Stan Wawrinka', 'Tomas Berdych',
          'David Ferrer:', 'Juan Martin del Potro', 'Gilles Simon', 'Jo-Wilfried Tsonga', 'Richard Gasquet']

weights = [59, 50, 36, 26, 28,
           20, 19, 19, 18, 18]

df = pd.DataFrame(data=np.c_[source, target, weights], columns=['source','target','weight'])

# Initialize
d3 = D3Blocks(frame=False)
d3.chord(df, color='source', fontsize=20, opacity='source',
         title='Mean opponents of Novak Djokovic in ATP matches', filepath='Novak_Djokovic_atp_matches.html',
         cmap='tab20c', figsize=[1500,800], arrowhead=20, ordering='descending')
