from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Empresa, Avaliacao, Review
from .forms import LoginForm, CadastroForm, AvaliacaoForm
from django.shortcuts import redirect

# CBV para listar empresas
class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa_list.html'
    context_object_name = 'empresas'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avaliacao_form'] = AvaliacaoForm()
        return context

# CBV para detalhes da empresa
class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'empresa_detail.html'

# FBV para login de usuários
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha incorretos')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# FBV para cadastro de usuários
def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro no cadastro. Por favor, tente novamente.')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

@login_required(login_url='/login/')
def avaliar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao, created = Avaliacao.objects.update_or_create(
                empresa=empresa,
                usuario=request.user,
                defaults={
                    'nota': form.cleaned_data['nota'],
                    'comentario': form.cleaned_data['comentario']
                }
            )
            if created:
                messages.success(request, 'Sua avaliação foi criada com sucesso!')
            else:
                messages.success(request, 'Sua avaliação foi atualizada com sucesso!')
            return redirect('empresa_detail', pk=empresa.pk)
        else:
            messages.error(request, 'Erro ao salvar a avaliação.')
    else:
        form = AvaliacaoForm()
    return render(request, 'empresa_detail.html', {'form': form, 'empresa': empresa})


# FBV para comentar sobre a avaliação de uma empresa
@login_required
def comentario_view(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk, usuario=request.user)
    if request.method == 'POST':
        texto = request.POST.get('comentario')
        Review.objects.create(avaliacao=avaliacao, texto=texto)
        messages.success(request, 'Seu comentário foi salvo com sucesso!')
        return redirect('empresa_detail', pk=avaliacao.empresa.pk)
    else:
        return render(request, 'comentario.html', {'avaliacao': avaliacao})
    
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso.')
    return redirect('login')  # Redireciona para a página de login

