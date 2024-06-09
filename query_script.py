from flask import Flask , request , render_template,  jsonify
from model import db , Product, Category
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://seller:#Seller_Admin1234@localhost/product_store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db.init_app(app)

# Initialize the database (create tables)
with app.app_context():
    db.create_all()


# Define API resources
class ProductResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([{
            'id': product.id,
            'title': product.title,
            'price': product.price,
            'quantity': product.quantity
        } for product in products])

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        return jsonify([{
            'id': category.id,
            'title': category.title
        } for category in categories])

# Add resources to the API
api.add_resource(ProductResource, '/api/products')
api.add_resource(CategoryResource, '/api/categories')

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Path to the API specification
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Product Store API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)

