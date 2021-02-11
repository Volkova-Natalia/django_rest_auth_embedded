from django.views.generic import TemplateView

from django.urls import reverse, get_resolver

from ..settings import app_name, end_point


class SwaggerExpectedView(TemplateView):

    # --------------------------------------------------

    def __init__(self, **kwargs):
        namespace = ""
        for url_pattern in get_resolver().url_patterns:
            try:
                if (url_pattern.urlconf_name.__name__ == get_resolver(app_name + '.urls').urlconf_name):
                    namespace = url_pattern.namespace + ":"
                    break
            except:
                pass

        absolute_url_swagger_expected = reverse(namespace + end_point['swagger_expected']['name'])
        pos_local_url_swagger_expected = absolute_url_swagger_expected.find(end_point['swagger_expected']['url'])
        base_url = absolute_url_swagger_expected[:pos_local_url_swagger_expected]

        kwargs['template_name'] = app_name + r'/swagger/index.html'
        kwargs['extra_context'] = {'base_url': base_url, 'app_name': app_name}

        super().__init__(**kwargs)
