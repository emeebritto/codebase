// Atualização da iluminação de acordo com a direção de caminhada do personagem.

// 1° Area de reflexo lateral
function reflexoSideW(){
	if (positionPersoMain > bordaInicialA + bordaInicialD) {
        setPositionReflexoW(); setPositionReflexoA();
        setPositionReflexoS(); setPositionReflexoD();
	    return
	}
	if (positionPersoMain == bordaInicialA){
	    setPositionReflexoS(); setPositionReflexoD();
		return
	}
    setPositionReflexoA(); setPositionReflexoS(); setPositionReflexoD();
}

function reflexoSideA(){
	for (var i = bordaInicialA - 1; i <= bordaFinalA; i++){
		if (positionPersoMain == numBordaA[i]) {
	    setPositionReflexoW(); setPositionReflexoS(); setPositionReflexoD();
		return
	    }
	}
    setPositionReflexoW(); setPositionReflexoA();
    setPositionReflexoS(); setPositionReflexoD();
}

function reflexoSideS(){
	if (positionPersoMain < bordaFinalA) {
        setPositionReflexoW(); setPositionReflexoS();
        setPositionReflexoA(); setPositionReflexoD();
		return
	}
    setPositionReflexoW(); setPositionReflexoA(); setPositionReflexoD();
}

function reflexoSideD(){
	for (var i = bordaInicialA - 1; i <= bordaFinalA; i++){
		if (positionPersoMain == numBordaD[i]){
	    setPositionReflexoW(); setPositionReflexoA(); setPositionReflexoS();
		return
	    }
    }
    setPositionReflexoW(); setPositionReflexoA();
    setPositionReflexoS(); setPositionReflexoD();
}

function setPositionReflexoW(cor=positionReflexoW, shadow=positionReflexoW) {setPositionCorReflexo(cor); setPositionShadowReflexo(shadow)}
function setPositionReflexoS(cor=positionReflexoS, shadow=positionReflexoS) {setPositionCorReflexo(cor); setPositionShadowReflexo(shadow)}
function setPositionReflexoA(cor=positionReflexoA, shadow=positionReflexoA) {setPositionCorReflexo(cor); setPositionShadowReflexo(shadow)}
function setPositionReflexoD() {setPositionCorReflexo(); setPositionShadowReflexo()}

function setPositionCorReflexo(PCR=positionPersoMain, CRL=corReflexoLateral) { bottonList[PCR].style.backgroundColor= CRL; }
function setPositionShadowReflexo(PSR=positionPersoMain, BRL=blurReflexoLateral) { bottonList[PSR].style.boxShadow= BRL; }

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

// 1° Area de reflexo - semi-verticais
function reflexoSideW1(){
	if (positionPersoMain > bordaInicialA + bordaInicialD) {
        setPositionReflexoW1(); setPositionReflexoA1();
        setPositionReflexoS1(); setPositionReflexoD1();
	    return
	}
	if (positionPersoMain == bordaInicialA){
	    setPositionReflexoS1(); setPositionReflexoD1();
		return
	}
    setPositionReflexoA1(); setPositionReflexoS1(); setPositionReflexoD1();
}

function reflexoSideA1(){
	for (var i = bordaInicialA - 1; i <= bordaFinalA; i++){
		if (positionPersoMain == numBordaA[i]) {
	    setPositionReflexoW1(); setPositionReflexoS1(); setPositionReflexoD1();
		return
	    }
	}
    setPositionReflexoW1(); setPositionReflexoA1();
    setPositionReflexoS1(); setPositionReflexoD1();
}

function reflexoSideS1(){
	if (positionPersoMain < bordaFinalA) {
        setPositionReflexoW1(); setPositionReflexoS1();
        setPositionReflexoA1(); setPositionReflexoD1();
		return
	}
    setPositionReflexoW1(); setPositionReflexoA1(); setPositionReflexoD1();
}

function reflexoSideD1(){
	for (var i = bordaInicialA - 1; i <= bordaFinalA; i++){
		if (positionPersoMain == numBordaD[i]){
	    setPositionReflexoW1(); setPositionReflexoA1(); setPositionReflexoS1();
		return
	    }
    }
    setPositionReflexoW1(); setPositionReflexoA1();
    setPositionReflexoS1(); setPositionReflexoD1();
}

function setPositionReflexoW1(cor=positionReflexoW1, shadow=positionReflexoW1) {setPositionCorReflexo1(cor); setPositionShadowReflexo1(shadow)}
function setPositionReflexoS1(cor=positionReflexoS1, shadow=positionReflexoS1) {setPositionCorReflexo1(cor); setPositionShadowReflexo1(shadow)}
function setPositionReflexoA1(cor=positionReflexoA1, shadow=positionReflexoA1) {setPositionCorReflexo1(cor); setPositionShadowReflexo1(shadow)}
function setPositionReflexoD1() {setPositionCorReflexo1(); setPositionShadowReflexo1()}

function setPositionCorReflexo1(PCR=positionReflexoD1, CRL=corReflexoSemiVertical) { bottonList[PCR].style.backgroundColor= CRL; }
function setPositionShadowReflexo1(PSR=positionReflexoD1, BRL=blurReflexoSemiVertical) { bottonList[PSR].style.boxShadow= BRL; }

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

// 2° Area de reflexo lateral
function reflexoSideW2(){
	if (positionPersoMain > bordaInicialA + bordaInicialD) {
        setPositionReflexoW2(); setPositionReflexoA2();
        setPositionReflexoS2(); setPositionReflexoD2();
	    return
	}
	if (positionPersoMain == bordaInicialA){
	    setPositionReflexoS2(); setPositionReflexoD2();
		return
	}
    setPositionReflexoA2(); setPositionReflexoS2(); setPositionReflexoD2();
}

function reflexoSideA2(){
	for (var i = bordaInicialA - 1; i <= bordaFinalA; i++){
		if (positionPersoMain == numBordaA[i]) {
	    setPositionReflexoW2(); setPositionReflexoS2(); setPositionReflexoD2();
		return
	    }
	}
    setPositionReflexoW2(); setPositionReflexoA2();
    setPositionReflexoS2(); setPositionReflexoD2();
}

function reflexoSideS2(){
	if (positionPersoMain < bordaFinalA) {
        setPositionReflexoW2(); setPositionReflexoS2();
        setPositionReflexoA2(); setPositionReflexoD2();
		return
	}
    setPositionReflexoW2(); setPositionReflexoA2(); setPositionReflexoD2();
}

function reflexoSideD2(){
	for (var i = bordaInicialA - 1; i <= bordaFinalA; i++){
		if (positionPersoMain == numBordaD[i]){
	    setPositionReflexoW2(); setPositionReflexoA2(); setPositionReflexoS2();
		return
	    }
    }
    setPositionReflexoW2(); setPositionReflexoA2();
    setPositionReflexoS2(); setPositionReflexoD2();
}

function setPositionReflexoW2(cor=positionReflexoW2, shadow=positionReflexoW2) {setPositionCorReflexo2(cor); setPositionShadowReflexo2(shadow)}
function setPositionReflexoS2(cor=positionReflexoS2, shadow=positionReflexoS2) {setPositionCorReflexo2(cor); setPositionShadowReflexo2(shadow)}
function setPositionReflexoA2(cor=positionReflexoA2, shadow=positionReflexoA2) {setPositionCorReflexo2(cor); setPositionShadowReflexo2(shadow)}
function setPositionReflexoD2() {setPositionCorReflexo2(); setPositionShadowReflexo2()}

function setPositionCorReflexo2(PCR=positionReflexoD2, CRL=corReflexoLateralCamada2) { bottonList[PCR].style.backgroundColor= CRL; }
function setPositionShadowReflexo2(PSR=positionReflexoD2, BRL=corReflexoLateralCamada2) { bottonList[PSR].style.boxShadow= BRL; }












/*function setPositionReflexoW() {setPositionCorReflexo(positionReflexoW); setPositionShadowReflexo(positionReflexoW)}
function setPositionReflexoS() {setPositionCorReflexo(positionReflexoS); setPositionShadowReflexo(positionReflexoS)}
function setPositionReflexoA() {setPositionCorReflexo(positionReflexoA); setPositionShadowReflexo(positionReflexoA)}
function setPositionReflexoD() {setPositionCorReflexo(); setPositionShadowReflexo()}

function setPositionCorReflexo(PCR=positionPersoMain, CRL=corReflexoLateral) { bottonList[PCR].style.backgroundColor= CRL; }
function setPositionShadowReflexo(PSR=positionPersoMain, BRL=blurReflexoLateral) { bottonList[PSR].style.boxShadow= BRL; }*/