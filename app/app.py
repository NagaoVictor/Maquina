import plotly.express as px
import pandas as pd

df = pd.read_csv(r"..\data\Accounting_rates_and_market_rates_from_1959_to_1974.csv")

fig = px.line(
    df,
    x="Market Rate",
    y="Accounting Rate",
    title="Accounting Rates Over Time"
)

fig.show()