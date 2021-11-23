function verificarPosicaoW(){
	if (positionPersoMain >= 11){
		lastPosition = positionPersoMain;
		positionPersoMain = positionPersoMain -17;
		atualizarPixel(positionPersoMain, lastPosition);
		lastReflexoW(positionPersoMain);
		reflexoW(positionPersoMain, corReflexoW);
		return
	}
	console.log("Não pode passar pela parede");
}

function verificarPosicaoA(){
	if (positionPersoMain == 1 ||positionPersoMain == 18 || positionPersoMain == 35 || positionPersoMain == 52 || positionPersoMain == 69 || positionPersoMain == 86 || positionPersoMain == 103 || positionPersoMain == 120) {
		console.log("Não pode passar por aqui");
		return
	}
    lastPosition = positionPersoMain;
	positionPersoMain = positionPersoMain -1;
	atualizarPixel(positionPersoMain, lastPosition);
	lastReflexoA(positionPersoMain);
	reflexA(positionPersoMain);
}

function verificarPosicaoS(){
	if (positionPersoMain < bottonList.length - 16) {
		lastPosition = positionPersoMain;
		positionPersoMain = positionPersoMain +17;
		atualizarPixel(positionPersoMain, lastPosition);
		lastReflexoS(positionPersoMain, lastPosition);
		reflexoS(positionPersoMain);
		return
	}
	console.log("Não pode passar por aqui");
}

function verificarPosicaoD(){
    if (positionPersoMain == 17 ||positionPersoMain == 34 || positionPersoMain == 51 || positionPersoMain == 68 || positionPersoMain == 85 || positionPersoMain == 102 || positionPersoMain == 119 || positionPersoMain == 136){
    	console.log("Não pode passar pela parede");
		return
    }
    lastPosition = positionPersoMain;
	positionPersoMain = positionPersoMain +1;
	atualizarPixel(positionPersoMain, lastPosition);
	lastReflexoD(positionPersoMain);
	reflexoD(positionPersoMain);
}