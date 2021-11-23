function verificarPosicaoW(){
	if (positionPersoMain >= bordaInicialD){
		lastPosition = positionPersoMain;
		positionPersoMain = positionPersoMain -bordaInicialD;
		atualizar_comportamentos_dos_blocos();
		lastReflexoSideW();
		lastReflexoSideW1();
		lastReflexoSideW2();
		reflexoSideW();
		reflexoSideW1();
		reflexoSideW2();
		return
	}
	console.log("Não pode passar pela parede");
}

function verificarPosicaoA(){
	for (var i = bordaInicialA - 1; i <= bordaFinalA; i++){
		if (positionPersoMain == numBordaA[i]) {
		console.log("Não pode passar por aqui");
		return
	    }
	}
    lastPosition = positionPersoMain;
	positionPersoMain = positionPersoMain -1;
	atualizar_comportamentos_dos_blocos();
	lastReflexoSideA();
	lastReflexoSideA1();
	lastReflexoSideA2();
	reflexoSideA();
	reflexoSideA1();
	reflexoSideA2();
}

function verificarPosicaoS(){
	if (positionPersoMain < bordaFinalA) {
		lastPosition = positionPersoMain;
		positionPersoMain = positionPersoMain +bordaInicialD;
		atualizar_comportamentos_dos_blocos();
		lastReflexoSideS();
		lastReflexoSideS1();
		lastReflexoSideS2();
		reflexoSideS();
		reflexoSideS1();
		reflexoSideS2();
		return
	}
	console.log("Não pode passar por aqui");
}

function verificarPosicaoD(){
	for (var i = bordaInicialA - 1; i <= bordaFinalA; i++){
		if (positionPersoMain == numBordaD[i]){
    	console.log("Não pode passar pela parede");
		return
	    }
    }
    lastPosition = positionPersoMain;
	positionPersoMain = positionPersoMain +1;
	atualizar_comportamentos_dos_blocos();
	lastReflexoSideD();
	lastReflexoSideD1();
	lastReflexoSideD2();
	reflexoSideD();
	reflexoSideD1();
	reflexoSideD2();
}