from models.teclado_models import Teclado    # DE models.carro_models IMPORTAR Carro: importa a classe/modelo Carro (representa a tabela/registro de carro)
from db import db                        # DE db IMPORTAR db: importa a instância do SQLAlchemy usada para acessar o banco (sessão, etc.)
import json                              # IMPORTAR json: módulo para serializar/deserializar dados JSON
from flask import make_response          # DE flask IMPORTAR make_response: função que cria uma resposta HTTP personalizada

def create_teclado(teclado_data):            # DEFINIR create_carro(carro_data): define a função que recebe os dados do carro (provém da requisição)
    novo_teclado = Teclado(                  # criar novo objeto Carro usando o construtor do modelo
        modelo=teclado_data['modelo'],     # pega o campo 'modelo' do dicionário carro_data e atribui ao atributo modelo do novo objeto
        categoria=teclado_data['marca'],       # pega o campo 'marca' de carro_data e atribui ao atributo marca do novo objeto
        preco=teclado_data['ano']            # pega o campo 'ano' de carro_data e atribui ao atributo ano do novo objeto
    )
    db.session.add(novo_teclado)           # session.add(novo_carro): adiciona o novo objeto à sessão do SQLAlchemy (prepara para inserção)
    db.session.commit()                  # session.commit(): confirma e persiste as alterações no banco (insere o novo registro)
    response = make_response(            # cria um objeto Response do Flask contendo o corpo (aqui: o JSON gerado abaixo)
        json.dumps({                      # json.dumps(...): converte o dicionário Python para uma string JSON
            'mensagem': 'Teclado cadastrado com sucesso.',  # mensagem de confirmação incluída no JSON de resposta
            'teclado': novo_teclado.json()   # inclui os dados do carro chamando novo_carro.json() — método do modelo que retorna um dict
        }, sort_keys=False)               # sort_keys=False: não ordena as chaves do dicionário quando serializa para JSON
    )
    response.headers['content-Type'] = 'application/json'  # define o cabeçalho HTTP Content-Type como application/json (informa que o corpo é JSON)
    return response                      # retorna o objeto Response para quem chamou a função (ex.: rota Flask)

