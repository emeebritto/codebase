#iterar, buscar e transformar Elementos

##Iterar elementos >>>>>>>>>>>>>>>>>>>>>>>>>>


## forEach ------------------------------------------------->


Iteração de cada item dentro de um Array

<script>
	
const arr = [1, 2, 3, 4, 5];

arr.forEach((value, index) => {
	console.log(`${index}: ${value}`);
}
</script>


## map ------------------------------------------------------->


Retorna um novo array, de mesmo tamanho, iterando cada item de um array

<script>
	
const arr = [1, 2, 3, 4, 5];

const newArray = arr.map(value => value * 2);

console.log(newArray);
// [2, 4, 6, 8, 10]

</script>


## flat --------------------------------------------------->


retorna um novo array com todos os elementos de um sub-array
concatenados de forma recursiva de acordo com a profundidade
especificada(depth)

<script>
	
const arr = [1, 2, [3, 4]];
const arr2 = [1, 2, [3, [4, 5]]];

const newArray = arr.flat(); // o padrão é 1 (uma camada);
const newArray2 = arr2.flat();

console.log(newArray);
// [1, 2, 3, 4]
console.log(newArray2);
// [1, 2, 3, [4, 5]]

</script>


## flatMap ----------------------------------------------------------->


Retorna um novo array como a função map e executa um flat de profundidade 1

<script>
	
const arr = [1, 2, 3, 4];

arr.flatMap(value => [value * 2]);
// [2, 4, 6, 8]

arr .flatMap(value => [[value * 2]]);
// [[2], [4], [6], [8]]

</script>


## keys ------------------------------------------------------------>

Retorna um Array iterator que contém as chaves para cada element do Array

<script>
	
const arr = [1, 2, 3, 4];

const arrIterator = arr.keys();

arrIterator.next();
// {value: 0, done: false}

arrIterator.next();
// {value: 1, done: false}

arrIterator.next();
// {value: 2, done: false}

arrIterator.next();
// {value: 3, done: true}

</script>


## values ------------------------------------------------------------>

Retorna um Array Iterator que contém os valores para cada elemento do array

<script>
	
const arr = [1, 2, 3, 4];

const arrIterator = arr.values();

arrIterator.next();
// {value: 1, done: false}

arrIterator.next();
// {value: 2, done: false}

arrIterator.next();
// {value: 3, done: false}

arrIterator.next();
// {value: 4, done: true}

</script>


## entries ---------------------------------------------------------->


retorna um Array lterator que contém os pares chaves/valor para cada elemento da array

<script>
	
const arr = [1, 2, 3, 4];

const arrIterator = arr.entries();

arrIterator.next();
// {value: [0, 1], done: false}

arrIterator.next();
// {value: [1, 2], done: false}

arrIterator.next();
// {value: [2, 3], done: false}

arrIterator.next();
// {value: [3, 4], done: true}

</script>


## find ----------------------------------------------------------->


Retorna o primeiro item (encontrado) de um array que satisfaz a condição

<script>
	
const arr = [1, 2, 3, 4];
const firstGreaterThanTwo = arr.find(value => value > 2);

console.log(firstGreaterThanTwo);
// 3

</script>


## findIndex ------------------------------------------------------------>


Retorna o indice do primeiro item de um array que satisfaz a condição

<script>
	
const arr = [1, 2, 3, 4];
const firstIndexGreaterThanTwo = arr.findIndex(value => value > 2);

console.log(firstIndexGreaterThanTwo);
// 2

</script>


## filter ------------------------------------------------------------->

Retorna um novo array com todos os elementos que satisfazem a condição

<script>
	
const arr = [1, 2, 3, 4];
const allValuesGreaterThanTwo = arr.filter(value => value > 2);

console.log(allValuesGreaterThanTwo);
// [3, 4]

</script>


## indexOf ------------------------------------------------------------>


Retorna o 1° índice em que um element pode ser encontrado no Array

<script>
	
const arr = [1, 3, 3, 4, 3];
const firstIndexOfItem = arr.indexOf(3);

console.log(firstIndexOfItem);
// 1

</script>


## lastIndexOf ------------------------------------------------------------>


Retorna o ultimo índice em que um element pode ser encontrado no Array

<script>
	
const arr = [1, 3, 3, 4, 3];
const lastIndexOfItem = arr.lastIndexOf(3);

console.log(lastIndexOfItem);
// 4

</script>


## includes -------------------------------------------------------------->


Retorna um booleano(true / false) verificando se determinado elemento existe no array

<script>
	
const arr = [1, 3, 3, 4, 3];

const hasItemOne = arr.includes(1);
// true

const hasItemTwo = arr.includes(2);
// false

</script>


## some -------------------------------------------------------------------->

Retorna um booleano verificando se pelo menos um item de um array satisfaz a condição

<script>
	
const arr = [1, 3, 3, 4, 3];

const hasSomeEvenNumber = arr.some(value => value % 2 === 0);
// true

</script>


## every ---------------------------------------------------------------------->


Retorna um booleano verificando se todos os itens de um array satisfazem a condição


<script>
	
const arr = [1, 3, 3, 4, 3];

const allEvenNumbers = arr.every(value => value == 10);
// false

</script>


## sort ---------------------------------------------------------------------->


Ordena os elementos de um array de acordo com o condição

<script>
	
const arr = [1, 3, 2, 5, 4];

arr.sort();
// [1, 2, 3, 4, 5]

</script>


## reverse -------------------------------------------------------------------->


inverte os elementos de um array

<script>
	
const arr = [1, 2, 3, 4, 5];

arr.reverse();
// [5, 4, 3, 2, 1]

</script> 


## join --------------------------------------------------------------------->


Junta todos os elementos de um Array, separados por um delimitador e retorna uma string

<script>
	
const arr = [1, 2, 3, 4, 5];

arr.join('-');
// "1-2-3-4-5"

</script>


## reduce ----------------------------------------------------------------->


Retorna um novo tipo de dado iterando cada posição de um array

<script>
	
const arr = [1, 2, 3, 4, 5];

arr.reduce((total, value) => total += value, 0);
// 15

</script>
