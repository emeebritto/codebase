// Parametros de cor, brilho e Posição do Personagem Principal.
let corPersoMain = "white";
let brilhoPersoMain = "-5px -5px 35px white";
let positionPersoMain = 38;

// Altera a cor de todos os reflexos.
let corReflexoGeral = "gray";
let brilhoReflexoGeral = "";

//Altera as cores dos reflexos individualmente.
let corReflexoW = corReflexoGeral;
let brilhoReflexoW = brilhoReflexoGeral;

let corReflexoA = corReflexoGeral;
let brilhoReflexoA = brilhoReflexoGeral;

let corReflexoS = corReflexoGeral;
let brilhoReflexoS = brilhoReflexoGeral;

let corReflexoD = corReflexoGeral;
let brilhoReflexoD = brilhoReflexoGeral;


/*---------------------------------------------------------------------*/

//Gerador de caminhos.
var painel = document.querySelector(".painel");
var bottonList = [];
for (var i = 1; i <= 136; i++){
	var botton = document.createElement('color');
	botton.id = i;
	botton.style.color="#242424";
	botton.textContent = i;
	botton.style.width= "79.6px";
	botton.style.height= "79.6px";
	botton.style.backgroundColor= "#060606";
/*	botton.style.opacity= "0%";*/
	botton.style.transition= "600ms";

	bottonList.push(botton);
	painel.appendChild(botton);
}
/*------------------------------------------------------------------------*/

/*let mapa = [2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 22, 23, 24, 25, 26, 38, 39, 40, 41, 42, 43, 56, 57, 58, 59, 60];

for (var i = 0; i < mapa.length; i++){
	var temp = mapa[i];
	bottonList[temp - 1].style.opacity= "100%";

}*/


let lastPosition = 36;

//Configurações iniciais do Personagem Principal.
bottonList[positionPersoMain - 1].style.backgroundColor= corPersoMain;
bottonList[positionPersoMain - 1].style.boxShadow= brilhoPersoMain;

bottonList[positionPersoMain - 18].style.backgroundColor= corReflexoW;
bottonList[positionPersoMain - 18].style.boxShadow= brilhoReflexoW;

bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;

bottonList[positionPersoMain - 2].style.backgroundColor= corReflexoA;
bottonList[positionPersoMain - 2].style.boxShadow= brilhoReflexoA;

bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
/*-------------------------------------------------------------------------*/

document.addEventListener('keydown', function(){
	if (event.key === 'w'){
		console.log("botão clicado");
        verificarPosicaoW();
	}
	if (event.key === 'a'){
		console.log("botão clicado");
		verificarPosicaoA()
	}
	if (event.key === 's'){
		console.log("botão clicado");
        verificarPosicaoS();
	}
	if (event.key === 'd'){
		console.log("botão clicado");
		verificarPosicaoD()
	}
});

function atualizarPixel(positionPersoMain, lastPosition) {
	bottonList[positionPersoMain - 1].style.backgroundColor= corPersoMain;
    bottonList[positionPersoMain - 1].style.boxShadow= brilhoPersoMain;
    bottonList[lastPosition - 1].style.backgroundColor= "#060606";
    bottonList[lastPosition - 1].style.boxShadow= "";
    console.log("Posição atual: " + positionPersoMain + " - Posição Anterior: " + lastPosition);
}











/*let list = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16];

let total = 7;
let numrest = 0;
let numsorteado = [];

while(total != numrest){
	let num = Math.floor(Math.random() * 16);
	numsorteado.push(num);
    numrest = verificar(num, list, numrest);
}

console.log(numsorteado);
var minhaSelecao = [];*/
/*------------------------------------------------------*/
/*botton.addEventListener("click", function() {
	var numselecionado = event.target.textContent;
	var numformatado = parseInt(numselecionado);
	minhaSelecao.push(numformatado);
	event.target.style.backgroundColor= "red";
	console.log(minhaSelecao);
});*/
/*---------------------------------------------------------*/
/*bottons.addEventListener("click", function() {
	for (var i = 0; i != numsorteado.length; i++){
		var n = numsorteado[i];
		var alvo = event.target.textContent;

		if (numsorteado[i] == alvo){
			event.target.style.backgroundColor= "red";
			event.target.style.boxShadow= "-5px -5px 45px red";
			return;
		}else{
			console.log("errouuu");
			event.target.style.backgroundColor= "white";
			event.target.style.boxShadow= "-5px -5px 45px white";
		}
	}
});

document.addEventListener('keydown', function(){
	if (event.key === 'q'){
		button1.style.backgroundColor= "red";
		button1.style.boxShadow= "-5px -5px 45px red";
	}

	if (event.key === 'w'){
		button2.style.backgroundColor= "red";
		button2.style.boxShadow= "-5px -5px 45px red";
	}

	if (event.ctrlKey & event.key === 'q'){
		button1.style.backgroundColor= "white";
		button1.style.boxShadow= "-5px -5px 45px white"
	}

	if (event.ctrlKey & event.key === 'w'){
		button2.style.backgroundColor= "white";
		button2.style.boxShadow= "-5px -5px 45px white"
	}
});

document.addEventListener('keyup', function(){
	if (event.key === 'q'){
		button1.style.backgroundColor= "";
		button1.style.boxShadow= "";
	}

	if (event.key === 'w'){
		button2.style.backgroundColor= "";
		button2.style.boxShadow= "";
	}

});

button1.addEventListener('scroll', function() {
	button1.style.backgroundColor= "white";
	button1.style.boxShadow= "-5px -5px 45px white";
});
*/