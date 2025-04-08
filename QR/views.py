from django.shortcuts import render
from .forms import QRCodeForm
import qrcode

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']  # removed space
            url = form.cleaned_data['url']

            # Generate QR code
            qr_img = qrcode.make(url)
            qr_img.save(f'{res_name}_qr.png') 
            context  = {
                'res_name':res_name ,
            }
            return render (request , 'qr_result.html' , context)# Save with a more descriptive filename
    else:
        form = QRCodeForm()

    context = {
        'form': form,
    }
    return render(request, 'generate_qr_code.html', context)
