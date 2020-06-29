import yfinance as yf

class StockService(object):
    
    def getTickerInfo(self, ticker_code):
        try:
            ticker_code = ticker_code.upper()
            ticker = yf.Ticker(ticker_code)
            import pdb; pdb.set_trace()
            return (ticker.info, 1)
        except ValueError as ve:
            return ("Ticker didn't exist.", 0)
        except Exception as e:
            return ("Problem to connect to the service.", 0)

    def getTickerHistory(self, ticker_code, history_type="max"):
        try:
            ticker_code = ticker_code.upper()
            ticker = yf.Ticker(ticker_code)
            pd_col = ticker.history(period=history_type)
            pd_col.index = pd_col.index.strftime('%Y-%m-%d %H:%M')
            hist_dict = pd_col.to_dict()
            return (hist_dict, 1)
        except ValueError as ve:
            return ("Ticker didn't exist.", 0)
        except Exception as e:
            return ("Problem to connect to the service.", 0)

    def getStocksPriceNow(self, ticker_code):
        try:
            ticker_code = ticker_code.upper()
            result = yf.download(tickers=ticker_code, period='1d', interval = "1m")
            import pdb; pdb.set_trace()
            result.index = result.index.strftime('%Y-%m-%d %H:%M')
            hist_dict = result.to_dict()
            return (hist_dict, 1)
        except ValueError as ve:
            return ("Ticker didn't exist.", 0)
        except Exception as e:
            return ("Problem to connect to the service.", 0)
