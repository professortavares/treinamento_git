
class Pilha:
    """
    Classe que representa uma estrutura de dados
    do tipo pilha (FiLo).
    """

    def __init__(self, tamanho_maximo:int):
        """
        Construtor da classe Pilha.

        Parametros:
        -----------
        tamanho_maximo:
            Tamanho maximo da pilha.
        """
        self.tamanho_maximo = tamanho_maximo
        self.tamanho_atual = 0
        self.dados = []

    def adicionar(self, elemento:int):
        """
        Adiciona um elemento no topo da pilha.

        Parametros:
        -----------
        elemento:
            Elemento a ser adicionado.
        """

        # aqui o elemento que está sendo adicionado
        # é colocado no topo da pilha
        self.dados.append(elemento)
        self.tamanho_atual += 1

    def remover(self):
        """
        Remove o elemento do topo da pilha.
        """
        pass

    def tamanho_atual_pilha(self)->int:
        """
        Retorna o tamanho atual da pilha.

        Retorno:
        --------
        int:
            Tamanho atual da pilha.
        """
        return self.tamanho_atual

    def tamanho_maximo(self) -> int:
        """
        Retorna o tamanho maximo da pilha.

        Retorno:
        --------
        int:
            Tamanho maximo da pilha.
        """
        pass