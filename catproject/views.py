from django.http import HttpResponse

def homepage(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Welcome to Cat World</title>
                <link href="https://cdn.jsdelivr.net/npm/bootswatch@5.3.0/dist/sketchy/bootstrap.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="container d-flex flex-column justify-content-center align-items-center vh-100">
                    <h1 class="text-center">Welcome to Cat World</h1>
                    <p class="text-center">Explore our Cats and Kittens sections!</p>
                    <div>
                        <a href="/cats/" class="btn btn-primary mx-2">Explore Cats</a>
                        <a href="/kittens/" class="btn btn-success mx-2">Explore Kittens</a>
                    </div>
                </div>
            </body>
        </html>
    """)
