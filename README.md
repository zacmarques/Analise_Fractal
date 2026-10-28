**README.md**

---

# **Analise_fractal.py**  
**Descrição:**  
Este script calcula a **dimensão fractal** de um grafo (como um *sona*) usando o método de **contagem de caixas (box-counting)**. Ele gera um painel visual com a imagem analisada, a fórmula matemática aplicada e o gráfico de regressão linear que determina a dimensão fractal.

---

## **Requisitos**  
Instale as dependências abaixo usando `pip`:

```bash
pip install numpy matplotlib pillow
```

---

## **Como usar**  
1. Coloque a imagem que deseja analisar na mesma pasta do script.  
   Exemplo: `imagem_analise.png`  
2. Edite a variável `nome_da_sua_imagem` no final do script com o nome da sua imagem.  
3. Execute o script com Python 3.

```python
# Exemplo de uso (não é necessário alterar esta parte)
nome_da_sua_imagem = 'imagem_analise.png'
analisador_para_banca(nome_da_sua_imagem)
```

---

## **O que o script faz**  
1. **Preparação da imagem:**  
   - Converte a imagem para preto e branco (grayscale).  
   - Cria uma versão binária (pixels < 128 são considerados "negros").  

2. **Contagem de caixas:**  
   - Divide a imagem em caixas de tamanhos crescentes (2^n).  
   - Conta o número de caixas que intersectam a imagem.  

3. **Cálculo da dimensão fractal:**  
   - Aplica regressão linear no gráfico log-log (log(N) vs. log(1/ε)).  
   - A inclinação da reta é a **dimensão fractal (D)**.  

4. **Visualização:**  
   - Exibe um painel com:  
     - A imagem original.  
     - A fórmula do método de contagem de caixas.  
     - O gráfico de regressão linear e a dimensão fractal calculada.  

---

## **Exemplo de Saída**  
- **Painel esquerdo:**  
  - Imagem analisada com a fórmula:  
    $$
    D = \lim_{\epsilon \to 0} \frac{\log N(\epsilon)}{\log(1/\epsilon)}
    $$  
  - Dimensão fractal calculada (ex.: `D = 1.2345`).  

- **Painel direito:**  
  - Gráfico log-log com a reta de ajuste e a dimensão fractal.  

---

## **Notas Importantes**  
- A imagem deve ser em **formato PNG** e **escuro em tons de cinza** (preferencialmente com elementos geométricos claros).  
- O script ajusta automaticamente a margem inferior da janela para exibir a fórmula completa.  
- Para uso em trabalhos acadêmicos, cite a metodologia de **contagem de caixas** e a fórmula aplicada.

---

## **Contribuições**  
Se você encontrar erros ou quiser melhorias, entre em contato ou abra uma issue!  

--- 

**Autor:** Isaac Marques de Souza Garcia, mestrando pelo Programa de Pós-Graduação em História Ibérica da Universidade Federal de Alfenas (UNIFAL-MG).    

--- 

*Pronto para copiar e colar em um arquivo `README.md`!* 📦

Autor: Isaac Marques de Souza Garcia, mestrando pelo Programa de Pós-Graduação em História Ibérica da Universidade Federal de Alfenas (UNIFAL-MG).

