function verificarPosicaoW(){
	futurePosition = positionPersoMain -bordaInicialD;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePosition == mapa[i]) {
			lastPosition = positionPersoMain;
			positionPersoMain = positionPersoMain -bordaInicialD;
			arualizar_parametros_persoMain();
			lastReflexoSideW();
			lastReflexoSideW1();
			lastReflexoSideW2();
			reflexoSideW();
			reflexoSideW1();
			reflexoSideW2();
			return
		}
	}
	console.log("Não pode passar pela parede!!");
}

function verificarPosicaoA(){
	futurePosition = positionPersoMain -1;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePosition == mapa[i]) {
		    lastPosition = positionPersoMain;
			positionPersoMain = positionPersoMain -1;
			arualizar_parametros_persoMain();
			lastReflexoSideA();
			lastReflexoSideA1();
			lastReflexoSideA2();
			reflexoSideA();
			reflexoSideA1();
			reflexoSideA2();
			return
	    }
    }
    console.log("Não pode passar por aqui");
}

function verificarPosicaoS(){
	futurePosition = positionPersoMain +bordaInicialD;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePosition == mapa[i]) {
			lastPosition = positionPersoMain;
			positionPersoMain = positionPersoMain +bordaInicialD;
			arualizar_parametros_persoMain();
			lastReflexoSideS();
			lastReflexoSideS1();
			lastReflexoSideS2();
			reflexoSideS();
			reflexoSideS1();
			reflexoSideS2();
			return
        }
	}
	console.log("Hum.. Tente outro caminho");
}

function verificarPosicaoD(){
	futurePosition = positionPersoMain +1;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePosition == mapa[i]) {
			lastPosition = positionPersoMain;
			positionPersoMain = positionPersoMain +1;
			arualizar_parametros_persoMain();
			lastReflexoSideD();
			lastReflexoSideD1();
			lastReflexoSideD2();
			reflexoSideD();
			reflexoSideD1();
			reflexoSideD2();
			return
		}
	}
	console.log("Não pode passar pela parede");
}