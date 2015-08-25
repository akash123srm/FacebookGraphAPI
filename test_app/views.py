from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.conf import settings
from .models import UserProfile
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import facebook
import json
import urllib

# Create your views here.


class AuthorizeView(TemplateView):
    template_name = "authorize.html"

    def get_context_data(self, **kwargs):
        self.url_authorize = 'https://www.facebook.com/dialog/oauth?client_id={0}&redirect_uri={1}'.format(settings.SOCIAL_AUTH_FACEBOOK_KEY, settings.REDIRECT_URI)
        return {
            'url': self.url_authorize,
        }

    def dispatch(self, request, *args, **kwargs):
         return super(AuthorizeView, self).dispatch(request, *args, **kwargs)


EXTENDED_TOKEN = ''


def login_view(request):
    try:
            parameters = facebook.get_access_token_from_code(request.GET['code'], settings.REDIRECT_URI,
                                                          settings.SOCIAL_AUTH_FACEBOOK_KEY, settings.SOCIAL_AUTH_FACEBOOK_SECRET)
            access_token = parameters['access_token']

            #Another approach could be to read the url & parse it as JSON

            '''url_access = 'https://graph.facebook.com/v2.3/oauth/access_token?client_id={0}&redirect_uri={1}&client_secret={2}&code={3}'\
                    .format(settings.SOCIAL_AUTH_FACEBOOK_KEY, settings.REDIRECT_URI, settings.SOCIAL_AUTH_FACEBOOK_SECRET,code)
            response = urllib.urlopen(url_access)
            self.access_token = json.loads(response.read())['access_token']'''

            #Extend the token validity

            graph = facebook.GraphAPI(access_token=access_token)
            extend_object = graph.extend_access_token(app_id=settings.SOCIAL_AUTH_FACEBOOK_KEY, app_secret=settings.SOCIAL_AUTH_FACEBOOK_SECRET)
            global EXTENDED_TOKEN
            EXTENDED_TOKEN = extend_object['access_token']


    except Exception, e:
            print e
    return render(request, 'login.html')


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        graph = facebook.GraphAPI(access_token=EXTENDED_TOKEN)
        profile = graph.get_object(id='me')
        url_profile_picture = 'http://graph.facebook.com/{0}/picture?type=large'.format(profile['id'])
        print profile['name'].replace(" ", "")
        try:
            user = User.objects.get(username=profile['name'].replace(" ",""))
            print user
            e, created = UserProfile.objects.get_or_create(name=user, id=profile['id'],
                                                          access_token=EXTENDED_TOKEN)
            e.save()
        except ObjectDoesNotExist:
            return None

        return {
            'user_name': profile['name'],
            'url_profile_picture': url_profile_picture,

             }










