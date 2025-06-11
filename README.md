
# 🧪 Seminário: Reconstrução Morfológica em Níveis de Cinza

Este projeto demonstra a aplicação de **reconstrução morfológica** utilizando imagens em níveis de cinza. O foco está em duas aplicações clássicas:

1. ✅ Preenchimento de buracos em objetos.  
2. ✅ Eliminação de pequenos objetos (abertura por reconstrução).

O código permite a **utilização de imagens externas**, facilitando a experimentação com exemplos reais ou sintéticos, conforme solicitado na atividade.

---

## 📚 Fundamentos Teóricos

Antes de utilizar este código, é importante revisar os seguintes conceitos de morfologia matemática:

- Erosão e Dilatação  
- Abertura e Fechamento  
- Transformada Hit-or-Miss  
- Reconstrução Morfológica (por dilatação condicional)  

Esses conceitos são essenciais para compreender o comportamento das operações morfológicas aplicadas em imagens digitais.

---

## 📦 Dependências

Instale as bibliotecas necessárias com:

```bash
pip install numpy matplotlib scikit-image
```

---

## ▶️ Como Usar

1. Coloque suas imagens `.png`, `.jpg` ou similares em uma pasta imagens do projeto.
2. Execute o script no terminal ou em um ambiente como Jupyter Notebook:

```bash
python3 reconstrucao_mofologica.py
```

---

## 📂 Estrutura Sugerida de Pastas

```
projeto/
├── imagens/
│   └── sua_imagem.png
├── reconstrucao.py
└── README.md
```

---

## 📸 Exemplo

O script exibirá comparações entre:
- Imagem original
- Imagem marcadora
- Imagem reconstruída

Ideal para visualização dos efeitos da reconstrução morfológica.

---
