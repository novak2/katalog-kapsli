from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from kapsle.models import UserCoin, Coin, Brewery, IgnoreCoin
from kapsle.forms import UserCoinCreateForm, IgnoreCoinCreateForm
from django.urls import reverse_lazy
#from django.urls import reverse
#from django.db.models import F
#from django.shortcuts import get_object_or_404


class WantListView(LoginRequiredMixin, ListView):
    model = Coin
    template_name = 'wantlist.html'
    login_url = '/login/'

    def get_queryset(self):
        queryset = Coin.objects.exclude(usercoin__owner=self.request.user).exclude(ignorecoin__owner=self.request.user).order_by('-year', '-wiki_index', 'brewery', 'index')
        return queryset


class BreweryListView(ListView):
    model = Brewery
    template_name = 'list.html'


class BreweryDetailView(DetailView):
    model = Brewery
    template_name = 'detail.html'


class CoinDetailView(LoginRequiredMixin, CreateView):
    form_class = UserCoinCreateForm
    template_name = 'kapsle/coin_detail.html'
    success_url = '/user/'
    login_url = '/login/'
    #model = Coin
    #fields = ['coin']
    #permission_required = 'kapsle.add_usercoin'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['coin'] = Coin.objects.get(pk=self.kwargs['pk'])
        context['ignore_coin'] = Coin.objects.filter(ignorecoin__owner=self.request.user).filter(pk=self.kwargs['pk'])
        #context['']
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.coin = Coin.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

#    def get_initial(self):
#        initial = super().get_initial()
#        initial['coin'] = self.kwargs['pk']
#        return initial


class IgnoreCoinCreateView(LoginRequiredMixin, CreateView):
    model = IgnoreCoin
    form_class = IgnoreCoinCreateForm
    #template_name_suffix = '_update_form'
    login_url = '/login/'

    def get_success_url(self, **kwargs):
        success_url = super().get_success_url
        success_url = reverse_lazy('coin-detail', kwargs={'pk': self.kwargs['pk'], 'slug': self.kwargs['slug']})
        return success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = Coin.objects.get(pk=self.kwargs['pk'])
        context['ignore_coin'] = Coin.objects.filter(ignorecoin__owner=self.request.user).filter(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.coin = Coin.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial


class IgnoreCoinDeleteView(LoginRequiredMixin, DeleteView):
    model = IgnoreCoin
    login_url = '/login/'

    def get_success_url(self, **kwargs):
        success_url = super().get_success_url
        success_url = reverse_lazy('coin-detail', kwargs={'pk': self.object.coin.id, 'slug': self.kwargs['slug']})
        return success_url

    def get_queryset(self):
        return IgnoreCoin.objects.filter(owner=self.request.user)


class UserCoinListView(LoginRequiredMixin, ListView):
    model = UserCoin
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(UserCoinListView, self).get_context_data(*args, **kwargs)
        context['dont_have_list'] = Coin.objects.exclude(usercoin__owner=self.request.user).exclude(ignorecoin__owner=self.request.user).order_by('-year', '-wiki_index', 'brewery', 'index')
        context['ignored'] = Coin.objects.filter(ignorecoin__owner=self.request.user).order_by('-year', '-wiki_index', 'brewery', 'index')
        return context

    def get_queryset(self):
        return UserCoin.objects.filter(owner=self.request.user)


class UserCoinUpdateView(LoginRequiredMixin, UpdateView):
    model = UserCoin
    template_name_suffix = '_update_form'
    login_url = '/login/'
    #raise_exception = True
    #form_class = CoinUpdateForm
    fields = ['user_image', 'types', 'kind', 'condition']
    #template_name = 'kapsle/form.html'
    success_url = '/user/'
    #permission_required = 'kapsle.change_usercoin'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return UserCoin.objects.filter(owner=self.request.user)


class UserCoinDeleteView(LoginRequiredMixin, DeleteView):
    model = UserCoin
    login_url = '/login/'
    success_url = reverse_lazy('user')

    def get_queryset(self):
        return UserCoin.objects.filter(owner=self.request.user)