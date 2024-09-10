from django.shortcuts import render

def show_main(request):
    # Data produk dalam bentuk list of dictionaries
    products = [
        {
            'name': 'Microscope X200',
            'price': 2000000,
            'description': 'High-quality microscope suitable for research and education purposes.',
            'rating': 4
        },
        {
            'name': 'Centrifuge 3000 RPM',
            'price': 5000000,
            'description': 'High-speed centrifuge for separating fluids and gases based on density.',
            'rating': 5
        },
        {
            'name': 'Autoclave Sterilizer',
            'price': 7000000,
            'description': 'Compact autoclave for sterilization in laboratories.',
            'rating': 4
        },
    ]
    
    # Context untuk dikirimkan ke template
    context = {
        'products': products
    }
    
    # Merender template main.html dengan context
    return render(request, "main.html", context)
