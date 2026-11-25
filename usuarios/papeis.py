# papeis.py — define os cargos e o que cada um pode fazer

PERMISSOES = {
    "solicitante": ["abrir_pedido"],
    "supervisor": ["aprovar_pedido"],
    "almoxarifado": ["andamento_pedido", "cancelar_pedido"],
    "admin": ["mudar_papeis"],
}

# Devolve a lista de cargos que existem
def papeis_validos():
    return list(PERMISSOES.keys())

# Devolve o que um cargo pode fazer (lista vazia se o cargo não existe)
def permissoes_do_papel(papel):
    return PERMISSOES.get(papel, [])