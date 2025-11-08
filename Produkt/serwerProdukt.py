from flask import Flask, jsonify

app = Flask(__name__)

products = {
    123: {"id": 123, "name": "Laptop", "price": 4500.00},
    124: {"id": 124, "name": "Smartphone", "price": 2500.00},
}

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(port=8001)
