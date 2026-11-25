# usuario.py — a classe Usuario: quem é a pessoa, a senha e o que ela pode

from usuarios.papeis import permissoes_do_papel


class Usuario:
    # Construtor: guarda os dados da pessoa; começa como "ativo"
    def _init_(self, matricula, nome, senha, papeis, supervisor=None):
        self.matricula = matricula
        self.nome = nome
        self.senha = senha
        self.papeis = papeis
        self.supervisor = supervisor  # matrícula de quem aprova
        self.situacao = "ativo"

    # True se a senha digitada é a certa
    def conferir_senha(self, senha):
        return self.senha == senha

    # True se algum dos cargos da pessoa permite essa ação
    def pode(self, acao):
        for papel in self.papeis:
            if acao in permissoes_do_papel(papel):
                return True
        return False