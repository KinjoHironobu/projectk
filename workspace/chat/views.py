from django.http import StreamingHttpResponse
from django.shortcuts import render
from openai import OpenAI

def index(request):
    return render(request, "chat/index.html")

def chatgpt_stream(request):
    #イベントストリームの送信を開始する前に、必要なレスポンスヘッダーを設定する
     response = StreamingHttpResponse(streaming_content = stream_events())
     response['Content-Type'] = 'text/event-stream'
     response['Cache-control'] = 'no-cache'
     return response

def stream_events():
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは優秀なアシスタントです。質問に対しては日本語で回答します。"},
            {"role": "user", "content": "インボイス制度について詳しく教えて"},
        ],
        stream=True
    )
    for chunk in completion:
        print(chunk)
        yield f'data: {chunk.choices[0].delta.content}\n\n'
    