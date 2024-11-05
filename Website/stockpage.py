from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_required, current_user
from .models import Items, Basket, User
from . import db

stockpage = Blueprint('items',__name__)

@stockpage.route('/item1',methods=['GET', 'POST'])
def item1():
    item = Items.query.filter_by(name = 'Red Flowers').first()

    if request.method == "POST":
        new_basketitem = Basket(user_id = current_user.id, item_id = item.id, quantity = int(request.form.get('Quantity')))
        existing_item = Basket.query.filter_by(user_id=current_user.id, item_id=item.id).first()


        if existing_item:
            existing_item.quantity += new_basketitem.quantity
        else:
            db.session.add(new_basketitem)
        
        db.session.commit()
        flash('Added successfully', category = 'success')
        return redirect(url_for('views.home'))
    
    return render_template('item.html', itemname = item.name, picture = item.picture, price = item.price, enviroment_impact = item.enviroment_impact, description = item.description )

@stockpage.route('/item2', methods=['GET', 'POST'])  
def item2():
    item = Items.query.filter_by(name = 'Pink Flowers').first()

    if request.method == "POST":
            new_basketitem = Basket(user_id = current_user.id, item_id = item.id, quantity = int(request.form.get('Quantity')))
            existing_item = Basket.query.filter_by(user_id=current_user.id, item_id=item.id).first()


            if existing_item:
                existing_item.quantity += new_basketitem.quantity
            else:
                db.session.add(new_basketitem)
        
            db.session.commit()
            flash('Added successfully', category = 'success')
            return redirect(url_for('views.home'))
    

    return render_template('item.html', itemname = item.name, picture = item.picture, price = item.price, enviroment_impact = item.enviroment_impact, description = item.description )

@stockpage.route('/item3', methods=['GET', 'POST'])
def item3():
    item = Items.query.filter_by(name = 'Yellow Flowers').first()

    if request.method == "POST":
        new_basketitem = Basket(user_id = current_user.id, item_id = item.id, quantity = int(request.form.get('Quantity')))
        existing_item = Basket.query.filter_by(user_id=current_user.id, item_id=item.id).first()


        if existing_item:
            existing_item.quantity += new_basketitem.quantity
        else:
            db.session.add(new_basketitem)
        
        db.session.commit()
        flash('Added successfully', category = 'success')
        return redirect(url_for('views.home'))
    


    return render_template('item.html', itemname = item.name, picture = item.picture, price = item.price, enviroment_impact = item.enviroment_impact, description = item.description )


@stockpage.route('/item4',methods=['GET', 'POST'])
def item4():
    item = Items.query.filter_by(name = 'Blue Flowers').first()

    if request.method == "POST":
        new_basketitem = Basket(user_id = current_user.id, item_id = item.id, quantity = int(request.form.get('Quantity')))
        existing_item = Basket.query.filter_by(user_id=current_user.id, item_id=item.id).first()


        if existing_item:
            existing_item.quantity += new_basketitem.quantity
        else:
            db.session.add(new_basketitem)
        
        db.session.commit()
        flash('Added successfully', category = 'success')
        return redirect(url_for('views.home'))
    

    return render_template('item.html', itemname = item.name, picture = item.picture, price = item.price, enviroment_impact = item.enviroment_impact, description = item.description )




