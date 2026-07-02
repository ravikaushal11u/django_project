from django.shortcuts import render
from .services import ApiServices

gemini_service = ApiServices()

def ai(request):
    prompt = ""
    ai_response = ""

    if request.method == "POST":
        prompt = request.POST.get("prompt")

        if prompt:
            ai_response = gemini_service.textQuery(prompt)

    context = {
        "prompt": prompt,
        "response": ai_response,
    }

    return render(request, "ai.html", context)