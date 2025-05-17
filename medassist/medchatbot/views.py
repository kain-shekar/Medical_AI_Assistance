import os
from groq import Groq
from django.conf import settings
from django.shortcuts import render

# Initialize Groq client using Django settings (make sure it's defined in settings.py or .env)
client = Groq(api_key=settings.GROQ_API_KEY)

def medchat(request):
    answer = None
    if request.method == 'POST':
        user_query = request.POST.get('query')
        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": user_query
                    }
                ]
            )
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"An error occurred: {e}"

    return render(request, 'medchat.html', {'answer': answer})
