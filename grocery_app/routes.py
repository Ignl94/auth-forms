from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
# from grocery_app.forms import BookForm, AuthorForm, GenreForm
from grocery_app.forms import GroceryStoreForm, GroceryItemForm

# Import app and db from events_app package so that we can run app
from grocery_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################


@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)


@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    # TODO: Create a GroceryStoreForm
    grocery_store_form = GroceryStoreForm()

    # TODO: If form was submitted and was valid:
    # - create a new GroceryStore object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the store detail page.
    if grocery_store_form.validate_on_submit():
        grocery_store = GroceryStore(
            title=grocery_store_form.title.data, address=grocery_store_form.address.data)
        db.session.add(grocery_store)
        db.session.commit()
        return redirect(f'/store/{grocery_store.id}')

    # TODO: Send the form to the template and use it to render the form fields
    return render_template('new_store.html', grocery_store_form=grocery_store_form)


@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    # TODO: Create a GroceryItemForm
    grocery_item_form = GroceryItemForm()

    # TODO: If form was submitted and was valid:
    # - create a new GroceryItem object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the item detail page.
    if grocery_item_form.validate_on_submit():
        grocery_item = GroceryItem(name=grocery_item_form.name.data, price=grocery_item_form.price.data,
                                   category=grocery_item_form.category.data, photo_url=grocery_item_form.photo_url.data, store=grocery_item_form.store.data)
        db.session.add(grocery_item)
        db.session.commit()
        print('########## Store Item commited ######')
        flash('Added Grocery Item')
        return redirect(f'/item/{grocery_item.id}')

    # TODO: Send the form to the template and use it to render the form fields
    return render_template('new_item.html', grocery_item_form=grocery_item_form)


@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    # TODO: Create a GroceryStoreForm and pass in `obj=store`
    grocery_store_form = GroceryStoreForm(obj=store)

    # TODO: If form was submitted and was valid:
    # - update the GroceryStore object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the store detail page.
    if grocery_store_form.validate_on_submit():
        store.title = grocery_store_form.title.data
        store.address = grocery_store_form.address.data
        db.session.add(store)
        db.session.commit()
        # TODO: Send the form to the template and use it to render the form fields
    store = GroceryStore.query.get(store_id)
    return render_template('store_detail.html', store=store, grocery_store_form=grocery_store_form)


@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    # TODO: Create a GroceryItemForm and pass in `obj=item`
    grocery_item_form = GroceryItemForm(obj=item)

    # TODO: If form was submitted and was valid:
    # - update the GroceryItem object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the item detail page.
    if grocery_item_form.validate_on_submit():
        item.name = grocery_item_form.name.data
        item.price = grocery_item_form.price.data
        item.category = grocery_item_form.category.data
        item.photo_url = grocery_item_form.photo_url.data
        item.store = grocery_item_form.store.data
        db.session.add(item)
        db.session.commit()

    # TODO: Send the form to the template and use it to render the form fields
    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item, grocery_item_form=grocery_item_form)
