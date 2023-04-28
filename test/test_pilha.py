from estrutura_dados.pilha import Pilha

def test_adicionar():
    """
    Método responsável por testar o método adicionar da classe Pilha.

    Cenário:
        Aqui vou testar o caminho feliz, ou seja, o caso onde o método
        adicionar deve funcionar corretamente.
    """

    # Setup
    pilha = Pilha(10)

    # Executar
    pilha.adicionar(1)
    pilha.adicionar(2)
    pilha.adicionar(3)

    # Verificar
    assert pilha.tamanho_atual_pilha() == 3