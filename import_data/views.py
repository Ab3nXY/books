# import_data/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ExcelFileUploadForm
from subprocess import run

def upload_excel_file(request):
    if request.method == 'POST':
        form = ExcelFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            # Save the uploaded file to a temporary location (or process it directly)
            with open('temp.xlsx', 'wb') as destination:
                for chunk in excel_file.chunks():
                    destination.write(chunk)

            # Run the management command
            command = f'python manage.py import_excel_data temp.xlsx'
            result = run(command, shell=True)

            if result.returncode == 0:
                # The command executed successfully
                return render(request, 'import_data/upload_success.html', {'success_message': 'successfuly uploaded and imported'})  # Redirect to a success page
            else:
                # Handle any errors or failures
                return render(request, 'import_data/error_page.html', {'error_message': 'Processing failed.'})
    else:
        form = ExcelFileUploadForm()

    return render(request, 'import_data/upload_excel_file.html', {'form': form})
