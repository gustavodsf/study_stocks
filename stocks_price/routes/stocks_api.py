"""The Endpoints to manage the BOOK_REQUESTS"""
import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint
from service.stocks_service import StockService

REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

@REQUEST_API.route('/stock/<string:_ticker_code>', methods=['GET'])
def get_company_information_by_ticker(_ticker_code):
    """Get book request details by it's id
    @param _ticker_code: the code of the stocks
    @return: 200: return the information of the company that belongs the ticker.
    @raise 500: if has problem
    """
    stock_service = StockService()
    info_output = stock_service.getTickerInfo(_ticker_code)
    if info_output[1] == 0:
        abort(404)
    return jsonify(info_output[0])

@REQUEST_API.route('/stock/hist/min/<string:_ticker_code>', methods=['GET'])
def get_max_history_of_stock_by_ticker(_ticker_code):
    """Get book request details by it's id
    @param _ticker_code: the code of the stocks
    @return: 200: return the information of the company that belongs the ticker.
    @raise 500: if has problem
    """
    stock_service = StockService()
    info_output = stock_service.getTickerHistory(_ticker_code, "max")
    if info_output[1] == 0:
        abort(404)
    return jsonify(info_output[0])

@REQUEST_API.route('/stock/hist/max/<string:_ticker_code>', methods=['GET'])
def get_min_history_of_stock_by_ticker(_ticker_code):
    """Get book request details by it's id
    @param _ticker_code: the code of the stocks
    @return: 200: return the information of the company that belongs the ticker.
    @raise 500: if has problem
    """
    stock_service = StockService()
    info_output = stock_service.getTickerHistory(_ticker_code, "min")
    if info_output[1] == 0:
        abort(404)
    return jsonify(info_output[0])

@REQUEST_API.route('/stock/price/<string:_ticker_code>', methods=['GET'])
def get_sticks_price(_ticker_code):
    """Get book request details by it's id
    @param _ticker_code: the code of the stocks
    @return: 200: return the information of the company that belongs the ticker.
    @raise 500: if has problem
    """
    stock_service = StockService()
    info_output = stock_service.getStocksPriceNow(_ticker_code)
    if info_output[1] == 0:
        abort(404)
    return jsonify(info_output[0])
