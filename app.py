from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
from config.stocks import Stock, session
import json


app = Flask(__name__)

@app.route('/create-stock', methods=['POST'])
def createStock():
    data = request.get_json()
    try: 
        stock = Stock(symbol= data['symbol'], name=data['name'], price=data['price'])
        session.add(stock)
        session.commit()
        return("Stock has been added")
    except Exception as e:
        session.rollback()
        return(f"{e}")
    finally:
        session.close()
        

@app.route("/get-all-stocks", methods=['GET'])
def getAllStocks():
    try:
        stocks = session.query(Stock).all()
        allStocks = []
        for stock in stocks:
            allStocks.append({"name": stock.name, "id": stock.id, "symbol": stock.symbol, "price": stock.price})
        return(jsonify(allStocks))
    except Exception as e:
        session.rollback()
        return(f"{e}")
    finally:
        session.close()

@app.route('/get-stock/<string:symbol>', methods=['GET'])
def method_name(symbol):
    try:
        stock = session.query(Stock).filter(Stock.symbol == symbol).first()
        if stock is None:
            return("No stock available for this symbol try with some other symbol")
        foundStock = {"name": stock.name, "id": stock.id, "symbol": stock.symbol, "price": stock.price}
        return(jsonify(foundStock)), 200
            
    except Exception as e:
        session.rollback()
        return(f"{e}")
    finally:
        session.close()


app.run(debug=True)