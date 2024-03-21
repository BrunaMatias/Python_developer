from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Criar engine e sessão do banco de dados
engine = create_engine('sqlite:///banco.db')
Session = sessionmaker(bind=engine)
session = Session()

# Definir a base declarativa
Base = declarative_base()

# Definir classes para as tabelas
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String)

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(DECIMAL)
    cliente = relationship("Cliente", back_populates="contas")

Cliente.contas = relationship("Conta", order_by=Conta.id, back_populates="cliente")

# Criar as tabelas
Base.metadata.create_all(engine)

# Inserir dados de exemplo
cliente1 = Cliente(nome='João', cpf='123456789', endereco='Rua A')
cliente2 = Cliente(nome='Maria', cpf='987654321', endereco='Rua B')

conta1 = Conta(tipo='Corrente', agencia='001', num=123, saldo=1000, cliente=cliente1)
conta2 = Conta(tipo='Poupança', agencia='002', num=456, saldo=500, cliente=cliente2)

session.add_all([cliente1, cliente2, conta1, conta2])
session.commit()

# Executar métodos de recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print("Nome:", cliente.nome)
    print("CPF:", cliente.cpf)
    print("Endereço:", cliente.endereco)
    print("Contas:")
    for conta in cliente.contas:
        print("- Tipo:", conta.tipo)
        print("- Agência:", conta.agencia)
        print("- Número:", conta.num)
        print("- Saldo:", conta.saldo)
    print()


from pymongo import MongoClient

# Conectar ao MongoDB Atlas
client = MongoClient("mongodb+srv://pymongo:<password>@cluster0.d88sdsz.mongodb.net/?retryWrites=true&w=majority")
db = client["banco_nosql"]
colecao = db["bank"]

# Inserir documentos
documentos = [
    {
        "cliente_id": 1,
        "nome": "João",
        "cpf": "123456789",
        "endereço": "Rua A",
        "contas": [
            {"tipo": "Corrente", "agencia": "001", "num": 123, "saldo": 1000},
            {"tipo": "Poupança", "agencia": "002", "num": 456, "saldo": 500}
        ]
    },
    {
        "cliente_id": 2,
        "nome": "Maria",
        "cpf": "987654321",
        "endereço": "Rua B",
        "contas": [
            {"tipo": "Corrente", "agencia": "003", "num": 789, "saldo": 2000}
        ]
    }
]

colecao.insert_many(documentos)

# Recuperação de informações
resultado = colecao.find_one({"nome": "João"})
print("Nome:", resultado["nome"])
print("CPF:", resultado["cpf"])
print("Endereço:", resultado["endereço"])
print("Contas:")
for conta in resultado["contas"]:
    print("- Tipo:", conta["tipo"])
    print("- Agência:", conta["agencia"])
    print("- Número:", conta["num"])
    print("- Saldo:", conta["saldo"])
