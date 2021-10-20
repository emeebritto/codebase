// Aula_1__meuPrimeiroPrograma: ----------------------------


console.log("Meu Primeiro programa: trabalhando com variáveis");

const idade = 26;
    // 'const' é um tipo de variavel estática (não muda).

console.log("idade");
console.log(idade);
console.log(idade + 2);
console.log(idade - 2);
console.log(idade / 2);
    // 'console.log()' exibe o resultado (do code) no console.
    // No exemplo acima, estamos efetuando calculos com a constante 'idade'.

const idadeSomada = idade + 2;
console.log(idadeSomada);


// Aula_2__trabalhandoComVariaveis: --------------------------


//Console.log("Trabalhando com variáveis");
console.log("Trabalhando com variáveis");
//JS é case sensitive

const idade = 29;
const nome = "Ricardo";


//NÃO FAÇA:

//mes = "Janeiro";
    // Smpre declare o tipo da vriavel (let, const, var).
    // O correto da linha 34, seria - const mes = "Janeiro".


// Aula_3__operacoesAritmeticas: -----------------------------


console.log("Operações Aritiméticas");

console.log(2 + 2);
console.log(10 + 8 * 2);
console.log((10 + 8) * 2);

console.log("ano" + 2020);
console.log("2" + "2");


// Aula_4__conversaoDetipos: ----------------------------------


console.log("Conversão de Tipos");

console.log("ano" + 2020);
console.log("2" + "2");
console.log(parseInt("2") + parseInt("2"));
    // O 'parseInt' declara o conteúdo como número.

console.log("7" / "2");
console.log("Ricardo" / "2"); //Not a Number

console.log(6.5);
    // O ponto ( . ) é usado em calculo de numeros float.
console.log(6,5);
    // A vírgula ( , ) da espaço entre os elementos.


// Aula_5__atribuicaoVariaveis: ---------------------------------


console.log("Trabalhando com atribuição de variáveis");
const idade = 29;
const primeiroNome = "Ricardo";
const sobrenome = "Bugan";

//console.log(nome + " " + sobrenome)
console.log(primeiroNome, sobrenome)
console.log(`Meu nome é ${primeiroNome} ${sobrenome}`);
    // Para usarmos o valor de uma veriavel dentro de uma string
     // Utilizamos o ${} dentro adicionamos a variavel.
    // Existe uma função semelhante no python.

let contador = 0
    // Diferente do 'const', o 'let' permite alteração de valores.
contador = contador + 1
    // Se o contador tivesse sido clarado como 'const'
     // Teriamos um erro ao tentar trocar o valor.
const nomeCompleto = primeiroNome + sobrenome;
console.log(nomeCompleto);
nomeCompleto = 2;

    // DICA: evite usar (somente onde for possivel) variaveis que 
     //permite mudança de valor (var, let)
      // em casos de bugs no code, pode dificultar a resolução.


// Aula_6__listas: -----------------------------------------------


console.log(`Trabalhando com listas`);
/*const salvador = `Salvador`;
const saoPaulo = `São Paulo`;
const rioDeJaneiro = `Rio de Janeiro`;*/
    // rascunho de um outro método de lista..

let new = 2;
    // A palavra 'new' é reservada ao js (não podemos usar como variável).

const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);
    // 'new Array()' declara a variável como lista.
    // Mesmo a 'listaDeDestinos' sendo 'const' é 
      // possivel adicionar e remover elementos.

listaDeDestinos.push(`Curitiba`) // adicionando um item na lista
console.log("Destinos possíveis:");
/*console.log(salvador, saoPaulo, rioDeJaneiro)*/
    // rascunho de um outro método de lista..
console.log(listaDeDestinos);

listaDeDestinos.splice(1,1);
    // 'splice' remover items da lista.
    // splice(posição, quantidade).
    // OBS: a contagem da lista inicia apartir de 0.
console.log(listaDeDestinos);


console.log(listaDeDestinos[1], listaDeDestinos[0]);
    // Lista[posição], usamos para ver um conteúdo especifico 
     // dentro da lista.


// Aula_7__condicionais: ---------------------------------------


console.log(`Trabalhando com condicionais`);
const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);

const idadeComprador = 18;
const estaAcompanhada = false;
const temPassagemComprada = true;

console.log("Destinos possíveis:");
console.log(listaDeDestinos);

// if (idadeComprador >= 18) {
//     console.log("Comprador maior de idade");
//     listaDeDestinos.splice(1, 1); //removendo item
// } else if (estaAcompanhada == true) {
//     console.log("Comprador está acompanhado");
//     listaDeDestinos.splice(1, 1); //removendo item
// } else {
//     console.log("Não é maior de Idade e não posso vender");
// }

if (idadeComprador >= 18 || estaAcompanhada == true) {
	    // O '||' é o mesmo que 'ou'.
	     // condição1 ou condição2.
    console.log("Boa Viagem!!");
    listaDeDestinos.splice(2, 1); //removendo item
} else {
    console.log("Não é maior de Idade e não posso vender");
}

console.log("Embarque: \n\n")
    // '\n' pula linha (deixando uma linha vazia.)
if(idadeComprador >= 18 && temPassagemComprada){
	    // O '&&' é o mesmo que 'e'.
	     // condição1 e condição2.
    console.log("Boa viagem");
}else{
    console.log("Você não pode embarcar");
}


console.log(listaDeDestinos);

// console.log(idadeComprador > 18);
// console.log(idadeComprador < 18);
// console.log(idadeComprador <= 18);
// console.log(idadeComprador >= 18);
// console.log(idadeComprador == 18);


// Aula_8__loops: ------------------------------------------------


console.log(`\nTrabalhando com condicionais`);
const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);

const idadeComprador = 18;
const estaAcompanhada = false;
let temPassagemComprada = false;
const destino = "Curitiba";

console.log("\n Destinos possíveis:");
console.log(listaDeDestinos);

const podeComprar  = idadeComprador >= 18 || estaAcompanhada == true;

let contador = 0;
let destinoExiste = false;
while(contador < 3 ){
    if(listaDeDestinos[contador] == destino){
        destinoExiste = true;
        break;
    }
    contador += 1;
}

console.log("Destino exite: ", destinoExiste);

if(podeComprar && destinoExiste){
    console.log("Boa Viagem");
}else{
    console.log("Desculpe tivemos um erro!");
}

// Forma alternativa da linha 217:

for(let i  = 0 ; i < 3 ; i++){
    if(listaDeDestinos[i] == destino){
        destinoExiste = true;
    }
   
}