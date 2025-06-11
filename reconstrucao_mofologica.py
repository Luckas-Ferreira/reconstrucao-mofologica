"""
Seminário: Reconstrução Morfológica em Níveis de Cinza

Este script demonstra duas aplicações da reconstrução morfológica:
1. Preenchimento de buracos em objetos.
2. Eliminação de pequenos objetos (abertura por reconstrução).

Agora com suporte a imagens externas!
"""

# --- Importação das Bibliotecas Necessárias ---
import numpy as np  # Biblioteca para manipulação de arrays numéricos (as imagens são matrizes).
import matplotlib.pyplot as plt  # Biblioteca para criar visualizações e plots das imagens.
from skimage.morphology import reconstruction, disk, erosion  # Funções específicas de morfologia matemática.
from skimage import io, img_as_ubyte  # Funções para carregar imagens e converter seus tipos de dados.
import os  # Biblioteca para interagir com o sistema operacional, usada aqui para verificar se um arquivo existe.


def plot_comparison(original, marker, reconstructed, title=""):
    """
    Função auxiliar para plotar a imagem original, a marcadora e a reconstruída lado a lado.
    """
    # Cria uma figura e um conjunto de subplots (1 linha, 3 colunas).
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    # 'Aplaina' o array de eixos para facilitar o acesso.
    ax = axes.ravel()

    # --- Primeiro Subplot: Imagem Original ---
    ax[0].imshow(original, cmap='gray')  # Mostra a imagem original em tons de cinza.
    ax[0].set_title("Imagem Original")   # Define o título do subplot.
    ax[0].axis('off')                    # Remove os eixos (números) da visualização.

    # --- Segundo Subplot: Imagem Marcadora ---
    ax[1].imshow(marker, cmap='gray')    # Mostra a imagem marcadora.
    ax[1].set_title("Imagem Marcadora (Marker)") # Define o título.
    ax[1].axis('off')                    # Remove os eixos.

    # --- Terceiro Subplot: Imagem Reconstruída ---
    ax[2].imshow(reconstructed, cmap='gray') # Mostra o resultado final.
    ax[2].set_title("Imagem Reconstruída") # Define o título.
    ax[2].axis('off')                    # Remove os eixos.

    fig.suptitle(title, fontsize=16)     # Adiciona um título principal para a figura inteira.
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajusta o layout para evitar sobreposição.
    plt.show()                           # Exibe a janela com os plots.

def carregar_imagem(caminho):
    """
    Carrega uma imagem do disco, a converte para escala de cinza e para o formato 8-bits.
    """
    # Verifica se o caminho do arquivo fornecido realmente existe.
    if not os.path.exists(caminho):
        # Se não existir, lança um erro informando que o arquivo não foi encontrado.
        raise FileNotFoundError(f"Imagem não encontrada: {caminho}")
    
    # Carrega a imagem. 'as_gray=True' garante que ela será convertida para tons de cinza.
    imagem = io.imread(caminho, as_gray=True)
    # Converte a imagem para o tipo 'unsigned byte' (valores de 0 a 255), um padrão comum.
    imagem = img_as_ubyte(imagem)
    return imagem

def exemplo_preenchimento_buracos(imagem):
    """
    Usa reconstrução por dilatação para preencher buracos em objetos.
    Este método é eficaz para preencher regiões escuras cercadas por pixels claros.
    """
    # A imagem marcadora (marker) é criada a partir de uma cópia da original.
    marker = np.copy(imagem)
    # Zera todos os pixels internos, deixando apenas uma borda de 1 pixel.
    # A reconstrução começará a partir dessa borda.
    marker[1:-1, 1:-1] = 0
    
    # Executa a reconstrução por dilatação. A `marker` é expandida, mas é limitada
    # pela `imagem` original (que atua como máscara), preenchendo as áreas internas.
    reconstruida = reconstruction(marker, imagem, method='dilation')
    
    # Mostra os resultados.
    plot_comparison(imagem, marker, reconstruida, title="Preenchimento de Buracos")

def exemplo_abertura_por_reconstrucao(imagem):
    """
    Remove pequenos objetos brilhantes, preservando a forma dos objetos maiores.
    Isso é superior a uma abertura morfológica clássica, pois não deforma os objetos grandes.
    """
    # 1. Cria um elemento estruturante (SE) em forma de disco. O raio (aqui, 5)
    #    determina o tamanho dos objetos a serem removidos.
    se = disk(5)
    
    # 2. Cria a imagem marcadora (marker) erodindo a imagem original. A erosão remove
    #    objetos menores que o elemento estruturante.
    marker = erosion(imagem, se)
    
    # 3. Executa a reconstrução. A partir da `marker` erodida, os objetos restantes
    #    são "recrescidos" até seu tamanho original, pois são limitados pela `imagem` (máscara).
    reconstruida = reconstruction(marker, imagem, method='dilation')
    
    # Mostra os resultados.
    plot_comparison(imagem, marker, reconstruida, title="Abertura por Reconstrução")

# ---------- Bloco de Execução Principal ----------
# Este código só roda quando o script é executado diretamente.
if __name__ == "__main__":
    # Pede ao usuário para digitar o nome do arquivo da imagem. '.strip()' remove espaços em branco.
    caminho = input("Digite o nome do arquivo da imagem (ex: 'moedas.png'): ").strip()
    
    # Usa um bloco 'try...except' para lidar com possíveis erros (como arquivo não encontrado).
    try:
        # Tenta carregar a imagem, assumindo que ela está em uma subpasta chamada 'imagens'.
        img = carregar_imagem('imagens/' + caminho)
        
        # Executa o primeiro exemplo com a imagem carregada.
        print("\nExecutando exemplo 1: Preenchimento de buracos")
        exemplo_preenchimento_buracos(img)

        # Executa o segundo exemplo com a mesma imagem.
        print("\nExecutando exemplo 2: Abertura por reconstrução (remoção de objetos pequenos)")
        exemplo_abertura_por_reconstrucao(img)

    # Se ocorrer qualquer erro no bloco 'try', o programa executa este bloco.
    except Exception as e:
        # Imprime uma mensagem de erro amigável para o usuário.
        print(f"Ocorreu um erro: {e}")