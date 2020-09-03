from django.shortcuts import render, redirect
from django.views.generic.base import View
import telegram
from django.conf import settings
from .models import Doc, Services, Event
from .forms import ReceptionForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




class Doctors(View):
    def get(self, request):
        docs = Doc.objects.all()
        services = Services.objects.all().filter(id__lte=6)
        new = Event.objects.all()[:2:-1]
        content = {
            'docs_list': docs,
            'services': services,
            'news': new
        }
        return render(request, "doc/main_description.html", content)

    def post(self, request):
        form = ReceptionForm(request.POST)
        if form.is_valid():
            msg = form.save()
            # reception = Reception.objects.last()
            token = settings.TELEGRAM['bot_token']
            chat_id = settings.TELEGRAM['channel_name']
            bot = telegram.Bot(token)
            bot.send_message(chat_id, str(msg))
            return redirect("/")
        return redirect("/")

class News(View):
    # paginate_by = 2
    context_object_name = 'news'
    template_name = 'doc/news1.html'

    def get(self, request):
        news = Event.objects.all().filter()
        paginator = Paginator(news, 10)
        page = self.request.GET.get('page')
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            news = paginator.page(paginator.num_pages)
        content = {
            'news': news,
        }
        return render(request, 'doc/news1.html', content)


class Service(View):
    def get(self, request):
        services = Services.objects.all()
        content = {
            'services': services,
        }
        return render(request, 'doc/service1.html', content)


# class AboutUs(View):
#     def get(self, request):
#         return render(request, 'pages/about_us.html')


class Docs(View):
    def get(self, request):
        docs = Doc.objects.all()
        content = {
            'docs_list': docs,
        }
        return render(request, 'doc/docs.html', content)


class Contact(View):
    def get(self, request):
        return render(request, 'doc/contact.html')
class Prep(View):
    def get(self, request):
        return render(request, 'doc/Prep.html')

class After(View):
    def get(self, request):
        return render(request, 'doc/Page.html')

class Quest(View):
    def get(self, request):
        return render(request, 'doc/Quest.html')