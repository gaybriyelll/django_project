from django.shortcuts import render
from django.http import HttpResponse

def breeds(request):
    return render(request, 'cats/breeds.html')

def facts(request):
    return render(request, 'cats/facts.html')

def gallery(request):
    return render(request, 'cats/gallery.html')

def index(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Cats Home</title>
                <link href="https://cdn.jsdelivr.net/npm/bootswatch@5.3.0/dist/sketchy/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="container d-flex flex-column justify-content-center align-items-center vh-100">
                    <h1 class="text-center">Welcome to the Cats Section</h1>
                    <p class="text-center">Explore the different breeds, facts, and gallery about cats.</p>
                    <div>
                        <a href="/" class="btn btn-dark mx-2">Home</a> <!-- Button to go back to home -->
                        <a href="/cats/breeds/" class="btn btn-primary mx-2">Cat Breeds</a>
                        <a href="/cats/facts/" class="btn btn-info mx-2">Cat Facts</a>
                        <a href="/cats/gallery/" class="btn btn-success mx-2">Cat Gallery</a>
                    </div>
                </div>
            </body>
        </html>
    """)
