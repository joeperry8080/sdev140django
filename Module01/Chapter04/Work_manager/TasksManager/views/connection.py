from django.shortcuts import render
# View for connection page. 
# renamed from "page" for clarity
def connections(request):
	return render(request, 'en/public/connection.html')