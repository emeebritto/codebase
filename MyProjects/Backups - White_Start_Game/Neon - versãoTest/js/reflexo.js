
function reflexoW(positionPersoMain){
	if (positionPersoMain > 18) {
		bottonList[positionPersoMain - 18].style.backgroundColor= corReflexoW;
	    bottonList[positionPersoMain - 18].style.boxShadow= brilhoReflexoW;
		bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
	    bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;
		bottonList[positionPersoMain - 2].style.backgroundColor= corReflexoA;
	    bottonList[positionPersoMain - 2].style.boxShadow= brilhoReflexoA;
		bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
	    bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
	    return
	}
	if (positionPersoMain == 1){
        bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
	    bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;
	    bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
		bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
		return
	}
	bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
	bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;
    bottonList[positionPersoMain - 2].style.backgroundColor= corReflexoA;
	bottonList[positionPersoMain - 2].style.boxShadow= brilhoReflexoA;
    bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
	bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
}

function reflexA(positionPersoMain){
	if (positionPersoMain == 1 ||positionPersoMain == 18 || positionPersoMain == 35 || positionPersoMain == 52 || positionPersoMain == 69 || positionPersoMain == 86 || positionPersoMain == 103 || positionPersoMain == 120) {
		bottonList[positionPersoMain - 18].style.backgroundColor= corReflexoW;
		bottonList[positionPersoMain - 18].style.boxShadow= brilhoReflexoW;
		bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
	    bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;
	    bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
        bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
		return
	}
	bottonList[positionPersoMain - 2].style.backgroundColor= corReflexoA;
    bottonList[positionPersoMain - 2].style.boxShadow= brilhoReflexoA;
	bottonList[positionPersoMain - 18].style.backgroundColor= corReflexoW;
	bottonList[positionPersoMain - 18].style.boxShadow= brilhoReflexoW;
	bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
	bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;
	bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
    bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
}

function reflexoS(positionPersoMain){
	if (positionPersoMain < 120) {
		bottonList[positionPersoMain - 18].style.backgroundColor= corReflexoW;
		bottonList[positionPersoMain - 18].style.boxShadow= brilhoReflexoW;
		bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
	    bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;
		bottonList[positionPersoMain - 2].style.backgroundColor= corReflexoA;
	    bottonList[positionPersoMain - 2].style.boxShadow= brilhoReflexoA;
		bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
	    bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
		return
	}
	bottonList[positionPersoMain - 18].style.backgroundColor= corReflexoW;
	bottonList[positionPersoMain - 18].style.boxShadow= brilhoReflexoW;
	bottonList[positionPersoMain - 2].style.backgroundColor= corReflexoA;
    bottonList[positionPersoMain - 2].style.boxShadow= brilhoReflexoA;
	bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
    bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
}

function reflexoD(positionPersoMain){
    if (positionPersoMain == 17 ||positionPersoMain == 34 || positionPersoMain == 51 || positionPersoMain == 68 || positionPersoMain == 85 || positionPersoMain == 102 || positionPersoMain == 119 || positionPersoMain == 136){
		bottonList[positionPersoMain - 18].style.backgroundColor= corReflexoW;
		bottonList[positionPersoMain - 18].style.boxShadow= brilhoReflexoW;
		bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
	    bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;
		bottonList[positionPersoMain - 2].style.backgroundColor= corReflexoA;
	    bottonList[positionPersoMain - 2].style.boxShadow= brilhoReflexoA;
		return
    }
	bottonList[positionPersoMain - 18].style.backgroundColor= corReflexoW;
	bottonList[positionPersoMain - 18].style.boxShadow= brilhoReflexoW;
	bottonList[positionPersoMain + 16].style.backgroundColor= corReflexoS;
    bottonList[positionPersoMain + 16].style.boxShadow= brilhoReflexoS;
	bottonList[positionPersoMain - 2].style.backgroundColor= corReflexoA;
    bottonList[positionPersoMain - 2].style.boxShadow= brilhoReflexoA;
	bottonList[positionPersoMain].style.backgroundColor= corReflexoD;
    bottonList[positionPersoMain].style.boxShadow= brilhoReflexoD;
}

/*----------------------------------------------------------*/

function lastReflexoW(positionPersoMain){
	if (positionPersoMain <= 102){
		console.log("condição executada");
		bottonList[lastPosition + 16].style.backgroundColor= "#060606";
        bottonList[lastPosition + 16].style.boxShadow= "";
		bottonList[lastPosition - 2].style.backgroundColor= "#060606";
	    bottonList[lastPosition - 2].style.boxShadow= "";
		bottonList[lastPosition].style.backgroundColor= "#060606";
	    bottonList[lastPosition].style.boxShadow= "";
	    return
	}
	if (positionPersoMain == 119) {
		bottonList[lastPosition - 2].style.backgroundColor= "#060606";
        bottonList[lastPosition - 2].style.boxShadow= "";
        return
	}
	console.log("fora da condição executada");
	bottonList[lastPosition - 2].style.backgroundColor= "#060606";
    bottonList[lastPosition - 2].style.boxShadow= "";
	bottonList[lastPosition].style.backgroundColor= "#060606";
    bottonList[lastPosition].style.boxShadow= "";
}

function lastReflexoA(positionPersoMain){
	bottonList[lastPosition - 18].style.backgroundColor= "#060606";
	bottonList[lastPosition - 18].style.boxShadow= "";
	bottonList[lastPosition + 16].style.backgroundColor= "#060606";
    bottonList[lastPosition + 16].style.boxShadow= "";
	bottonList[lastPosition].style.backgroundColor= "#060606";
    bottonList[lastPosition].style.boxShadow= "";
}

function lastReflexoS(positionPersoMain, lastPosition){
	if (positionPersoMain >= 35){
		bottonList[lastPosition - 18].style.backgroundColor= "#060606";
		bottonList[lastPosition - 18].style.boxShadow= "";
		bottonList[lastPosition - 2].style.backgroundColor= "#060606";
		bottonList[lastPosition - 2].style.boxShadow= "";
	    bottonList[lastPosition].style.backgroundColor= "#060606";
		bottonList[lastPosition].style.boxShadow= "";
	    return
	} 
	if (positionPersoMain == 18){
		bottonList[lastPosition].style.backgroundColor= "#060606";
	    bottonList[lastPosition].style.boxShadow= "";
	    return
	}
	bottonList[lastPosition - 2].style.backgroundColor= "#060606";
	bottonList[lastPosition - 2].style.boxShadow= "";
    bottonList[lastPosition].style.backgroundColor= "#060606";
	bottonList[lastPosition].style.boxShadow= "";
}

function lastReflexoD(positionPersoMain){
	bottonList[lastPosition - 18].style.backgroundColor= "#060606";
	bottonList[lastPosition - 18].style.boxShadow= "";
	bottonList[lastPosition + 16].style.backgroundColor= "#060606";
    bottonList[lastPosition + 16].style.boxShadow= "";
	bottonList[lastPosition - 2].style.backgroundColor= "#060606";
    bottonList[lastPosition - 2].style.boxShadow= "";
}