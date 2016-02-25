from app.models import UserProfile


def save_profile_picture(backend, user, response, details, is_new=False, *args,                     **kwargs):
    
    if backend.__class__.__name__ == 'FacebookOAuth2' and is_new:
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        UserProfile.objects.create(user=user, picture_url=url)
