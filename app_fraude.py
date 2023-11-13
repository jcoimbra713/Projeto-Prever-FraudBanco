import pickle
import streamlit as st
import numpy as np

# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva_fraude.pkl', 'rb') 
maquina_preditiva_fraude = pickle.load(pickle_in)

# Essa função é para criação da página web
def main():  
    # Elementos da página web
    # Nesse ponto, você deve personalizar o sistema com sua marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">PROJETO PARA PREVER A PROBABILIDADE DE FRAUDE</h1> 
    <h2 style ="color:white;text-align:center;">SISTEMA PARA PREVER A PROBABILIDADE DE FRAUDE - by João Coimbra </h2> 
    </div> 
    """
      
    # Função do Streamlit que faz o display da página web
    st.markdown(html_temp, unsafe_allow_html=True) 
      
    # As linhas abaixo criam as caixas nas quais o usuário vai inserir os dados da pessoa que deseja prever o diabetes
    Idade = st.number_input("Idade")
    Sexo = st.selectbox('Sexo', ("Feminino", "Masculino"))
    Valor_Renda = st.number_input("Valor Da Renda") 
    UF_Cliente = st.selectbox('Estado', ("AC", "AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT","PA",
    "PB","PE","PI","PR","RJ","RN","RO","RR","RS","SC","SE","SP","TO"))
    Juros = st.number_input("Juros") 
    Prazo_Emprestimo = st.number_input("Prazo De Empréstimo")
    Prazo_Restante = st.number_input("Prazo Restante")  
    VL_Emprestimo = st.number_input("Valor Do Empréstimo") 
    QT_Total_Parcelas_Pagas = st.number_input("Quantidade De Parcelas Pagas")
    QT_Total_Parcelas_Pagas_EmDia = st.number_input("Quantidade De Parcelas Pagas Em Dia")  
    QT_Parcelas_Atraso = st.number_input("Quantidade de Parcelas Atrasadas")
    QT_Total_Parcelas_Pagas_EmAtraso = st.number_input("Quantidade De Parcelas Pagas Em Atrasos") 
    Saldo_Devedor = st.number_input("Saldo Do Devedor") 

    # Quando o usuário clicar no botão "Verificar", a Máquina Preditiva fará seu trabalho
    if st.button("Verificar"): 
        result, probabilidade = prediction(Sexo, Idade, Valor_Renda, UF_Cliente, Juros, Prazo_Emprestimo, Prazo_Restante, VL_Emprestimo,QT_Total_Parcelas_Pagas,
        QT_Total_Parcelas_Pagas_EmDia,QT_Parcelas_Atraso,QT_Total_Parcelas_Pagas_EmAtraso,Saldo_Devedor) 
        st.success(f'Resultado: {result}')
        st.write(f'Probabilidade: {probabilidade:.2f}%')

# Essa função faz a predição usando os dados inseridos pelo usuário
def prediction(Sexo, Idade, Valor_Renda, UF_Cliente, Juros, Prazo_Emprestimo, Prazo_Restante, VL_Emprestimo,QT_Total_Parcelas_Pagas,
        QT_Total_Parcelas_Pagas_EmDia,QT_Parcelas_Atraso,QT_Total_Parcelas_Pagas_EmAtraso,Saldo_Devedor):   
    # Pre-processando a entrada do Usuário    
    if Sexo == "Feminino":
        Sexo = 0
    else:
        Sexo = 1

    UF_Cliente_dict = {
        "AC": 0,
        "AL": 1,
        "AM": 2,
        "AP": 3,
        "BA": 4,
        "CE": 5,
        "DF": 6,
        "ES": 7,
        "GO": 8,
        "MA": 9,
        "MG": 10,
        "MS": 11,
        "MT": 12,
        "PA": 13,
        "PB": 14,
        "PE": 15,
        "PI": 16,
        "PR": 17,
        "RJ": 18,
        "RN": 19,
        "RO": 20,
        "RR": 21,
        "RS": 22,
        "SC": 23,
        "SE": 24,
        "SP": 25,
        "TO": 26,
        "SE": 24
    }
    UF_Cliente = UF_Cliente_dict[UF_Cliente]

    # Fazendo a Predição
    parametro = np.array([[Sexo, Idade, Valor_Renda, UF_Cliente, Juros, Prazo_Emprestimo, Prazo_Restante, VL_Emprestimo,QT_Total_Parcelas_Pagas,
        QT_Total_Parcelas_Pagas_EmDia,QT_Parcelas_Atraso,QT_Total_Parcelas_Pagas_EmAtraso,Saldo_Devedor]])
    fazendo_previsao = maquina_preditiva_fraude.predict(parametro)
    probabilidade = maquina_preditiva_fraude.predict_proba(parametro)[:, 1] * 100

    if (fazendo_previsao == 0).any():
        pred = 'NÃO É FRAUDE'
    else:
        pred = 'É FRAUDE'

    return pred, probabilidade.item()

if __name__ == '__main__':
    main()


