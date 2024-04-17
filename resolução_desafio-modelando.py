from abc import ABC, abstractmethod,abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(Conta)

    def adiconar_contas(self, conta):
        self.contas.append(Conta)     
           

class PessoaFisica(Cliente):
    def __init__(nome, data_aniversario, cpf, endereco): 
        super().__init__(endereco)
        self.nome = nome
        self.data_aniversario = data_aniversario
        self.cpf = cpf


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
            saldo = self.saldo
            excedeu_saldo = valor > saldo
            
            if excedeu_saldo:
                print("\n@@@Operação falhou! Você não tem saldo suficiente.@@@")
            
            elif valor > 0:
                self.saldo -= valor
                print("\n=== Saque realizado com sucesso! ===")
                return True

            else:
                print("@@@ Operação falhou! O valor informado é inválido. @@@")
            
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@  Operação falhou! O valor informado é inválido. @@@")        
        return False


class contaCorrente(Conta):
    def __init__(self, saldo, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
            numero_saques = len(transacao for transacao in self.historico.transacoes if transacao["tipo" == Saque.__name__])
            saldo = self.saldo

            excedeu_limite = valor > self.limite
            excedeu_saques = numero_saques >= self.limite_saques

            excedeu_saldo = valor > saldo
            
            if excedeu_limite:
                print("\n@@@Operação falhou! O valor do saque excedeu o limite.@@@")
            
            elif excedeu_saques:
                print("\n@@@Operação falhou! Número máximo de saques excedido.@@@")
                
            else:
                return super().sacar(valor)
            
            return False


    def __str__(self):

        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self.trasacoes = []

    @property
    def trandacoes(self):
        return self.transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%y %H:%M%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __innit__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
