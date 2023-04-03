# Importa a biblioteca streamlit com o apelido st
import streamlit as st

# Importa o pandas com o apelido pd
import pandas as pd

# Título da aplicação
st.title('Calculadora de IMC')

# Seção para definição do que é IMC
st.header('IMC: O que é?')

# Escreve a definição de IMC na interface
st.write('O Índice de Massa Corporal (IMC) é uma medida que relaciona o peso e a altura de uma pessoa.'\
         ' É calculado dividindo o peso da pessoa em quilogramas pela altura da pessoa em metros ao quadrado.'\
        ' O IMC é frequentemente utilizado como uma medida de saúde geral e para determinar se uma pessoa está'\
        'em um peso saudável para sua altura.')

# Seção para calculo do IMC para um único usuário
st.header('Calcule seu IMC')

# Armazena o peso do paciente
peso = st.number_input('Digite seu peso (kg):')

# Armazena a unidade escolhida pelo usuário
unidade_altura = st.radio(
    'Selecione uma unidade para informar sua altura:',
    ('cm (centímetro)', 'm (metro)')
)

# Verifica qual foi a opção escolhida
if unidade_altura.startswith('cm'):
    # Altura informada pelo usuário em centímetros
    altura = st.number_input('Digite sua altura (cm):')
else:
    # Altura informada pelo usuário em metros
    altura = st.number_input('Digite sua altura (m):')


def informar_situacao(imc: float) -> str: 
    '''Informa a situação do paciente de acordo com o valor de seu IMC.'''
    if imc < 16:
        return 'Seu peso está bem abaixo da faixa de peso ideal para sua altura.'
    elif imc >= 16 and imc < 18.5:
        return 'Seu peso está abaixo da faixa de peso ideal para sua altura'
    elif imc >= 18.5 and imc < 25:
        return 'Seu peso está na faixa ideal de peso para sua altura.'
    elif imc >= 25 and imc < 30:
        return 'Seu peso está acima da faixa ideal de peso para sua altura.'
    elif imc >= 30:
        return 'Seu peso está bem acima da faixa de peso ideal para sua altura.'


# Verifica se o usuário preencheu todos os campos
if peso and altura:
    if unidade_altura == 'cm (centímetro)':
        imc = peso / ((altura / 100 ) ** 2)
    elif unidade_altura == 'm (metro)':
        imc = peso / (altura ** 2)

    # Exibe o botão para calcular o IMC
    if st.button('Calcular IMC'):
        st.write('**Resultado:**')

        # Exibe o IMC do usuário
        st.write(f'Seu IMC é {round(imc, 2)}')

        # Chama a função para retornar a situação do usuário
        st.write(informar_situacao(imc))      
else:
    st.error('Preencha todos os campos corretamente.')

# Seção para calcular o IMC para diveros usuários
st.header('Calcule o IMC para Diversas Pessoas')

# Instrução para o usuário carregar um arquivo do Excel
st.write('Calcule o IMC e determine a situação de diversos indivíduos carregando um arquivo'\
         ' do Excel que tenha a seguinte estrutura:')

# Dataframe de exemplo
df_exemplo = pd.DataFrame(
    {'Pacientes': ['Geraldo', 'Maria', 'Diego', 'Karoline', 'Milene'],
     'Peso (kg)': [65, 75, 62, 64, 63],
     'Altura (m)': [1.63, 1.75, 1.72, 1.76, 1.68]
    }
)

# Exibe o dataframe
st.write(df_exemplo)

st.subheader('Carregamento da Planilha')

# Botão para carregar um arquivo do Excel (extensão xlsx)
planilha = st.file_uploader('Selecione um arquivo do Excel:', type='xlsx')


# Verifica se o usuário carregou um arquivo
if planilha:
    try:
        # Carrega a planilha como um dataframe
        df = pd.read_excel(planilha)

        # Cria uma coluna com o IMC para cada paciente
        df['IMC'] = df['Peso (kg)'] / (df['Altura (cm)'] ** 2)

        df['Situação'] = df['IMC'].apply(informar_situacao)

        st.subheader('Dados Processados')

        # Exibe a planilha atualizada
        st.write(df)

        # Exporta o dataframe com um arquivo CSV
        csv = df.to_csv(index=False).encode('utf-8')

        st.subheader('Criação do CSV')

        st.write('Baixe um arquivo CSV a partir destes dados:')

        # Botão para exportar o CSV
        st.download_button(
            label='Baixar CSV',
            data=csv,
            file_name='PacientesAtualizada.csv',
            mime='text/csv'
        )
    except:
        st.error('Ocorreu um erro durante o processamento dos dados.')

else:
    st.warning('Nenhum arquivo foi carregado.')