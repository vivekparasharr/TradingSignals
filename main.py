import fundamentalanalysis as fa
import pandas as pd
import os

ticker = "MSFT"
api_key = os.environ['api_key_value']

companies = fa.available_companies(api_key)
print(companies.info())
