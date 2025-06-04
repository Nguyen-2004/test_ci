from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms_sqlalchemy.fields import QuerySelectField


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)

# =========================
# Models
# =========================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

# =========================
# Admin Views
# =========================

class UserView(ModelView):
    column_list = ['id', 'name', 'email']
    column_searchable_list = ['name', 'email']
    column_filters = ['name']
    can_delete = True

class ProductView(ModelView):
    column_list = ['id', 'name', 'price', 'category']
    column_searchable_list = ['name']
    column_filters = ['price', 'category.name']

    form_extra_fields = {
        'category': QuerySelectField(
            'Category',
            query_factory=lambda: Category.query.all(),
            allow_blank=False
        )
    }

# =========================
# Routes
# =========================

@app.route('/')
def home():
    return redirect('/admin')

# =========================
# Flask-Admin Setup
# =========================

admin = Admin(app, name='Quản trị hệ thống', template_mode='bootstrap3')
admin.add_view(UserView(User, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(ModelView(Category, db.session))

# =========================
# Run App
# =========================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)