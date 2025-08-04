from django.shortcuts import render

def product_list(request):
    return render(request, 'store/home.html')  # ✅ Correct path
