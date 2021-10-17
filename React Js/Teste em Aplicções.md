#Teste em Aplicções


##Testando elementos --------------------------------------------------------------->

<script>

describe('Componente principal', () => {
// describe - descreve o teste e envelopa os demais elementos, servindo como um titulo.

  describe('Quando eu abro o app do banco', () => {
    test('o nome é exibido', () => {
// O test ou it, recebe um titulo de marcação é inicia a function de teste.

      render(<App />);
// render - renderiza o conteúdo (ex:HTML), assim é possivel testa-lo.
  
      expect(screen.getByText('ByteBank')).toBeInTheDocument();
// expect - inspeciona o elemento especificado.
// toBeInTheDocument() - verifica se o elemento inspecionado está dento do documento (no caso <App/>).
// screen - na linha 14, foi usado screen, ele serve para fazer a leitura do conteúdo renderiazado na linha 11.
    })
}
</script>


##Testando Funções ---------------------------------------------------------------->


<script>

import App, { calcularNovoSaldo } from './app';
// importamos a função 'calcularNovoSaldo' que está no 'App'.

describe('Quando eu realizo uma transação', () => {
    it('que é um saque, o valor vai diminuir', () => {
      const valores = {
        transacao: 'saque',
        valor: 50
      }
// Esse 'valores' é apenas um dado que essa função exige, isso altera de acordo com a função.

      const novoSaldo = calcularNovoSaldo(valores, 150)

      expect(novoSaldo).toBe(100);
// Não usamos o 'screen' pois estamos testando um função, não necessário 'render' e 'screen'.
// Quando estamos testando uma função precisamos importar-la do arquivo que está sendo testado.
    });
  })
</script>


##Teste Unitários em Funções ------------------------------------------------------>


<script>
	
it("a função calcula o valor quadrado de um número", () =>{
	const resultado = calculoQuadrado(2)
	const resultadoB = calculoQuadrado(4)

	expect (resultado).toBe(4)
	expect (resultadoB).toBe(16)
// Consiste em realizar mais de um teste. evitando possíveis erros em caso diferentes.
})

</script>


##Função Pura --------------------------------------------------------------------->


Sempre que executamos a função passando os mesmos parâmetros, o resultado será o mesmo. 
Ela não depende de nenhum fator externo ou faz alterações globais na aplicação. 
Temos a previsão do resultado para poder escrever um teste unitário.

<script>
// Exemplo:
function calcularDesconto(valorCompra, descontoPercentual) {
    const valorFinal = valorCompra * (1 - descontoPercentual);
    return valorFinal;
}

// Um exmplo contrário:

function atualizarCarrinho(valorCompra) {
    const { saldoCarrinho } = this.state;
    const novoSaldoCarrinho = saldoCarrinho + valorCompra;
    return novoSaldoCarrinho;
// O valor retornado pela função vai variar de acordo com o saldoCarrinho que está no state. 
// Se executarmos 2 vezes a função, com o mesmo valorCompra, não temos garantia que resultado será o mesmo.
}

</script>


##FireEvent ------------------------------------------------------------------------>


<script>

import { render, screen, fireEvent } from '@testing-library/react';
	
it('que é um saque, a transação deve ser realizada', () => {
  render(<App />);

  const saldo = screen.getByText('R$ 1000');
  const transacao =  screen.getByLabelText('Saque');
  const valor = screen.getByTestId('valor');
  const botaoTransacao = screen.getByText('Realizar operação');

  expect(saldo.textContent).toBe('R$ 1000')

  fireEvent.click(transacao, { target: { value: 'saque'}});
// O fireEvent deve ser importado.
// fireEvent.click simula o click do usuario sob o elemento em questão.
  fireEvent.change(valor, { target: { value:  10 }});
  fireEvent.click(botaoTransacao);

// --------------------------------------------------->>>>>>

usamos o {target: { value : 'saque'}}, isso é semelhante ao  event.target.value = 'saque'

// --------------------------------------------------->>>>>>

// A sequencia de comandos do fireEvent simula a interação do usuario com a aplicação.

  expect(saldo.textContent).toBe('R$ 990');
// Verificamos o novo valor esperado.
})

</script>

[**Doc Sobre fireEvent**](https://testing-library.com/docs/dom-testing-library/api-events/);
[**Event-Suport**](https://github.com/testing-library/dom-testing-library/blob/main/src/event-map.js);
[**MDN - Event Reference**](https://developer.mozilla.org/en-US/docs/Web/Events).

##Simulando o retorno de uma API --------------------------------------------->

<script>

import { render, screen } from '@testing-library/react';
import api from './api';
import App from './App';

jest.mock('./api')
// jest.mock - faz uma simulação da API (não acessa exatamente).

describe('Requisições para API', () => {
  it('Exibir lista de transações através da API', async () => {
// usamos o async para habilitar a função assincrona.
    api.listaTransacoes.mockResolvedValue([
// mockResolvedValue - retorna o valor da promise.
      {
        "valor": "10",
        "transacao": "saque",
        "data": "10/08/2020",
        "id": 1
      },
      {
        "transacao": "deposito",
        "valor": "20",
        "data": "26/09/2020",
        "id": 2
      }
    ]);
// O conteúdo que esperamos que a API restorne.

    render(<App />);

    expect(await screen.findByText('saque')).toBeInTheDocument();
// findByText - encontra um elemento/txt dentro do documento.
// Usamos o await screen.findByText() para espera o elemento surgi no documento.
// é posivel usar o await porque declaramos a functin como async.

    expect(screen.getByTestId('transacoes').children.length).toBe(2)
// children - se refere aos elemento filhos.
// children.lenght - captura a quantidade de elementos contido no elemento alvo.

  });
})

</script>


##getBy ou findBy? -------------------------------------------------------------------->


A query *findBy* retorna uma promise que é completada quando o elemento é encontrado, dessa forma nosso teste espera até que o componente esteja disponível.


##Simulando uma Função ---------------------------------------------------------------->


<script>

//...
	
  it('Chama a função de realizar transação, quando o botão é clicado', () => {
    const funcaoRealizarTransação = jest.fn()
// just.fn() - simula uma função (apenas para testes).
  // Essa função não recebe parametro, nem retorna valores.

    render(<Conta saldo={1000} realizarTransacao={funcaoRealizarTransação} />)

    fireEvent.click(screen.getByText('Realizar operação'));

    expect(funcaoRealizarTransação).toHaveBeenCalled()
// toHaveBeenCalled avisa se o elemento foi chamado.
// Também podemos testar quantas vezes ela foi chamada utilizando | expect(mockFuncao).toHaveBeenCalledTimes(quantidade).

  })
})

</script>