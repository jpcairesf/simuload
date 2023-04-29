# SIMULOAD
Simuload é um projeto para criação de um simulador de curvas de cargas elétricas em uma linha de distribuição.

## Instalação Executável
Em breve

## Instalação Código Fonte
### Windows
Execute os seguintes comandos
```python
    >> python -m venv .venv
    >> .venv/Scripts/activate
    (.venv)>> pip install -e .
```

### Linux
Execute os seguintes comandos
```python
    >> python -m venv .venv
    >> source .venv/bin/activate
    (.venv)>> pip install -e .
```

## Uso
Executar o main no ambiente virtual
```python
    (.venv)>> python main.py
```
### Entidades
O Simuload faz uso de quatro entidades.
1. Equipamento: Representa os equipamentos que compõem uma carga.
2. Carga: Representa um estabelecimento consumidor. Pode ser uma casa, um galpão, um mercado, iluminação pública, entre outros.
3. Curva: Representa a distribuição temporal do consumo de várias cargas. Representa o consumo numa região atendida por um transformador.
4. Transformador: Representa o fornecimento na curva característica de um transformador que atende uma região.

### Janela Principal

Simuload é uma plataforma na qual é possível utilizar os equipamentos e cargas pré-definidos no banco de dados ou customizar novas opções. Dentre os registros pré-definidos, estão os equipamentos com uso diário mapeados pelo PPH 2019 do Procel e potência mapeadas pela norma SM04.14-01.001 12ª edição da Neoenergia. Na tela prinicpal é possível visualizar os comandos de criação de componentes ou simulações de curvas.


![Janela Principal](docs/readme-imgs/janela-prinicpal.png)

### Adicionando Equipamentos
Adicionar, editar ou excluir um equipamento são tarefas possíveis no menu equipamentos. No campo Uso Diário, podemos definir a distribuição de uso em 24 horas do equipamento seguindo o padrão de números entre 0 e 1 nos colchetes. Exemplo: [1 1 1 1 1 1 1 1 1 1 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.2 0.2 0.2 0.2].


![Janelas Equipamentos](docs/readme-imgs/janela-equipamentos.png)

### Criando Cargas
No menu cargas é possível juntar diversas configurações de equipamentos para construir a carga desejada. 


![Janelas Cargas](docs/readme-imgs/janela-cargas.png)

### Criando Transformadores
No menu transformadores é possível criar e configurar transformadores com a mesma estrutura de distribuição de 24 horas dos equipamentos no campo Demanda.

### Criando Curvas
Na tela prinicpal é possível editar as configurações para a simulação da curva e criar curvas baseadas nas cargas existentes.


![Janelas Config](docs/readme-imgs/janela-curvas-config.png)
![Janelas Curva](docs/readme-imgs/janela-curvas.png)


### Resultados
Ao clicar em simular curva, uma janela com p gráfico da curva de carga é mostrado. É possível salvar a imagem do gráfico ou exportar um .CSV na janela principal.


![Janela Resultado](docs/readme-imgs/janela-resultado.png)

## License

[MIT](https://github.com/caleo-hub/simuload/blob/main/LICENSE)
