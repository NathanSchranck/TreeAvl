class AVL:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class TreeAVL:
    def inserir(self, raiz, chave):
        if not raiz:
            return AVL(chave)
        
        if chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        else:
            raiz.direita = self.inserir(raiz.direita, chave)
        
        raiz.altura = 1 + max(self.getAltura(raiz.esquerda), self.getAltura(raiz.direita))
        
        return self.balancear(raiz)

    def excluir(self, raiz, chave):
        if not raiz:
            return raiz
        
        if chave < raiz.chave:
            raiz.esquerda = self.excluir(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.excluir(raiz.direita, chave)
        else:
            if not raiz.esquerda:
                temp = raiz.direita
                raiz = None
                return temp
            elif not raiz.direita:
                temp = raiz.esquerda
                raiz = None
                return temp
            
            temp = self.getMinimoValorNo(raiz.direita)
            raiz.chave = temp.chave
            raiz.direita = self.excluir(raiz.direita, temp.chave)
        
        raiz.altura = 1 + max(self.getAltura(raiz.esquerda), self.getAltura(raiz.direita))
        
        return self.balancear(raiz)

    def pesquisar(self, raiz, chave):
        if not raiz:
            return False
        
        if chave == raiz.chave:
            return True
        elif chave < raiz.chave:
            return self.pesquisar(raiz.esquerda, chave)
        else:
            return self.pesquisar(raiz.direita, chave)

    def getAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    def balancear(self, raiz):
        balance = self.getBalance(raiz)
        
        if balance > 1:
            if self.getBalance(raiz.esquerda) < 0:
                raiz.esquerda = self.rotacaoEsquerda(raiz.esquerda)
            return self.rotacaoDireita(raiz)
        
        if balance < -1:
            if self.getBalance(raiz.direita) > 0:
                raiz.direita = self.rotacaoDireita(raiz.direita)
            return self.rotacaoEsquerda(raiz)
        
        return raiz

    def getBalance(self, raiz):
        if not raiz:
            return 0
        return self.getAltura(raiz.esquerda) - self.getAltura(raiz.direita)

    def rotacaoEsquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        
        y.esquerda = z
        z.direita = T2
        
        z.altura = 1 + max(self.getAltura(z.esquerda), self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda), self.getAltura(y.direita))
        
        return y

    def rotacaoDireita(self, y):
        x = y.esquerda
        T2 = x.direita
        
        x.direita = y
        y.esquerda = T2
        
        y.altura = 1 + max(self.getAltura(y.esquerda), self.getAltura(y.direita))
        x.altura = 1 + max(self.getAltura(x.esquerda), self.getAltura(x.direita))
        
        return x

    def getMinimoValorNo(self, raiz):
        if raiz is None or raiz.esquerda is None:
            return raiz
        return self.getMinimoValorNo(raiz.esquerda)

def imprimaArvore(raiz):
    if raiz:
        imprimaArvore(raiz.esquerda)
        print(raiz.chave, end=" ")
        imprimaArvore(raiz.direita)

def menu():
    arvore = TreeAVL()
    raiz = None

    while True:
        print("\nMenu:")
        print("1. Inserir valor")
        print("2. Pesquisar valor")
        print("3. Remover valor")
        print("4. Imprimir árvore em ordem")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            valor = int(input("Digite o valor a ser inserido: "))
            raiz = arvore.inserir(raiz, valor)
            print(f"{valor} inserido com sucesso.")
        elif escolha == "2":
            valor = int(input("Digite o valor a ser pesquisado: "))
            if arvore.pesquisar(raiz, valor):
                print(f"{valor} encontrado na árvore.")
            else:
                print(f"{valor} não encontrado na árvore.")
        elif escolha == "3":
            valor = int(input("Digite o valor a ser removido: "))
            if arvore.pesquisar(raiz, valor):
                raiz = arvore.excluir(raiz, valor)
                print(f"{valor} removido com sucesso.")
            else:
                print(f"{valor} não encontrado na árvore.")
        elif escolha == "4":
            print("Árvore em ordem:", end=" ")
            imprimaArvore(raiz)
            print()
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

