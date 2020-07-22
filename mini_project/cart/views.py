from django.shortcuts import render
from django.views.decorators.http import require_POST
# from shop.models import Product
# from .forms import AddProductForm
# from .cart import Cart


# def add(request, dest_id):
#     cart = Cart(request)
#     Product = get_object_or_404(Product, id=dest_id)
#     # 클라이언트 -> 서버로 데이터 전달
#     # 유효성 검사, injection 전처리
#     form = AddProductForm(request.POST)

#     if form.is_valid():
#         cd = form.cleaned
#         cart.add(product=product, is_update=cd['is_update'])

#     return redirect('cart.detail')