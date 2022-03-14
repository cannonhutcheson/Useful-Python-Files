import pandas as pd
data = pd.io.stata.read_stata("<INSERT YOUR STATA FILE PATH HERE>")
data.to_csv('<INSERT THE PATH OF THE LOCATION YOU WOULD LIKE TO SAVE YOUR CSV FILE AT>')

