#criar os clientes
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")
        
#def ver_filme(self, filme):
    
#class Produtos:
    
cliente = Cliente("Ricieri", "ricieri.silva@gmail.com", "basic")
print("Cliente: ", cliente.nome)
print("Email: ",cliente.email)
print("Plano: ", cliente.plano)

# no botão de upgrade
cliente.mudar_plano("premium")
print("Mudança de plano para: ",cliente.plano)