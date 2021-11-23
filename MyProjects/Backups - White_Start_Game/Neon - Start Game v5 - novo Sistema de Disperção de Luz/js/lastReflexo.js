function lastReflexoSideW(){
	if (positionPersoMain < bordaFinalA - bordaInicialD){
        clearLastPositReflexA(); clearLastPositReflexS(); clearLastPositReflexD();
	    return
	}
	if (positionPersoMain == bordaFinalD - bordaInicialD) {
        clearLastPositReflexA();
        return
	}
    clearLastPositReflexA(); clearLastPositReflexD();
}

function lastReflexoSideA(){
	clearLastPositReflexW(); clearLastPositReflexS(); clearLastPositReflexD();
}

function lastReflexoSideS(){
	if (positionPersoMain > bordaInicialD + bordaInicialD){
        clearLastPositReflexW(); clearLastPositReflexA(); clearLastPositReflexD();
	    return
	} 
	if (positionPersoMain == bordaInicialD+1){
        clearLastPositReflexD();
	    return
	}
    clearLastPositReflexA(); clearLastPositReflexD();
}

function lastReflexoSideD(){
    clearLastPositReflexW(); clearLastPositReflexA(); clearLastPositReflexS();
}

function clearLastPositReflexW(cor=positionLastReflexoW, shadow=positionLastReflexoW) {clearLastPositCorRefex(cor); clearLastPositShadowReflex(shadow)}
function clearLastPositReflexS(cor=positionLastReflexoS, shadow=positionLastReflexoS) {clearLastPositCorRefex(cor); clearLastPositShadowReflex(shadow)}
function clearLastPositReflexA(cor=positionLastReflexoA, shadow=positionLastReflexoA) {clearLastPositCorRefex(cor); clearLastPositShadowReflex(shadow)}
function clearLastPositReflexD() {clearLastPositCorRefex(); clearLastPositShadowReflex()}

function clearLastPositCorRefex(PLCR=lastPosition, CLRL=corRestauracao) { bottonList[PLCR].style.backgroundColor= CLRL; }
function clearLastPositShadowReflex(PLSR=lastPosition, BLRL=clearShadow) { bottonList[PLSR].style.boxShadow= BLRL; }

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

function lastReflexoSideW1(){
	if (positionPersoMain < bordaFinalA - bordaInicialD){
        clearLastPositReflexA1(); clearLastPositReflexS1(); clearLastPositReflexD1();
	    return
	}
	if (positionPersoMain == bordaFinalD - bordaInicialD) {
        clearLastPositReflexA1();
        return
	}
    clearLastPositReflexA1(); clearLastPositReflexD1();
}

function lastReflexoSideA1(){
	clearLastPositReflexW1(); clearLastPositReflexS1(); clearLastPositReflexD1();
}

function lastReflexoSideS1(){
	if (positionPersoMain > bordaInicialD + bordaInicialD){
        clearLastPositReflexW1(); clearLastPositReflexA1(); clearLastPositReflexD1();
	    return
	} 
	if (positionPersoMain == bordaInicialD+1){
        clearLastPositReflexD1();
	    return
	}
    clearLastPositReflexA1(); clearLastPositReflexD1();
}

function lastReflexoSideD1(){
    clearLastPositReflexW1(); clearLastPositReflexA1(); clearLastPositReflexS1();
}

function clearLastPositReflexW1(cor=positionLastReflexoW1, shadow=positionLastReflexoW1) {clearLastPositCorRefex1(cor); clearLastPositShadowReflex1(shadow)}
function clearLastPositReflexS1(cor=positionLastReflexoS1, shadow=positionLastReflexoS1) {clearLastPositCorRefex1(cor); clearLastPositShadowReflex1(shadow)}
function clearLastPositReflexA1(cor=positionLastReflexoA1, shadow=positionLastReflexoA1) {clearLastPositCorRefex1(cor); clearLastPositShadowReflex1(shadow)}
function clearLastPositReflexD1() {clearLastPositCorRefex1(); clearLastPositShadowReflex1()}

function clearLastPositCorRefex1(PLCR=positionLastReflexoD1, CLRL=corRestauracao) { bottonList[PLCR].style.backgroundColor= CLRL; }
function clearLastPositShadowReflex1(PLSR=positionLastReflexoD1, BLRL=clearShadow) { bottonList[PLSR].style.boxShadow= BLRL; }

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

function lastReflexoSideW2(){
	if (positionPersoMain < bordaFinalA - bordaInicialD){
        clearLastPositReflexA2(); clearLastPositReflexS2(); clearLastPositReflexD2();
	    return
	}
	if (positionPersoMain == bordaFinalD - bordaInicialD) {
        clearLastPositReflexA2();
        return
	}
    clearLastPositReflexA2(); clearLastPositReflexD2();
}

function lastReflexoSideA2(){
	clearLastPositReflexW2(); clearLastPositReflexS2(); clearLastPositReflexD2();
}

function lastReflexoSideS2(){
	if (positionPersoMain > bordaInicialD + bordaInicialD){
        clearLastPositReflexW2(); clearLastPositReflexA2(); clearLastPositReflexD2();
	    return
	} 
	if (positionPersoMain == bordaInicialD+1){
        clearLastPositReflexD2();
	    return
	}
    clearLastPositReflexA2(); clearLastPositReflexD2();
}

function lastReflexoSideD2(){
    clearLastPositReflexW2(); clearLastPositReflexA2(); clearLastPositReflexS2();
}

function clearLastPositReflexW2() {clearLastPositCorRefex2(positionLastReflexoW2); clearLastPositShadowReflex2(positionLastReflexoW2)}
function clearLastPositReflexS2() {clearLastPositCorRefex2(positionLastReflexoS2); clearLastPositShadowReflex2(positionLastReflexoS2)}
function clearLastPositReflexA2() {clearLastPositCorRefex2(positionLastReflexoA2); clearLastPositShadowReflex2(positionLastReflexoA2)}
function clearLastPositReflexD2() {clearLastPositCorRefex2(); clearLastPositShadowReflex2()}

function clearLastPositCorRefex2(PLCR=positionLastReflexoD2, CLRL=corRestauracao) { bottonList[PLCR].style.backgroundColor= CLRL; }
function clearLastPositShadowReflex2(PLSR=positionLastReflexoD2, BLRL=clearShadow) { bottonList[PLSR].style.boxShadow= BLRL; }