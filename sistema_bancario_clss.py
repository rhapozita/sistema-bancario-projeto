from abc import ABC, abstractmethod

class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0
        self.numero = numero
        self.AGENCIA = '0001'
        self.cliente = cliente
        self.historico = Historico()
    
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
    def AGENCIA(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        self.valor = valor
        
        if valor > saldo:
            print('Opa! Operação falhou! \nVocê não tem saldo suficiente.')

        elif valor > limite:
            print('Opa! Operação falhou! \nO valor do saque excede o limite.')

        elif numero_saques >= LIMITE_SAQUES:
            print('Opa! Operação falhou! \nNúmero máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque realizado de: R$ {valor:.2f}\n'
            numero_saques += 1
            print(extrato)
            return True

        else:
            print('Opa! Operação falhou! \nO valor informado é inválido.')
            return False
           
    def depositar(self, valor):
        self.valor = valor

        if valor > 0:
            saldo += valor
            extrato += f'Depósito realizado de: R$ {valor:.2f}\n'
            print(extrato)
            return True

        else:
            print('Operação falhou! O valor informado é inválido.')
            return False
        
class ContaCorrente(Conta):
    def __init__(self, limite = 500, limite_saque = 3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == 'Saque']
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    def adicionar_conta(self, conta):
        self.conta.append(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Historico:
    def adicionar_transacao(self):
        self.transacao = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor
            }
        )

class Transacao(ABC):
    @property
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
