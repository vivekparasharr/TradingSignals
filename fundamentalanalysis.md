### install and import the package
pip install fundamentalanalysis
import fundamentalanalysis as fa

### access variables
ticker = "MSFT"
api_key = "xx"

### Show the available companies
companies = fa.available_companies(api_key)
companies

### Collect general company information
profile = fa.profile(ticker, api_key)
profile

### Collect recent company quotes
quotes = fa.quote(ticker, api_key)
quotes

### Collect market cap and enterprise value
entreprise_value = fa.enterprise(ticker, api_key)
entreprise_value

### Show recommendations of Analysts
ratings = fa.rating(ticker, api_key)
ratings

### Obtain DCFs over time
dcf_annually = fa.discounted_cash_flow(ticker, api_key, period="annual")
dcf_annually

### Collect the Income Statements
income_statement_annually = fa.income_statement(ticker, api_key, period="annual")
income_statement_annually

### Collect the Cash Flow Statements
cash_flow_statement_annually = fa.cash_flow_statement(ticker, api_key, period="annual")
cash_flow_statement_annually

### Show Key Metrics
key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
key_metrics_annually

### Show a large set of in-depth ratios
financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")
financial_ratios_annually

### Show the growth of the company
growth_annually = fa.financial_statement_growth(ticker, api_key, period="annual")
growth_annually

### Download general stock data
stock_data = fa.stock_data(ticker, period="ytd", interval="1d")
stock_data

### Download detailed stock data
stock_data_detailed = fa.stock_data_detailed(ticker, api_key, begin="2000-01-01", end="2020-01-01")
stock_data_detailed

### Download dividend history
dividends = fa.stock_dividend(ticker, api_key, begin="2000-01-01", end="2020-01-01")
dividends
