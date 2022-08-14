from . models import *

def cartData(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems= order.get_cart_items
    
    return {'items':items, 'order':order, 'cartItems':cartItems}

