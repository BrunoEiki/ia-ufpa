import random


class Ambiente:
    '''
    Matriz 3 x 3 em que cada quadradinho pode estar limpo ou sujo 
    '''

    def __init__(self):
        self.posicao_agente = [1, 1]
        self.estados = {(0, 0): "limpo",
                        (0, 1): "limpo",
                        (0, 2): "limpo",
                        (1, 0): "limpo",
                        (1, 1): "limpo",
                        (1, 2): "limpo",
                        (2, 0): "limpo",
                        (2, 1): "limpo",
                        (2, 2): "limpo"}
        random.seed(12)
        for i in range(3):
            for j in range(3):
                sujo = random.randint(0, 1)
                if sujo == 0:
                    self.estados[(i, j)] = "sujo"

    def parada(self) -> bool:
        for i in self.estados.values():
            if i == "sujo":
                return False
        return True

    # ======= PERCEPÇÃO =========
    def percepcao(self):
        return (tuple(self.posicao_agente), self.estados[tuple(self.posicao_agente)])

    def mostrarAmbiente(self):
        c = 65
        tamanhoMatriz = 3

        # First row
        print("  ", end='')
        for j in range(tamanhoMatriz):
            print(f"| {j+1} ", end='')
        print("| ")
        print((tamanhoMatriz*4+4)*"-")

        # Other rows
        for i in range(tamanhoMatriz):
            print(f"{chr(c+i)} ", end='')
            for j in range(tamanhoMatriz):
                if (self.estados[(i, j)] == "sujo"):
                    print("| ~ ", end='')
                elif (self.posicao_agente == [i, j]):
                    print("| O ", end='')
                elif (self.estados[(i, j)] == "limpo"):
                    print("|   ", end='')

            print("| ")
            print((tamanhoMatriz*4+4)*"-")


class Aspirador:
    '''
    Agente responsavel por vasculhar o ambiente e limpar os quadradinhos
    '''

    def __init__(self) -> None:
        self.tabela_acao = {
            ((0, 0), "sujo"): "limpa",
            ((0, 0), "limpo"): "baixo",
            ((0, 1), "sujo"): "limpa",
            ((0, 1), "limpo"): "esquerda",
            ((0, 2), "sujo"): "limpa",
            ((0, 2), "limpo"): "esquerda",
            ((1, 0), "sujo"): "limpa",
            ((1, 0), "limpo"): "baixo",
            ((1, 1), "sujo"): "limpa",
            ((1, 1), "limpo"): "cima",
            ((1, 2), "sujo"): "limpa",
            ((1, 2), "limpo"): "cima",
            ((2, 0), "sujo"): "limpa",
            ((2, 0), "limpo"): "direita",
            ((2, 1), "sujo"): "limpa",
            ((2, 1), "limpo"): "direita",
            ((2, 2), "sujo"): "limpa",
            ((2, 2), "limpo"): "cima",
        }

    def funcao_transicao(self, ambient):
        acao = self.tabela_acao[ambient.percepcao()]

        if acao == "cima":
            ambient.posicao_agente[0] -= 1
            print(f"Movido para cima: {ambient.posicao_agente}")

        if acao == "direita":
            ambient.posicao_agente[1] += 1
            print(f"Movido para direita: {ambient.posicao_agente}")

        if acao == "esquerda":
            ambient.posicao_agente[1] -= 1
            print(f"Movido para esquerda: {ambient.posicao_agente}")

        if acao == "baixo":
            ambient.posicao_agente[0] += 1
            print(f"Movido para baixo: {ambient.posicao_agente}")

        if acao == "limpa":
            print("O ambiente da posição",
                  ambient.posicao_agente, "foi limpo!")
            ambient.estados[tuple(ambient.posicao_agente)] = "limpo"
            print("Bom trabalho, aspirador")


def avaliar(ambient):
    for i in ambient.estados.values():
        if i == "sujo":
            return False
    return True


if __name__ == "__main__":
    pontuacao = 0
    aspirador = Aspirador()
    ambiente = Ambiente()

    while not avaliar(ambiente):
        print("\n==========================")
        aspirador.funcao_transicao(ambiente)
        ambiente.mostrarAmbiente()
        pontuacao += 1
    print(f"Desempenho: {pontuacao}")
