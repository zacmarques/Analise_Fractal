import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def analisador_para_banca(caminho_imagem):
    if not os.path.exists(caminho_imagem):
        print(f"ERRO: A imagem '{caminho_imagem}' não foi encontrada na pasta!")
        return

    # 1. Preparação da Imagem
    img = Image.open(caminho_imagem).convert('L')
    img_np = np.array(img)
    binary_img = img_np < 128
    
    p = min(binary_img.shape)
    n = int(np.floor(np.log2(p)))
    tamanhos_caixa = 2**np.arange(n, 1, -1)
    contagens = []
    
    # 2. Processo de Contagem de Caixas
    for tamanho in tamanhos_caixa:
        count = 0
        for i in range(0, binary_img.shape[0], tamanho):
            for j in range(0, binary_img.shape[1], tamanho):
                if np.any(binary_img[i:i+tamanho, j:j+tamanho]):
                    count += 1
        contagens.append(count)
        
    # 3. Regressão Linear (O Cálculo da Fórmula)
    log_tamanhos = np.log(1.0 / tamanhos_caixa) # log(1/epsilon)
    log_contagens = np.log(contagens)          # log(N)
    
    # y = mx + c (onde m é a nossa Dimensão Fractal D)
    coeffs = np.polyfit(log_tamanhos, log_contagens, 1)
    D = coeffs[0]
    
    # 4. Geração do Painel Visual para a Banca
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.canvas.manager.set_window_title('Resultado de Dimensão Fractal - Box Counting')

    # Painel Esquerdo: Imagem e Fórmulas
    ax1.imshow(img_np, cmap='gray')
    ax1.set_title("Grafo Analisado", fontsize=16, fontweight='bold')
    ax1.axis('off')
    
    # Texto Explicativo com a Fórmula de Box-Counting
    texto_formula = (
        "Fórmula do Box-Counting utilizada:\n"
        r"$D = \lim_{\epsilon \to 0} \frac{\log N(\epsilon)}{\log(1/\epsilon)}$" + "\n\n"
        "Onde:\n"
        r"$N(\epsilon)$ = N° de caixas interceptadas" + "\n"
        r"$\epsilon$ = Tamanho da caixa" + "\n\n"
        f"Dimensão Fractal Encontrada: D = {D:.4f}"
    )
    
    # Coloca a caixa de texto embaixo da imagem
    ax1.text(0.5, -0.15, texto_formula, transform=ax1.transAxes, 
             fontsize=12, ha='center', va='top', 
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0f0f0', edgecolor='black'))

    # Painel Direito: O Gráfico
    ax2.plot(log_tamanhos, log_contagens, 'bo-', markerfacecolor='red', markersize=8, label="Dados extraídos da imagem")
    
    # Linha de tendência (A regressão linear em si)
    linha_tendencia = coeffs[0] * log_tamanhos + coeffs[1]
    ax2.plot(log_tamanhos, linha_tendencia, 'k--', alpha=0.7, label=f'Reta de Ajuste: D = {D:.4f}')
    
    ax2.set_xlabel(r'$\log(1/\epsilon)$ (Inverso do Tamanho da Caixa)', fontsize=12)
    ax2.set_ylabel(r'$\log(N)$ (Número de Caixas)', fontsize=12)
    ax2.set_title("Regressão Linear (Log-Log)", fontsize=16, fontweight='bold')
    ax2.grid(True, which="both", ls="--", alpha=0.5)
    ax2.legend(fontsize=12)

    # 5. Ajustes de layout da janela
    plt.tight_layout()
    # Margem inferior fixada em 0.364 conforme solicitado
    plt.subplots_adjust(bottom=0.364) 
    plt.show()

# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================
# Coloque o nome da imagem do seu Sona/Grafo aqui:
nome_da_sua_imagem = 'imagem_analise.png' 
analisador_para_banca(nome_da_sua_imagem)
