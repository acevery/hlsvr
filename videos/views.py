from django.shortcuts import render, get_object_or_404
from videos.models import Video
# Create your views here.


def video_detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    context = {'the_video': video}
    return render(request, 'videos/single.html', context)


def video_list(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'videos/list.html', context)
