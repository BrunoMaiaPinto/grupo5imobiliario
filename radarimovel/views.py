from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Imovel, Localizacao, Proprietario
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'radarimovel/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('radarimovel:index')  # Redireciona para a página inicial após o login bem-sucedido
        else:
            return render(request, 'radarimovel/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'radarimovel/login.html')  # Página de login

def user_logout(request):
    logout(request)
    return redirect('radarimovel:index')  # Redirect to the homepage after logout

def imoveis(request):
    imoveis = Imovel.objects.all()

    if request.method == 'POST':
        tipologia = request.POST.get('Tipologia')
        tipoImovel = request.POST.get('tipo_de_imovel')
        endereco = request.POST.get('morada')
        cod_postal = request.POST.get('codigo_postal')
        preco = request.POST.get('preco_pedido')
        area = request.POST.get('area_m2')
        
        preco_max = request.POST.get('preco_max')  # Max price filter
        preco_min = request.POST.get('preco_min')  # Min price filter
        area_max = request.POST.get('area_max')  # Max area filter
        area_min = request.POST.get('area_min') 
        garagem = request.POST.get('garagem_estacionamento')

        filters = {}
        if tipologia:  # Apply filter only if tipologia is provided
            filters['tipologia'] = tipologia
        if tipoImovel:  # Apply filter only if tipoImovel is provided
            filters['tipo_de_imovel'] = tipoImovel
        if endereco:
            filters['morada'] = endereco
        if cod_postal:
            filters['codigo_postal'] = cod_postal
        if preco:
            filters['preco_pedido'] = preco
        if area:
            filters['area_m2'] = area
        if garagem:
            filters['garagem_estacionamento'] = garagem     

        if preco_min:
            filters['preco_pedido__gte'] = preco_min  # Price greater than or equal to min
        if preco_max:
            filters['preco_pedido__lte'] = preco_max  # Price less than or equal to max
        if area_min:
            filters['area_m2__gte'] = area_min  # Area greater than or equal to min
        if area_max:
            filters['area_m2__lte'] = area_max  # Area less than or equal to max 

        if filters:  # Apply the filter only if there's at least one condition
            imoveis = Imovel.objects.filter(**filters)

    return render(request, 'radarimovel/consulta.html', {'imoveis': imoveis})



def inserir(request):

    proprietarios = Proprietario.objects.all()
    localizacao = Localizacao.objects.all()


    if request.method == 'POST':
        nifproprietario = request.POST.get('proprietarios')
        # id_localizacao = request.POST.get('id_localizacao')

        try:
            proprietario_obj = Proprietario.objects.get(nifproprietario=nifproprietario)
            # localizacao_obj = Localizacao.objects.get(id_localizacao=id_localizacao)
        except Proprietario.DoesNotExist:
            print('Proprietario não encontrado')
    

        # idlocalizacao = request.POST['IDLocalizacao']
        tipo_de_imovel = request.POST['Tipo_de_imovel']
        tipologia = request.POST['Tipologia']
        morada = request.POST['Morada']
        codigo_postal = request.POST['Codigo_postal']
        preco_pedido = request.POST['Preco_pedido']
        fotos = None
        area_m2 = request.POST['area_m2']
        garagem_estacionamento = request.POST['garagem_estacionamento']

        novoImovel = Imovel(nifproprietario=proprietario_obj, tipo_de_imovel=tipo_de_imovel, tipologia=tipologia, morada=morada, codigo_postal=codigo_postal, preco_pedido=preco_pedido, fotos=fotos, area_m2=area_m2,garagem_estacionamento=garagem_estacionamento)

        novoImovel.save()

    return render(request, 'radarimovel/inserir.html', {'proprietarios': proprietarios, 'localizacao': localizacao})