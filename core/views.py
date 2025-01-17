from django.shortcuts import render
from django.https import HttpResponse

def home(request):
    return HttpResponse("Hello world")

# echo "# AccentArea" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/joseyawovi/AccentArea.git
# git push -u origin main

