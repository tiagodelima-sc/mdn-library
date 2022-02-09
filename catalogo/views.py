from django.shortcuts import render
from django.views import generic

# Create your views here.

from catalogo.models import Genero, Linguaguem, Autor, Livro, ExemplarLivro

def index(request):
  
    # contando o numero de livros e exemplares  
    num_livros = Livro.objects.all().count()
    num_exemplares = ExemplarLivro.objects.all().count()
    
    # Contando a quantidade de exemplares disponiveis (situacao = 'd')
    num_exemplares_disponiveis = ExemplarLivro.objects.filter(situacao__exact='d').count()
    
    # Contando o numero de autores. A opcao 'all()' é implicita por padrao
    num_autores = Autor.objects.count()
    
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1
    
    contexto = {
      'num_livros': num_livros,
      'num_exemplares': num_exemplares,
      'num_exemplares_disponiveis': num_exemplares_disponiveis,
      'num_autores': num_autores,
      'num_visitas': num_visitas,
    }
    
    # renderizando o template index.html com os dados da variavel contexto
    return render(request, 'index.html', context=contexto)
  
class BookListView(generic.ListView):
      
      model =  Livro
      
class BookDetailView(generic.DetailView):
      
      model = Livro
      
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):

    model = ExemplarLivro
    template_name = 'catalogo/exemplares_emprestados_usuario.html'

    def get_queryset(self):
        return ExemplarLivro.objects.filter(usuario=self.request.user).filter(situacao__exact='e').order_by('data_devolucao')
