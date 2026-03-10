from flask import Blueprint, request                  # DE flask IMPORTAR Blueprint e request:
                                                      # - Blueprint: usado para organizar as rotas do Flask em módulos separados
                                                      # - request: objeto que contém os dados enviados na requisição HTTP

from controllers.teclado_controllers import create_teclado # DE controllers.carro_controllers IMPORTAR create_carro:
                                                      # função que cria um novo carro no banco (controller)

teclado_routes = Blueprint('teclado_routes', __name__)    # Cria um Blueprint chamado "carro_routes" (identificador),
                                                      # associado ao módulo atual (__name__), para registrar rotas do carro

@teclado_routes.route('/Tv', methods=['POST'])       # Define a rota "/Carro" que aceita apenas requisições HTTP POST
def teclado_post():                                    # Função que será executada quando houver POST em "/Carro"
    teclado_data = request.json                         # Lê o corpo da requisição no formato JSON e armazena em carro_data
    return create_teclado(request.json)                 # Chama a função create_carro (controller) passando os dados recebidos
