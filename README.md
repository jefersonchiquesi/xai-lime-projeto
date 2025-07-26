🧠 Decifrando a Caixa Preta: Tornando Modelos de IA Explicáveis com LIME
📌 Contextualização do Problema e Objetivos
No cenário atual de transformação digital, modelos preditivos são amplamente utilizados para decisões críticas, como concessão de crédito. Apesar de sua eficácia, muitos desses modelos operam como "caixas pretas", dificultando a compreensão de como uma decisão foi tomada.

Este projeto tem como objetivo aplicar técnicas de Explainable Artificial Intelligence (XAI) utilizando a biblioteca LIME para explicar as decisões de um modelo de classificação binária no contexto de análise de crédito. O foco é gerar explicações locais, mostrando quais atributos mais influenciaram a decisão para um determinado cliente.

🤖 Modelo Preditivo Utilizado
Foi desenvolvido um modelo de aprendizado de máquina supervisionado para classificação de risco de crédito. As principais etapas foram:

Pré-processamento do dataset (Statlog German Credit Data ou Lending Club Loan Data)

Divisão entre conjunto de treino e teste

Treinamento com o modelo: RandomForestClassifier (ou o modelo que você usou)

Avaliação de performance com métricas como acurácia, precisão e matriz de confusão

🧪 Explicações Geradas pelo LIME
Utilizamos o LIME (Local Interpretable Model-agnostic Explanations) para explicar predições individuais do modelo.

As explicações mostram quais atributos impactaram positivamente ou negativamente a decisão.

Cada cliente recebe uma explicação visual dos principais fatores (ex: renda, histórico de pagamento, idade).

Isso torna o modelo mais transparente e aumenta a confiança de stakeholders como analistas e tomadores de decisão.

Foram geradas explicações como:

Cliente #5: recusa de crédito explicada por alto número de dívidas e curto tempo de emprego.

Cliente #17: aprovação explicada por renda elevada e bom histórico de crédito.

Inclua prints dessas explicações no repositório!

⚠️ Limitações, Importância e Contribuições
Limitações:
O LIME foca em explicações locais, ou seja, cada predição individual tem uma explicação diferente.

Pode apresentar inconsistências se os dados tiverem alta dimensionalidade ou forem ruidosos.

Importância da Interpretabilidade:
Transparência é fundamental em áreas sensíveis como crédito, saúde ou justiça.

Explicações claras ajudam a evitar viés algorítmico e melhoram a confiança nos sistemas de IA.

Contribuições do Projeto:
Demonstração prática do uso de XAI com LIME.

Aumenta a compreensão de como decisões automatizadas são tomadas.

Oferece base para futuras aplicações em sistemas críticos.

🚀 Como Executar o Projeto
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/jefersonchiquesi/xai-lime-projeto.git
cd xai-lime-projeto
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o script principal:

bash
Copiar
Editar
python main.py
