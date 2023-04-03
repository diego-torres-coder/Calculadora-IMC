# Calculadora de IMC

Em construção...

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
