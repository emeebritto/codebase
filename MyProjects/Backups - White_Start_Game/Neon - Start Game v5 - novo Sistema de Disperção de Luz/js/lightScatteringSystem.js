// Layer 1.0
// Layer 1.0

// cL = colorLight
// pL = powerLight
function lightScattering(pL, sourceLight, lastSourceLight, ps, cL1, cL1_1, cL2, cL2_1, cL2_2){
    bottonList[sourceLight-1].classList.add(ps);
    bottonList[lastSourceLight-1].classList.remove(ps);

	if (pL >= 1){
		setShineSideWLayer1(sourceLight, lastSourceLight, cL1, cL1_1);
		setShineSideALayer1(sourceLight, lastSourceLight, cL1, cL1_1);
		setShineSideSLayer1(sourceLight, lastSourceLight, cL1, cL1_1);
		setShineSideDLayer1(pL, sourceLight, lastSourceLight, cL1, cL1_1, cL2, cL2_1, cL2_2);
	}
	if (pL == 0){
	    bottonList[lastSourceLight-40].classList.remove(cL1);
	    ShineSideWLayer1 = false;
	    bottonList[lastSourceLight-2].classList.remove(cL1);
	    ShineSideALayer1 = false;
	    bottonList[lastSourceLight+38].classList.remove(cL1);
	    ShineSideSLayer1 = false;
	    bottonList[lastSourceLight].classList.remove(cL1);
	    ShineSideDLayer1 = false;
	}
}

function setShineSideWLayer1(sourceLight, lastSourceLight, cL1, cL1_1) {
	futurePositionShineW = sourceLight-39;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineW == mapa[i]){
			console.log("com condição");
			bottonList[lastSourceLight-40].classList.remove(cL1);
			bottonList[sourceLight-40].classList.add(cL1);
			ShineSideWLayer1 = true;
			return
		}
	}
	console.log("sem condição");
    bottonList[lastSourceLight-40].classList.remove(cL1);
	ShineSideWLayer1 = false;
}

function setShineSideALayer1(sourceLight, lastSourceLight, cL1, cL1_1) {
	futurePositionShineA = sourceLight -1;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineA == mapa[i]){
            bottonList[lastSourceLight-2].classList.remove(cL1);
			bottonList[sourceLight-2].classList.add(cL1);
			ShineSideALayer1 = true;
			return
		}
	}
    bottonList[lastSourceLight-2].classList.remove(cL1);
	ShineSideALayer1 = false;
}

function setShineSideSLayer1(sourceLight, lastSourceLight, cL1, cL1_1) {
	futurePositionShineS = sourceLight+39;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineS == mapa[i]){
            bottonList[lastSourceLight+38].classList.remove(cL1);
			bottonList[sourceLight+38].classList.add(cL1);
			ShineSideSLayer1 = true;
			return
		}
	}
    bottonList[lastSourceLight+38].classList.remove(cL1);
	ShineSideSLayer1 = false;
}

function setShineSideDLayer1(pL, sourceLight, lastSourceLight, cL1, cL1_1, cL2, cL2_1, cL2_2) {
	futurePositionShineD = sourceLight+1;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineD == mapa[i]){
			bottonList[lastSourceLight].classList.remove(cL1);
			bottonList[sourceLight].classList.add(cL1);
			ShineSideDLayer1 = true;
			lightScattering2_0 (pL, sourceLight, lastSourceLight, cL1_1, cL2, cL2_1, cL2_2);
			return
		}
	}
    bottonList[lastSourceLight].classList.remove(cL1);
	ShineSideDLayer1 = false;
	lightScattering2_0 (pL, sourceLight, lastSourceLight, cL1_1, cL2, cL2_1, cL2_2);
	return
}


/*---------------------------------------------------------------------------------*/
// Layer 1.1
// Layer 2.0

function lightScattering2_0 (pL, sourceLight, lastSourceLight, cL1_1, cL2, cL2_1, cL2_2) {
	if (pL >= 2){
		setShineSideWDLayer1_1(sourceLight, lastSourceLight, cL1_1);
		setShineSideAWLayer1_1(sourceLight, lastSourceLight, cL1_1);
		setShineSideSALayer1_1(sourceLight, lastSourceLight, cL1_1);
		setShineSideDSLayer1_1(sourceLight, lastSourceLight, cL1_1);
		setShineSideWLayer2(sourceLight, lastSourceLight, cL2);
		setShineSideALayer2(sourceLight, lastSourceLight, cL2);
		setShineSideSLayer2(sourceLight, lastSourceLight, cL2);
		setShineSideDLayer2(pL, sourceLight, lastSourceLight, cL2, cL2_1, cL2_2);
	}
	if (pL == 0){
		bottonList[lastSourceLight-39].classList.remove(cL1_1);
		shineSideWDLayer1 = false;
		bottonList[lastSourceLight-41].classList.remove(cL1_1);
		shineSideAWLayer1 = false;
		bottonList[lastSourceLight+37].classList.remove(cL1_1);
		shineSideSALayer1 = false;
		bottonList[lastSourceLight+39].classList.remove(cL1_1);
		shineSideDSLayer1 = false;
	}
}

function setShineSideWDLayer1_1(sourceLight, lastSourceLight, cL1_1) {
	futurePositionShineWD = sourceLight-39;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineWD == mapa[i]){
			bottonList[lastSourceLight-39].classList.remove(cL1_1);
			bottonList[sourceLight-39].classList.add(cL1_1);
			shineSideWDLayer1 = true;
			return
		}
	}
    bottonList[lastSourceLight-39].classList.remove(cL1_1);
	shineSideWDLayer1 = false;
}

function setShineSideAWLayer1_1(sourceLight, lastSourceLight, cL1_1) {
	futurePositionShineAW = sourceLight -40;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineAW == mapa[i]){
            bottonList[lastSourceLight-41].classList.remove(cL1_1);
			bottonList[sourceLight-41].classList.add(cL1_1);
			shineSideAWLayer1 = true;
			return
		}
	}
    bottonList[lastSourceLight-41].classList.remove(cL1_1);
	shineSideAWLayer1 = false;
}

function setShineSideSALayer1_1(sourceLight, lastSourceLight, cL1_1) {
	futurePositionShineSA = sourceLight+38;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineSA == mapa[i]){
            bottonList[lastSourceLight+37].classList.remove(cL1_1);
			bottonList[sourceLight+37].classList.add(cL1_1);
			shineSideSALayer1 = true;
			return
		}
	}
    bottonList[lastSourceLight+37].classList.remove(cL1_1);
	shineSideSALayer1 = false;
}

function setShineSideDSLayer1_1(sourceLight, lastSourceLight, cL1_1) {
	futurePositionShineDS = sourceLight+40;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineDS == mapa[i]){
			bottonList[lastSourceLight+39].classList.remove(cL1_1);
			bottonList[sourceLight+39].classList.add(cL1_1);
			shineSideDSLayer1 = true;
			return
		}
	}
    bottonList[lastSourceLight+39].classList.remove(cL1_1);
	shineSideDSLayer1 = false;
	return
}



function setShineSideWLayer2(sourceLight, lastSourceLight, cL2) {
	futurePositionShineW2 = sourceLight-78;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineW2 == mapa[i]){
			bottonList[lastSourceLight-79].classList.remove(cL2);
			bottonList[sourceLight-79].classList.add(cL2);
			ShineSideWLayer2 = true;
			return
		}
	}
    bottonList[lastSourceLight-79].classList.remove(cL2);
	ShineSideWLayer2 = false;
}

function setShineSideALayer2(sourceLight, lastSourceLight, cL2) {
	futurePositionShineA2 = sourceLight -2;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineA2 == mapa[i]){
            bottonList[lastSourceLight-3].classList.remove(cL2);
			bottonList[sourceLight-3].classList.add(cL2);
			ShineSideALayer2 = true;
			return
		}
	}
    bottonList[lastSourceLight-3].classList.remove(cL2);
	ShineSideALayer2 = false;
}

function setShineSideSLayer2(sourceLight, lastSourceLight, cL2) {
	futurePositionShineS2 = sourceLight+78;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineS2 == mapa[i]){
            bottonList[lastSourceLight+77].classList.remove(cL2);
			bottonList[sourceLight+77].classList.add(cL2);
			ShineSideSLayer2 = true;
			return
		}
	}
    bottonList[lastSourceLight+77].classList.remove(cL2);
	ShineSideSLayer2 = false;
}

function setShineSideDLayer2(pL, sourceLight, lastSourceLight, cL2, cL2_1, cL2_2) {
	futurePositionShineD2 = sourceLight+2;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineD2 == mapa[i]){
			bottonList[lastSourceLight+1].classList.remove(cL2);
			bottonList[sourceLight+1].classList.add(cL2);
			ShineSideDLayer2 = true;
			lightScattering3_0 (pL, sourceLight, lastSourceLight, cL2_1, cL2_2);
			return
		}
	}
    bottonList[lastSourceLight+1].classList.remove(cL2);
	ShineSideDLayer2 = false;
	lightScattering3_0 (pL, sourceLight, lastSourceLight, cL2_1, cL2_2);
	return
}

/*------------------------------------------------------------------------------------------------*/
// Layer 3.0

function lightScattering3_0 (pL, sourceLight, lastSourceLight, cL2_1, cL2_2) {
	if (pL >= 3){
		setShineSideWDLayer2_1(sourceLight, lastSourceLight, cL2_1);
		setShineSideAWLayer2_1(sourceLight, lastSourceLight, cL2_1);
		setShineSideSALayer2_1(sourceLight, lastSourceLight, cL2_1);
		setShineSideDSLayer2_1(sourceLight, lastSourceLight, cL2_1);

		setShineSideWDLayer2_2(sourceLight, lastSourceLight, cL2_2);
		setShineSideAWLayer2_2(sourceLight, lastSourceLight, cL2_2);
		setShineSideSALayer2_2(sourceLight, lastSourceLight, cL2_2);
		setShineSideDSLayer2_2(pL, sourceLight, lastSourceLight, cL2_2);
	}
	if (pL == 0){
		bottonList[lastSourceLight-39].classList.remove(cL2_1);
		shineSideWDLayer1 = false;
		bottonList[lastSourceLight-41].classList.remove(cL2_1);
		shineSideAWLayer1 = false;
		bottonList[lastSourceLight+37].classList.remove(cL2_1);
		shineSideSALayer1 = false;
		bottonList[lastSourceLight+39].classList.remove(cL2_1);
		shineSideDSLayer1 = false;
	}
}


function setShineSideWDLayer2_1(sourceLight, lastSourceLight, cL2_1) {
	futurePositionShineWD2_1 = sourceLight-38;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineWD2_1 == mapa[i]){
			bottonList[lastSourceLight-38].classList.remove(cL2_1);
			bottonList[sourceLight-38].classList.add(cL2_1);
			shineSideWDLayer2_1 = true;
			return
		}
	}
    bottonList[lastSourceLight-38].classList.remove(cL2_1);
	shineSideWDLayer2_1 = false;
}

function setShineSideWDLayer2_2(sourceLight, lastSourceLight, cL2_2) {
	futurePositionShineWD2_2 = sourceLight-78;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineWD2_2 == mapa[i]){
			bottonList[lastSourceLight-78].classList.remove(cL2_2);
			bottonList[sourceLight-78].classList.add(cL2_2);
			shineSideWDLayer2_2 = true;
			return
		}
	}
    bottonList[lastSourceLight-78].classList.remove(cL2_2);
	shineSideWDLayer2_2 = false;
}

function setShineSideAWLayer2_1(sourceLight, lastSourceLight, cL2_1) {
	futurePositionShineAW2_1 = sourceLight -42;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineAW2_1 == mapa[i]){
            bottonList[lastSourceLight-42].classList.remove(cL2_1);
			bottonList[sourceLight-42].classList.add(cL2_1);
			shineSideAWLayer2_1 = true;
			return
		}
	}
    bottonList[lastSourceLight-42].classList.remove(cL2_1);
	shineSideAWLayer2_1 = false;
}

function setShineSideAWLayer2_2(sourceLight, lastSourceLight, cL2_2) {
	futurePositionShineAW2_2 = sourceLight -80;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineAW2_2 == mapa[i]){
            bottonList[lastSourceLight-80].classList.remove(cL2_2);
			bottonList[sourceLight-80].classList.add(cL2_2);
			shineSideAWLayer2_2 = true;
			return
		}
	}
    bottonList[lastSourceLight-80].classList.remove(cL2_2);
	shineSideAWLayer2_2 = false;
}

function setShineSideSALayer2_1(sourceLight, lastSourceLight, cL2_1) {
	futurePositionShineSA2_1 = sourceLight+36;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineSA2_1 == mapa[i]){
            bottonList[lastSourceLight+36].classList.remove(cL2_1);
			bottonList[sourceLight+36].classList.add(cL2_1);
			shineSideSALayer2_1 = true;
			return
		}
	}
    bottonList[lastSourceLight+36].classList.remove(cL2_1);
	shineSideSALayer2_1 = false;
}

function setShineSideSALayer2_2(sourceLight, lastSourceLight, cL2_2) {
	futurePositionShineSA2_2 = sourceLight+76;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineSA2_2 == mapa[i]){
            bottonList[lastSourceLight+76].classList.remove(cL2_2);
			bottonList[sourceLight+76].classList.add(cL2_2);
			shineSideSALayer2_2 = true;
			return
		}
	}
    bottonList[lastSourceLight+76].classList.remove(cL2_2);
	shineSideSALayer2_2 = false;
}

function setShineSideDSLayer2_1(sourceLight, lastSourceLight, cL2_1) {
	futurePositionShineDS2_1 = sourceLight+40;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineDS2_1 == mapa[i]){
			bottonList[lastSourceLight+40].classList.remove(cL2_1);
			bottonList[sourceLight+40].classList.add(cL2_1);
			shineSideDSLayer2_1 = true;
			return
		}
	}
    bottonList[lastSourceLight+40].classList.remove(cL2_1);
	shineSideDSLayer2_1 = false;
	return
}

function setShineSideDSLayer2_2(pL, sourceLight, lastSourceLight, cL2_2) {
	futurePositionShineDS2_2 = sourceLight+78;
	for (var i = 0; i <= mapa.length; i++){
		if (futurePositionShineDS2_2 == mapa[i]){
			bottonList[lastSourceLight+78].classList.remove(cL2_2);
			bottonList[sourceLight+78].classList.add(cL2_2);
			shineSideDSLayer2_2 = true;
			return
		}
	}
    bottonList[lastSourceLight+78].classList.remove(cL2_2);
	shineSideDSLayer2_2 = false;
	return
}








/*function setPositionReflexoW() {setPositionCorReflexo(positionReflexoW); setPositionShadowReflexo(positionReflexoW)}
function setPositionReflexoS() {setPositionCorReflexo(positionReflexoS); setPositionShadowReflexo(positionReflexoS)}
function setPositionReflexoA() {setPositionCorReflexo(positionReflexoA); setPositionShadowReflexo(positionReflexoA)}
function setPositionReflexoD() {setPositionCorReflexo(); setPositionShadowReflexo()}

function setPositionCorReflexo(PCR=positionPersoMain, CRL=corReflexoLateral) { bottonList[PCR].style.backgroundColor= CRL; }
function setPositionShadowReflexo(PSR=positionPersoMain, BRL=blurReflexoLateral) { bottonList[PSR].style.boxShadow= BRL; }*/