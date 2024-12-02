import analyzer as pt

pt.short_predict(ticker="AAPL", prediction_days=3, start_date="1996-01-01", file=False)
pt.range_predict(ticker="AAPL", prediction_days=60, start_date="1996-01-01", plot_show=True, file=True, log=True)