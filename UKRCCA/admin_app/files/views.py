from django.views.generic import TemplateView

class CompCrePageView(TemplateView):
    template_name = 'compcre.html'

class CompsPageView(TemplateView):
    template_name = 'comps.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class LeadBPageView(TemplateView):
    template_name = 'leadb.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class RulesPageView(TemplateView):
    template_name = 'rules.html'

class LightRulesPageView(TemplateView):
    template_name = 'lightrules.html'

class HeavyRulesPageView(TemplateView):
    template_name = 'fullrules.html'