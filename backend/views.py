from django.http import JsonResponse
from rest_framework.decorators import api_view

from .utils import saveFileToServer, cleanFileContent, tokenizeAndSummarize

@api_view(['POST'])
def summarize(request):
  if (request.method == 'POST'):
    file = request.FILES['file']
    saveFileToServer(file);
    cleanText = cleanFileContent();
    output = tokenizeAndSummarize(cleanText);
    print("\n\nSummarized text: \n", output)

    return JsonResponse({'output': output})