import pandas as pd

# Carregando os dados
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
column_names = [
    "StatusConta", "Duracao", "HistoricoCredito", "Proposito", "ValorCredito",
    "Poupanca", "TempoEmprego", "TaxaParcelas", "StatusPessoa", "OutrosFiadores",
    "ResidenciaAtual", "Propriedade", "Idade", "OutrosPlanos", "Moradia",
    "CreditoExistente", "Emprego", "NumeroPessoas", "Telefone", "TrabalhadorEstrangeiro",
    "Classificacao"
]

df = pd.read_csv(url, sep=' ', header=None, names=column_names)

# Reclassificando target para binário (1: bom, 0: ruim)
df['Classificacao'] = df['Classificacao'].map({1: 1, 2: 0})

from sklearn.preprocessing import LabelEncoder

# Aplicando LabelEncoder em variáveis categóricas
for col in df.select_dtypes(include='object').columns:
    df[col] = LabelEncoder().fit_transform(df[col])

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X = df.drop("Classificacao", axis=1)
y = df["Classificacao"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

print(classification_report(y_test, modelo.predict(X_test)))


import lime
import lime.lime_tabular

explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=X_train.values,
    feature_names=X.columns,
    class_names=["Ruim", "Bom"],
    mode="classification"
)

# Escolha de um cliente para explicar
idx = 5
exp = explainer.explain_instance(X_test.iloc[idx].values, modelo.predict_proba, num_features=10)

# Visualizando explicação
from IPython.display import display, HTML
display(HTML(exp.as_html()))

# Salvar explicação em arquivo HTML (visualização interativa)
exp.save_to_file('explicacao_cliente5.html')

# Opcional: salvar explicação como imagem (para usar em README, apresentações)
fig = exp.as_pyplot_figure()
fig.savefig('explicacao_cliente5.png')
# Exibir a figura
import matplotlib.pyplot as plt 
plt.show()
