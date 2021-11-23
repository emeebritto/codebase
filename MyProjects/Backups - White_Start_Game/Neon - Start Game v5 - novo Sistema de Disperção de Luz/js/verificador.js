function verificarPosicaoW(){
	futurePosition = positionPersoMain -bordaInicialD;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePosition == mapa[i]) {
			lastPosition = positionPersoMain;
			positionPersoMain = positionPersoMain -bordaInicialD;
			atualizar_parametros_persoMain();
			lightScattering(pLPersoMain, positionPersoMain, lastPosition, pm_color, sh1_w, sh1_1_w, sh2_w, sh2_1_w, sh2_2_w);
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
			atualizar_parametros_persoMain();
			lightScattering(pLPersoMain, positionPersoMain, lastPosition, pm_color, sh1_w, sh1_1_w, sh2_w, sh2_1_w, sh2_2_w);
			

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
			positionPersoMain = positionPersoMain + bordaInicialD;
			atualizar_parametros_persoMain();
			lightScattering(pLPersoMain, positionPersoMain, lastPosition, pm_color, sh1_w, sh1_1_w, sh2_w, sh2_1_w, sh2_2_w);
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
			atualizar_parametros_persoMain();
			lightScattering(pLPersoMain, positionPersoMain, lastPosition, pm_color, sh1_w, sh1_1_w, sh2_w, sh2_1_w, sh2_2_w);
			return
		}
	}
	console.log("Não pode passar pela parede");
}