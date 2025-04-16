from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    """메인 페이지 뷰"""
    messages = Message.objects.all()
    return render(request, 'web_app/index.html', {'messages': messages})

@csrf_exempt
def create_message(request):
    """메시지 생성 API"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('content', '')
            if content:
                message = Message.objects.create(content=content)
                return JsonResponse({
                    'status': 'success',
                    'message_id': message.id,
                    'content': message.content,
                    'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                return JsonResponse({'status': 'error', 'message': '내용이 비어있습니다.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': '잘못된 요청입니다.'}, status=405)

@csrf_exempt
def get_messages(request):
    """메시지 목록 조회 API"""
    messages = Message.objects.all()
    data = [{
        'id': msg.id,
        'content': msg.content,
        'created_at': msg.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for msg in messages]
    return JsonResponse({'status': 'success', 'messages': data})
