from social.models import Link


def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()

    for l in links:
        ctx[l.key] = l.url

    return ctx
