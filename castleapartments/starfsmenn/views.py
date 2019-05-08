from django.shortcuts import render

dummies = [
    {
        "name": "J Json",
        "license": "Löggiltur Fasteignarsali",
        "contactInfo": "dummy@dummies.com",
        "description": "I did stuff before i sold houses"
    },

    {
        "name": "Brainan",
        "license": "Löggiltur Fasteignarsali",
        "contactInfo": "dummy@dummies.com",
        "description": "Houses aint the only thing i sell ;)"
    },

    {
        "name": "Brainina",
        "license": "Löggiltur Fasteignarsali",
        "contactInfo": "dummy@dummies.com",
        "description": "This is just temporary..."
    },

    {
        "name": "Samus Aran",
        "license": "Löggiltur Fasteignarsali",
        "contactInfo": "dummy@dummies.com",
        "description": "My parents wanted a girl... and liked metroid"
    },
]

def index(request):
    context = {"dummies": dummies}
    return render(request, 'starfsmenn/index.html', context)

