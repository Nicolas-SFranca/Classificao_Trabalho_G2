class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, genero):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.genero = genero  

class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def __init__(self):
        self.raiz = None

    def inserir(self, jogo):
        if self.raiz is None:
            self.raiz = NoJogo(jogo)
        else:
            self._inserir_recursivo(self.raiz, jogo)

    def _inserir_recursivo(self, no, jogo):
        if jogo.preco < no.jogo.preco:
            if no.esquerda is None:
                no.esquerda = NoJogo(jogo)
            else:
                self._inserir_recursivo(no.esquerda, jogo)
        else:
            if no.direita is None:
                no.direita = NoJogo(jogo)
            else:
                self._inserir_recursivo(no.direita, jogo)

    def buscar_por_preco(self, preco):
        return self._buscar_por_preco_recursivo(self.raiz, preco)

    def _buscar_por_preco_recursivo(self, no, preco):
        if no is None:
            return None
        if no.jogo.preco == preco:
            return no.jogo
        elif preco < no.jogo.preco:
            return self._buscar_por_preco_recursivo(no.esquerda, preco)
        else:
            return self._buscar_por_preco_recursivo(no.direita, preco)

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        jogos_encontrados = []
        self._busca_por_faixa_recursiva(self.raiz, preco_minimo, preco_maximo, jogos_encontrados)
        return jogos_encontrados

    def _busca_por_faixa_recursiva(self, no, preco_minimo, preco_maximo, jogos_encontrados):
        if no is not None:
            if preco_minimo < no.jogo.preco:
                self._busca_por_faixa_recursiva(no.esquerda, preco_minimo, preco_maximo, jogos_encontrados)
            if preco_minimo <= no.jogo.preco <= preco_maximo:
                jogos_encontrados.append(no.jogo)
            if preco_maximo > no.jogo.preco:
                self._busca_por_faixa_recursiva(no.direita, preco_minimo, preco_maximo, jogos_encontrados)

class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}

    def adicionar_jogo(self, jogo):
        if jogo.genero not in self.genero_para_jogos:
            self.genero_para_jogos[jogo.genero] = []
        self.genero_para_jogos[jogo.genero].append(jogo.jogo_id)

    def obter_jogos(self, genero):
        return self.genero_para_jogos.get(genero, [])

class MotorBuscaJogos:
    def __init__(self):
        self.catalogo_jogos = ArvoreJogos()
        self.generos = HashGeneros()

    def adicionar_jogo(self, jogo):
        self.catalogo_jogos.inserir(jogo)
        self.generos.adicionar_jogo(jogo)

    def buscar_jogo_por_preco(self, preco):
        return self.catalogo_jogos.buscar_por_preco(preco)

    def buscar_jogos_por_faixa_preco(self, preco_minimo, preco_maximo):
        return self.catalogo_jogos.busca_por_faixa_preco(preco_minimo, preco_maximo)

    def buscar_jogos_por_genero(self, genero):
        jogo_ids = self.generos.obter_jogos(genero)
        jogos_encontrados = []
        for jogo_id in jogo_ids:
            jogo = next((jogo for jogo in jogos_gamepass if jogo.jogo_id == jogo_id), None)
            if jogo:
                jogos_encontrados.append(jogo)
        return jogos_encontrados
# Criando uma instância do motor de busca de jogos
motor_busca = MotorBuscaJogos()

# Lista de jogos do Game Pass
jogos_gamepass = [
    Jogo(jogo_id=1, titulo="Halo Infinite", desenvolvedor="343 Industries", preco=109.99, genero="Ação"),
    Jogo(jogo_id=2, titulo="Forza Horizon 5", desenvolvedor="Playground Games", preco=79.99, genero="Corrida"),
    Jogo(jogo_id=3, titulo="Gears 5", desenvolvedor="The Coalition", preco=80.00, genero="Ação"),
    Jogo(jogo_id=4, titulo="Sea of Thieves", desenvolvedor="Rare", preco=60.00, genero="Aventura"),
    Jogo(jogo_id=5, titulo="Microsoft Flight Simulator", desenvolvedor="Asobo Studio", preco=49.99, genero="Simulação"),
    Jogo(jogo_id=6, titulo="Starfield", desenvolvedor="Bethesda", preco=200.00, genero="RPG"),
    Jogo(jogo_id=7, titulo="Psychonauts 2", desenvolvedor="Double Fine", preco=69.99, genero="Aventura"),
    Jogo(jogo_id=8, titulo="Age of Empires IV", desenvolvedor="Relic Entertainment", preco=89.99, genero="Estratégia"),
    Jogo(jogo_id=9, titulo="The Ascent", desenvolvedor="Neon Giant", preco=120.00, genero="Ação"),
    Jogo(jogo_id=10, titulo="Diablo IV", desenvolvedor="Blizzard Entertainment", preco=150.00, genero="RPG"),
    Jogo(jogo_id=11, titulo="FIFA 22", desenvolvedor="EA Sports", preco=200.00, genero="Esporte"),
    Jogo(jogo_id=12, titulo="NBA 2K22", desenvolvedor="Visual Concepts", preco=200.00, genero="Esporte"),

]


for jogo in jogos_gamepass:
    motor_busca.adicionar_jogo(jogo)


jogos_acao = motor_busca.buscar_jogos_por_genero("Ação")
for jogo in jogos_acao:
    print(f"{jogo.titulo} - {jogo.preco} REAIS")

def menu():
    while True:
        print("\nMenu:")
        print("\n==============================")
        print("      Xbox Game Pass Menu      ")
        print("==============================")
        print("1. Buscar jogo por preço")
        print("2. Buscar jogos por faixa de preço")
        print("3. Buscar jogos por gênero")
        print("4. Mostrar todos os jogos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            preco = float(input("Digite o preço do jogo: "))
            jogo = motor_busca.buscar_jogo_por_preco(preco)
            if jogo:
                print(f"Jogo encontrado: {jogo.titulo} - {jogo.preco} REAIS")
            else:
                print("Nenhum jogo encontrado com esse preço.")
        elif opcao == "2":
            preco_minimo = float(input("Digite o preço mínimo: "))
            preco_maximo = float(input("Digite o preço máximo: "))
            jogos = motor_busca.buscar_jogos_por_faixa_preco(preco_minimo, preco_maximo)
            if jogos:
                print("Jogos encontrados:")
                for jogo in jogos:
                    print(f"{jogo.titulo} - {jogo.preco} REAIS")
            else:
                print("Nenhum jogo encontrado nessa faixa de preço.")
        elif opcao == "3":
            genero = input("Digite o gênero do jogo: ")
            jogos_encontrados = motor_busca.buscar_jogos_por_genero(genero)
            if jogos_encontrados:
                print("Jogos encontrados:")
                for jogo in jogos_encontrados:
                    print(f"{jogo.titulo} - {jogo.preco} REAIS")
            else:
                print("Nenhum jogo encontrado para esse gênero.")
        elif opcao == "4":
            print("Todos os jogos:")
            for jogo in jogos_gamepass:
                print(f"{jogo.titulo} - {jogo.preco} REAIS")
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
