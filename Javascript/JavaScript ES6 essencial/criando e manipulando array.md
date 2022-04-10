#Aula: Criando e Manipulando Array


##Tipos de criação de Array >>>>>>>>>>>>>>>>>>


###Array.of --------------------------------------------------->


Cria uma nova instância de array a apartir do num de parâmetros informados.

<script>
	
const arr = Array.of(1, 2, 3);

</script>


###Array --------------------------------------------------------->


Cria uma nova instância de array de acordo com os parâmetros informados.

<script>

const arr = Array(3);
// [empty x 3]

const arr2 = Array(3, 2);
// [3. 2]

</script>


###Array.from ------------------------------------------------->


Cria uma nova instância de array a apartir de um parâmetro 
array-like ou iterable object
    // array-like : Ex: nodeList com querySelector no html

<script>

const divs = document.querySelectorAll('div');
// a const 'divs' retorna um nodeList.
    // As funções de Array ficam indisponíveis
const arr = Array.from(divs);
// o 'arr' retorna todas as divs dentro de uma list(Array).

</script>


##Inserir e remover Elementos >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


###Push (adiciona no final) ---------------------------------------->


Add um ou mais elementos no final do Array e retorna o tamando do novo Array

<script>
	
const arr = ['melon', 'apple', 'apricot'];
const arrLength = arr.push('orange');

console.log(arrLength);
// ['melon', 'apple', 'apricot', 'orange'];

console.log(arr);
// ['melon', 'apple', 'apricot'];

</script>


###Pop (remove o ultimo) ----------------------------------------->


Remove o ultimo elemento de um Array e retorna o elemento removido

<script>
	
const arr = ['melon', 'apple', 'apricot'];
const removedItem = arr.pop();

console.log(removedItem);
// 'apricot'

console.log(arr);
// ['melon', 'apple'];

</script>


###Unshift (Adiciona no início) -------------------------------------->


Add um ou mais element no inicio do Array e retorna o tamanho do novo Array

<script>
	
const arr = ['melon', 'apple', 'apricot'];
const arrLenght = arr.unshift('orange');

console.log(arrLenght);
// 4

console.log(arr);
// ['orange', 'melon', 'apple', 'apricot'];

</script>


###shift (remove no inicio) ------------------------------------------->


remove o primeiro element do Array e retorna o tamanho do novo Array

<script>
	
const arr = ['orange', 'melon', 'apple', 'apricot'];
const removedItem = arr.shift();

console.log(removedItem);
// 'orange'

console.log(arr);
// ['melon', 'apple', 'apricot'];

</script>


###concat ------------------------------------------------------>


Concatena um ou mais arrays retornando um novo array

<script>
	
const arr =[1, 2, 3];
const arr2 = [4, 5, 6];

const novoArr = arr.concat(arr2);

console.log(arr);
// (3) [1, 2, 3]

console.log(arr2);
// (3) [4, 5, 6]

console.log(novoArr);
// (6) [1, 2, 3, 4, 5, 6]

</script>


###Slice ---------------------------------------------------------->


Retorna um novo array "fatiando" o array de acordo com início e fim

<script>
	
const arr = [1, 2, 3, 4, 5];

arr.slice(0, 2);
// [1, 2]

arr.slice(2);
// [3, 4, 5]

arr.slice(-1);
// [5]

arr.slice(-3);
// [3, 4, 5]

// OBS: O array original não é modificado.

</script>


###Splice --------------------------------------------------------->


Altera um array adicionando novos elementos enquanto remove elementos antigo

<script>
	
const arr = [1, 2, 3, 4, 5];

const retorno = arr.splice(2);

console.log(retorno);
// [3, 4, 5]
console.log(arr);
// [1, 2]

const retorno2 = arr.splice(0, 0, 'first');

console.log(retorno2);
// []
console.log(arr);
// ["first", 1, 2]

const retorno3 = arr.splice(1, 1 "second");

console.log(retorno3);
// [1]
console.log(arr);
// ["first", "second", 2]


//OBS: O splice modifica o Array original.


</script>