function verificarPosicaoW(){
	if (position >= 11){
		lastPosition = position;
		position = position -10;
		atualizarPixel(position, lastPosition);
		lastReflexoW(position);
		reflexoW(position);
		return
	}
	console.log("Não pode passar pela parede");
}

function verificarPosicaoA(){
	if (position == 1 ||position == 11 || position == 21 || position == 31 || position == 41) {
		console.log("Não pode passar por aqui");
		return
	}
    lastPosition = position;
	position = position -1;
	atualizarPixel(position, lastPosition);
	lastReflexoA(position);
	reflexA(position);
}

function verificarPosicaoS(){
	if (position < 41) {
		lastPosition = position;
		position = position +10;
		atualizarPixel(position, lastPosition);
		lastReflexoS(position, lastPosition);
		reflexoS(position);
		return
	}
	console.log("Não pode passar por aqui");
}

function verificarPosicaoD(){
    if (position == 10 ||position == 20 || position == 30 || position == 40 || position == 50){
    	console.log("Não pode passar pela parede");
		return
    }
    lastPosition = position;
	position = position +1;
	atualizarPixel(position, lastPosition);
	lastReflexoD(position);
	reflexoD(position);
}