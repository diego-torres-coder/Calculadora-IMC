# Calculadora de IMC

Este projeto é uma calcudadora de IMC (Índice de Massa Corpórea) interativa na qual o usuário informa seu peso e sua altura para obter não só seu respectivo IMC mas também a interpretação de sua situação.

Esta aplicação também permite que o usuário carregue um arquivo do Excel com os dados diversos pacientes — nome, peso (kg) e altura (m) — para calcular o IMC e informar a situação de cada um deles. Além disso, o usuário pode baixar um arquivo CSV com os dados calculados.

## Demo

Acesse a aplicação neste link: 
[Calculadora de IMC](https://diego-torres-coder-calculadora-imc-calculadora-imc-4zf5io.streamlit.app/)

### Calculadora de IMC Simples

Esta é uma captura de tela da seção para calcular o IMC de um único usuário:

![Captura de Tela Calculo de IMC Simples](/calculadora-imc-simples.png "Calculadora de IMC Simples")


### Calculadora de IMC para Diversos Usuários

Esta é uma captura de tela da seção para calcular o IMC de diversos usuários:

![Captura de Tela para Calculo de IMC de Diversos Usuários](/calculadora-imc-completa.png "Calculadora de IMC Completa")


## Como Reproduzir este Projeto

Primeiramente, navegue até a pasta em que deseja clonar este projeto. Em seguida, digite o seguinte comando em seu terminal:

```bash
git clone https://github.com/diego-torres-coder/Calculadora-IMC.git
```

Navegue para a pasta recém-criada no passo anterior:

```bash
cd Calculadora-IMC
```

Crie um ambiente `conda` para o projeto:

```bash
conda create -n stenv-imc python=3.10
```

Com o ambiente criado, é hora de ativá-lo:

```bash
conda activate stenv-imc
```

Instale as dependências do projeto:

```bash
pip install numpy openpyxl pandas streamlit
```

Em vez de instalar as dependências com o comando anterior, você pode simplesmente usar o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Para executar o script `main.py`, digite:

```bash
streamlit run main.py
```
