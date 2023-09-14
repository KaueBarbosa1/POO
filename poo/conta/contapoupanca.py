from poo.conta.conta import Conta

class ContaPoupanca(Conta):

    def __init__(self, numero):
        super().__init__(numero)
        pass
    def render_juros(self, taxa):
        self.creditar(self.get_saldo() * taxa )
        pass