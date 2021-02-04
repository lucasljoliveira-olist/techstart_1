from flask import Blueprint, render_template, redirect, request
from back.controllers.category_controller import CategoryController
from back.models.category import Category


category_bp = Blueprint('category', __name__)


@category_bp.route('/category')
def category():
    items = CategoryController().read_all()
    return render_template('list_category.html', items=items)


@category_bp.route('/category/create')
def category_create_form():
    return render_template('create_category.html')

@category_bp.route('/category', methods=['POST'])
def category_create():
    name = request.form.get('name')
    description = request.form.get('description')
    item = Category(name, description)
    CategoryController().create(item)
    return redirect('/category')

@category_bp.route('/category/update/<int:id>')
def category_update_form(id):
    item = CategoryController().read_by_id(id)
    return render_template('update_category.html', item=item)


@category_bp.route('/category/update', methods=['POST'])
def category_update():
    item = CategoryController().read_by_id(int(request.form.get('id')))
    item.name = request.form.get('name')
    item.description = request.form.get('description')
    CategoryController().update(item)
    return redirect('/category')


@category_bp.route('/category/delete/<int:id>')
def category_delete(id):
    item = CategoryController().read_by_id(id)
    CategoryController().delete(item)
    return redirect('/category')
