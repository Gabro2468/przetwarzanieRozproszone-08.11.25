from flask import Flask, jsonify
import requests

app = Flask(__name__)

stock = {
    123: 15,
    124: 70,
}

PRODUCT_SERVER_URL = "http://localhost:8001/products/{}"

@app.route('/stock/<int:product_id>', methods=['GET'])
def get_stock(product_id):
    # Get product info from Product Server
    response = requests.get(PRODUCT_SERVER_URL.format(product_id))
    if response.status_code != 200:
        return jsonify({"error": "Product not found"}), 404

    product_info = response.json()
    quantity = stock.get(product_id)

    # Show 404 if no stock info found for product
    if quantity is None:
        return jsonify({"error": "Stock not found"}), 404

    # Return combined info
    return jsonify({
        "id": product_info["id"],
        "name": product_info["name"],
        "price": product_info["price"],
        "quantity": quantity
    })

if __name__ == "__main__":
    app.run(port=8002)
