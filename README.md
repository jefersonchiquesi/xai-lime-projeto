# 🧠 Decifrando a Caixa Preta: Tornando Modelos de IA Explicáveis com LIME

Este repositório apresenta um projeto acadêmico que explora os fundamentos da **Inteligência Artificial Explicável (XAI)**, com foco na aplicação prática da biblioteca **LIME** para tornar mais compreensíveis os resultados de um modelo preditivo de crédito bancário.

## 👤 Autor

**Jeferson Chiquesi**  
Estudante de Gestão da Tecnologia da Informação – UniFECAF  
GitHub: [@jefersonchiquesi](https://github.com/jefersonchiquesi)

---

## 🎯 Objetivo

Tornar um modelo de classificação de crédito mais transparente, revelando **quais características influenciam as decisões** do algoritmo. A técnica utilizada é o **LIME (Local Interpretable Model-agnostic Explanations)**, capaz de gerar explicações locais mesmo em modelos considerados "caixas-pretas".

---

## 🗂️ Conteúdo do Projeto

- `notebook/lime_credit_analysis.ipynb`: Jupyter Notebook com todo o pipeline, do pré-processamento à explicação via LIME.
- `outputs/`: Contém imagens com explicações geradas pelo LIME.
- `requirements.txt`: Dependências do projeto.
- `README.md`: Este documento.

---

## 🧪 Tecnologias e Bibliotecas

- Python 3.11+
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- LIME
- Jupyter Notebook

---

## 📊 Dataset Utilizado

- **German Credit Data** – Disponível na UCI Machine Learning Repository.
- Atributos: status de crédito, idade, histórico bancário, valor do empréstimo, entre outros.
- Classes: `Bom` ou `Ruim`.

---

## 🧠 Modelo Preditivo

- **Algoritmo:** Random Forest
- **Tarefa:** Classificação binária (crédito bom ou ruim)
- **Métrica Avaliada:** Acurácia

---

## 🔍 Explicações com LIME

A biblioteca LIME foi utilizada para explicar **instâncias individuais** do conjunto de teste. Cada explicação mostra:

- As **principais variáveis** que influenciaram a predição;
- O **peso e direção** de cada variável na decisão;
- Representação gráfica de forma intuitiva.

---

## 💡 Resultados e Insights

- O LIME permitiu visualizar o impacto de variáveis como `duration`, `credit_amount`, `age`, e `checking_status` na decisão do modelo.
- Evidenciou que mesmo modelos complexos podem ser explicados de forma **transparente e acessível**.
- Explicações ajudam a criar **confiança no modelo**, essencial em setores sensíveis como o financeiro.

---

## ⚠️ Limitações

- O LIME gera explicações **locais**, ou seja, válidas apenas para instâncias específicas.
- Pode ser sensível a ruído ou atributos altamente correlacionados.
- Não substitui uma análise global do modelo.

---

## 🔐 Ética, Segurança e Governança

- O projeto ressalta a importância da **explicabilidade em modelos de decisão automatizada**, especialmente em contextos com alto impacto social.
- Contribui para um uso mais responsável da IA.

---

## 🧭 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/jefersonchiquesi/xai-lime-projeto.git
   cd xai-lime-projeto
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txtExecute o Jupyter Notebook:

bash
Copiar
Editar
jupyter notebook


🤝 Contribuições
Este projeto foi desenvolvido como parte da disciplina de Explainable AI e está aberto para sugestões e melhorias.

