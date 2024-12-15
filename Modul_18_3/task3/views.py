from django.shortcuts import render, redirect

cart_items = {}

def main(request):
    title = 'Онлайн магазин настолок'
    text1 = ('Мы любим вас и ненавидим, как друзей, покупайте же у нас настолки для себя и своих друзей (с нами '
             'поиграть тоже можно)')
    context = {
        'title': title,
        'text1': text1,
    }
    return render(request, 'third_task/main_page.html', context)

def shop(request):
    games = [
        {"name": "Bullet", "price": 13},
        {"name": "Feet The Kraken", "price": 39},
        {"name": "The East Indian Campaign", "price": 19},
    ]

    if request.method == "POST":
        game_name = request.POST.get('game_name')
        game_price = next((game["price"] for game in games if game["name"] == game_name), None)

        if game_name in request.session['cart']:
            request.session['cart'][game_name]['quantity'] += 1
        else:
            request.session['cart'][game_name] = {'price': game_price, 'quantity': 1}


    if 'cart' not in request.session:
        request.session['cart'] = {}

    context = {
        'games': games,
        'cart_items': request.session.get('cart', {}),
    }
    return render(request, 'third_task/shop.html', context)

def cart(request):
    cart_items = request.session.get('cart', {})
    total_price = 0
    items_to_display = []

    for item_name, item_info in cart_items.items():
        item_price = item_info['price']
        item_quantity = item_info['quantity']
        total_price += item_price * item_quantity
        items_to_display.append((item_name, item_price, item_quantity))

    return render(request, 'third_task/cart.html', {'cart_items': items_to_display, 'total_price': total_price})
