from django.shortcuts import render
from django.http import HttpResponse

def types(request):
    return render(request, 'kittens/types.html')

def care(request):
    return render(request, 'kittens/care.html')

def photos(request):
    return render(request, 'kittens/photos.html')

def index(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Kittens Home</title>
                <link href="https://cdn.jsdelivr.net/npm/bootswatch@5.3.0/dist/sketchy/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="container d-flex flex-column justify-content-center align-items-center vh-100">
                    <h1 class="text-center">Welcome to the Kittens Section</h1>
                    <p class="text-center">Explore different types of kittens, their care, and photos.</p>
                    <div>
                        <a href="/" class="btn btn-dark mx-2">Home</a> <!-- Button to go back to home -->
                        <a href="/kittens/types/" class="btn btn-primary mx-2">Kitten Types</a>
                        <a href="/kittens/care/" class="btn btn-info mx-2">Kitten Care</a>
                        <a href="/kittens/photos/" class="btn btn-success mx-2">Kitten Photos</a>
                    </div>
                </div>
            </body>
        </html>
    """)
