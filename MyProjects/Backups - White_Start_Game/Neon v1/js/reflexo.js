function reflexoW(position){
	if (position >= 11) {
		bottonList[position - 11].style.backgroundColor= "green";
	    bottonList[position - 11].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position + 9].style.backgroundColor= "yellow";
	    bottonList[position + 9].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position - 2].style.backgroundColor= "lightblue";
	    bottonList[position - 1].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position].style.backgroundColor= "orange";
	    bottonList[position].style.boxShadow= "-5px -5px 35px #898989";
	    return
	}
	bottonList[position + 9].style.backgroundColor= "yellow";
	bottonList[position + 9].style.boxShadow= "-5px -5px 35px #898989";
    bottonList[position - 2].style.backgroundColor= "lightblue";
	bottonList[position - 1].style.boxShadow= "-5px -5px 35px #898989";
    bottonList[position].style.backgroundColor= "orange";
	bottonList[position].style.boxShadow= "-5px -5px 35px #898989";
}

function reflexA(position){
	if (position == 1 ||position == 11 || position == 21 || position == 31 || position == 41) {
		bottonList[position - 11].style.backgroundColor= "green";
		bottonList[position - 11].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position + 9].style.backgroundColor= "yellow";
	    bottonList[position + 9].style.boxShadow= "-5px -5px 35px #898989";
	    bottonList[position].style.backgroundColor= "orange";
        bottonList[position].style.boxShadow= "-5px -5px 35px #898989";
		return
	}
	bottonList[position - 2].style.backgroundColor= "lightblue";
    bottonList[position - 1].style.boxShadow= "-5px -5px 35px #898989";
	bottonList[position - 11].style.backgroundColor= "green";
	bottonList[position - 11].style.boxShadow= "-5px -5px 35px #898989";
	bottonList[position + 9].style.backgroundColor= "yellow";
	bottonList[position + 9].style.boxShadow= "-5px -5px 35px #898989";
	bottonList[position].style.backgroundColor= "orange";
    bottonList[position].style.boxShadow= "-5px -5px 35px #898989";
}

function reflexoS(position){
	if (position < 41) {
		bottonList[position - 11].style.backgroundColor= "green";
		bottonList[position - 11].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position + 9].style.backgroundColor= "yellow";
	    bottonList[position + 9].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position - 2].style.backgroundColor= "lightblue";
	    bottonList[position - 1].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position].style.backgroundColor= "orange";
	    bottonList[position].style.boxShadow= "-5px -5px 35px #898989";
		return
	}
	bottonList[position - 11].style.backgroundColor= "green";
	bottonList[position - 11].style.boxShadow= "-5px -5px 35px #898989";
	bottonList[position - 2].style.backgroundColor= "lightblue";
    bottonList[position - 1].style.boxShadow= "-5px -5px 35px #898989";
	bottonList[position].style.backgroundColor= "orange";
    bottonList[position].style.boxShadow= "-5px -5px 35px #898989";
}

function reflexoD(position){
    if (position == 10 ||position == 20 || position == 30 || position == 40 || position == 50){
		bottonList[position - 11].style.backgroundColor= "green";
		bottonList[position - 11].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position + 9].style.backgroundColor= "yellow";
	    bottonList[position + 9].style.boxShadow= "-5px -5px 35px #898989";
		bottonList[position - 2].style.backgroundColor= "lightblue";
	    bottonList[position - 1].style.boxShadow= "-5px -5px 35px #898989";
		return
    }
	bottonList[position - 11].style.backgroundColor= "green";
	bottonList[position - 11].style.boxShadow= "-5px -5px 35px #898989";
	bottonList[position + 9].style.backgroundColor= "yellow";
    bottonList[position + 9].style.boxShadow= "-5px -5px 35px #898989";
	bottonList[position - 2].style.backgroundColor= "lightblue";
    bottonList[position - 1].style.boxShadow= "-5px -5px 35px #898989";
	bottonList[position].style.backgroundColor= "orange";
    bottonList[position].style.boxShadow= "-5px -5px 35px #898989";
}

/*----------------------------------------------------------*/

function lastReflexoW(position){
	if (position <= 31){
		console.log("condição executada");
		bottonList[lastPosition + 9].style.backgroundColor= "#060606";
        bottonList[lastPosition + 9].style.boxShadow= "";
		bottonList[lastPosition - 2].style.backgroundColor= "#060606";
	    bottonList[lastPosition - 1].style.boxShadow= "";
		bottonList[lastPosition].style.backgroundColor= "#060606";
	    bottonList[lastPosition].style.boxShadow= "";
	    return
	}
	console.log("fora da condição executada");
	bottonList[lastPosition - 2].style.backgroundColor= "#060606";
    bottonList[lastPosition - 1].style.boxShadow= "";
	bottonList[lastPosition].style.backgroundColor= "#060606";
    bottonList[lastPosition].style.boxShadow= "";
}

function lastReflexoA(position){
	bottonList[lastPosition - 11].style.backgroundColor= "#060606";
	bottonList[lastPosition - 11].style.boxShadow= "";
	bottonList[lastPosition + 9].style.backgroundColor= "#060606";
    bottonList[lastPosition + 9].style.boxShadow= "";
	bottonList[lastPosition].style.backgroundColor= "#060606";
    bottonList[lastPosition].style.boxShadow= "";
}

function lastReflexoS(position, lastPosition){
	if (position >= 21){
		bottonList[lastPosition - 11].style.backgroundColor= "#060606";
		bottonList[lastPosition - 11].style.boxShadow= "";
		bottonList[lastPosition - 2].style.backgroundColor= "#060606";
		bottonList[lastPosition - 1].style.boxShadow= "";
	    bottonList[lastPosition].style.backgroundColor= "#060606";
		bottonList[lastPosition].style.boxShadow= "";
	    return
	}
	bottonList[lastPosition - 2].style.backgroundColor= "#060606";
	bottonList[lastPosition - 1].style.boxShadow= "";
    bottonList[lastPosition].style.backgroundColor= "#060606";
	bottonList[lastPosition].style.boxShadow= "";
}

function lastReflexoD(position){
	bottonList[lastPosition - 11].style.backgroundColor= "#060606";
	bottonList[lastPosition - 11].style.boxShadow= "";
	bottonList[lastPosition + 9].style.backgroundColor= "#060606";
    bottonList[lastPosition + 9].style.boxShadow= "";
	bottonList[lastPosition - 2].style.backgroundColor= "#060606";
    bottonList[lastPosition - 1].style.boxShadow= "";
}