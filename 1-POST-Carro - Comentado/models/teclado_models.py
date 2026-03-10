from db import db                       # DE db IMPORTAR db: importa a instância do SQLAlchemy que gerencia o banco de dados

class Teclado(db.Model):                   # Define a classe Carro como um modelo do SQLAlchemy (herda de db.Model)
    __tablename__ = 'tvs'              # Nome da tabela no banco de dados será "carros"

    id = db.Column(db.Integer, primary_key=True)          # Coluna "id": número inteiro, chave primária (identificador único)
    modelo = db.Column(db.String(80), nullable=False)     # Coluna "modelo": texto com limite de 80 caracteres, não pode ser nula
    categoria = db.Column(db.String(80), nullable=False)      # Coluna "marca": texto com limite de 80 caracteres, não pode ser nula
    preco = db.Column(db.Integer, nullable=False)           # Coluna "ano": número inteiro, não pode ser nulo

    def json(self):                                        # Define o método json() que retorna os dados do carro como dicionário
        return {
            'id': self.id,            # Retorna o ID do carro
            'modelo': self.modelo,    # Retorna o modelo do carro
            'marca': self.marca,      # Retorna a marca do carro
            'ano': self.ano           # Retorna o ano do carro
        }
