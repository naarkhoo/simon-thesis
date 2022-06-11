import wget
import pandas as pd

output = pd.read_csv(CSVFILENAME)

filename = output.iloc[0].image.replace('p/', '')
URL = 'https://images.vivino.com/labels/{0}'.format(filename)

import wget
response = wget.download(URL,filename)
