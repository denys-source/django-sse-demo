import asyncio

from django.http import HttpResponse, StreamingHttpResponse
from django.utils import timezone

from django_eventstream import send_event


async def clock(request):

    async def event_stream():
        while True:
            yield f"data: The server time is: {timezone.now()}\n\n".encode("utf-8")
            await asyncio.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


def send_event_view(request):
    send_event("test", "message", {"text": "hello world"})

    return HttpResponse("Event has been sent")
