var painel = document.querySelector(".painel");
var bottonList = [];
for (var i = 1; i <= 50; i++){
	var botton = document.createElement('color');
	botton.id = i;
    botton.style.color= "red";
	botton.style.marginBottom= "7px";
	botton.style.marginLeft= "7px";
	botton.style.width= "144px";
	botton.style.height= "144px";
	botton.style.backgroundColor= "#060606";
	botton.style.transition= "600ms";

	bottonList.push(botton);
	painel.appendChild(botton);
}



let position = 21;
let lastPosition = 21;
/*let refleW = 11;
let refleA = 22;
let refleS = 31;
let refleD = 22;*/
 
console.log("Variaveis criadas");

bottonList[position - 1].style.backgroundColor= "white";
bottonList[position - 1].style.boxShadow= "-5px -5px 35px white";

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

function atualizarPixel(position, lastPosition) {
	bottonList[position - 1].style.backgroundColor= "red";
    bottonList[position - 1].style.boxShadow= "-5px -5px 35px red";
    bottonList[lastPosition - 1].style.backgroundColor= "#060606";
    bottonList[lastPosition - 1].style.boxShadow= "";
    console.log("Posição atual: " + position + " - Posição Anterior: " + lastPosition);
    /*reflexo(position)*/
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