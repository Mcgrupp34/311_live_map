

import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("fhrw-4uyv", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df)