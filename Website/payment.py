from flask import Blueprint, render_template, request,flash
from flask_login import  login_required, current_user
from .models import Basket, Items


payment = Blueprint('payment', __name__)

@payment.route('/payment', methods = ['GET', 'POST'])
@login_required
def pay():

    if request.method == 'POST':
          CVC = request.form.get('CVC')
          CardNumber = request.form.get('cardnumber')
          DOE = request.form.get('DOE')
          flash('Payment accpeted, thank you', category = 'success')

    return render_template("payment.html") #Payment screen 

@payment.route('/basket')
@login_required
def basket():
     
      items = Basket.query.filter_by(user_id=current_user.id).all()
      totalprices = []
      products2 = []
      for item in items:
            pricequery = Items.query.filter_by(id=item.item_id).first()
            products2.append(pricequery)
            temp = int(item.quantity) * pricequery.price
            totalprices.append(temp)

      totalprice = sum(totalprices)

      
      return render_template("basket.html", basket=items, totalprice=totalprice, product=products2)