// Parametros de cor, brilho e Posição do Personagem Principal.
let pLPersoMain = 3;
let positionPersoMain = 162;

// Parametros de campo em Tela.
let bordaInicialA = 1;
let bordaInicialD = 39;
let bordaFinalD = 1794;
// Cálculo automático.
let bordaFinalA = bordaFinalD - (bordaInicialD-1);

/*---------------------------------------------------------------------*/

//Gerador de caminhos.
var painel = document.querySelector(".painel");
var bottonList = [];
for (var i = bordaInicialA; i <= bordaFinalD; i++){
	var botton = document.createElement('color');
	botton.id = i;
	botton.textContent = i;
	botton.style.width= "35px";
	botton.style.height= "35px";
	botton.style.backgroundColor= "#090a1b";
	botton.style.opacity= "0%";
	botton.style.transition= "400ms";

	bottonList.push(botton);
	painel.appendChild(botton);
}

/*------------------------------------------------------------------------*/

console.log(window.scrollX);

var numBordaA = [];
var numBordaD = [];

for (var i = bordaInicialA; i <= bordaFinalA; i = i + bordaInicialD){
	numBordaA.push(i);
}

for (var i = bordaInicialD; i <= bordaFinalD; i = i + bordaInicialD){
	numBordaD.push(i);
}

let mapa = [82,83,84,85,86,87,87,88,127,128,129,168,207,206,245,283,284,322,321,282,243,244,205,206,167,166,165,204,126,125,124,123,122,121,120,160,199,238,238,200,161,161,162,163,163,164,203,202,201,240,239,241,242,281,280,279,278,277,237,198,159,319,320,359,398,399,361,400,401,362,363,402,360,440,441,439,364,325,326,327,288,287,249,250,289,328,327,366,365,404,403,442,443,406,367,405,328,290,251,329,330,331,332,333,334,335,336,337,337,299,298,260,259,258,257,256,297,296,295,294,293,292,291,217,178,177,176,138,137,136,135,97,98,99,100,139,179,218,219,220,221,222,223,184,185,186,147,146,145,144,143,183,182,181,180,142,141,140,102,103,101,62,61,60,59,373,372,371,371,410,411,412,451,452,413,414,453,492,531,530,491,491,490,529,528,489,568,569,567,566,565,564,563,524,525,606,605,604,603,602,600,599,601,562,523,522,521,560,561,523,485,484,639,640,641,642,642,681,680,679,454,455,456,457,458,459,460,461,422,421,420,419,418,417,380,381,382,383,384,345,344,345,346,307,268,267,306,423,385,347,308,269,269,230,229,231,270,309,191,190,189,151,152,153,154,155,194,193,192,232,155,116,115,114,76,77,75,500,501,502,503,542,541,540,539,538,499,498,579,580,581,582,543,621,620,619,660,659,661,622,583,495,494,478,477,438,437,437,476,475,436,475,474,435,513,514,515,552,551,512,473,511,550,628,590,589,629,631,630,669,670,671,672,672,711,709,708,707,668,748,749,710,750,788,788,787,747,591,712,751,790,789,828,829,830,791,752,792,832,831,870,869,868,867,832,833,834,835,835,836,837,838,839,840,841,842,843,844,845,845,846,847,848,888,887,886,885,884,883,882,881,879,878,877,876,875,874,873,872,871,879,880,849,810,809,808,769,770,771,772,733,732,731,730,729,728,689,690,691,692,693,694,695,734,768,655,654,653,652,651,917,918,919,920,920,921,960,959,958,957,956,995,996,997,998,999,1034,1033,994,1033,1035,1074,1073,1072,1071,1110,1112,1111,1149,1188,1150,1189,1187,1148,1109,1186,1225,1226,1227,1147,1228,1268,1269,1309,1348,1388,1350,1349,1310,1311,1271,1270,1270,1231,1230,1229,1308,1307,1267,1190,1185,1184,1146,1145,1144,1143,1141,1140,1139,1102,1103,1104,1105,1106,1106,1107,1142,1181,1180,1179,1178,1100,1099,1098,1098,1137,1178,1138,1176,1176,1177,1059,1020,982,983,981,980,1019,1021,1060,1058,1020,941,940,979,1018,1217,1216,1216,1216,1215,1254,1255,1256,1295,1334,1373,1412,1411,1372,1333,1294,1293,1293,1332,1371,1410,1410,1374,1375,1376,1377,1378,1379,1380,1419,1418,1417,1416,1415,1414,1413,1452,1453,1454,1455,1456,1457,1458,1451,1450,1494,1493,1493,1532,1533,1572,1571,1610,1611,1650,1649,1573,1574,1575,1576,1577,1690,1691,1692,1693,1694,1689,1688,1578,1617,1656,1695,1695,1618,1579,1657,1696,1580,1619,1658,1697,1659,1620,1581,1582,1621,1583,927,966,1005,1044,1083,1122,1161,1200,1239,1278,1279,1240,1201,1162,1123,1084,1085,1124,1163,1202,1241,1280,1281,1242,1242,1203,1164,1125,1086,1048,1047,1049,1050,1051,1090,1129,1168,1207,1246,1285,1324,1323,1322,1321,1320,1052,1091,1130,1169,1208,1247,1286,1325,1121,1160,1199,1238,1513,1512,1511,1550,1551,1552,1553,1514,1515,1554,1589,1628,1593,1632,1671,1709,1708,1707,1667,1706,1710,1711,1672,1633,1594,1555,1516,1750,1749,1748,1747,1746,1745,1705,1666,1627,1588,1549,1510,1744,1472,1471,1432,1431,1430,1429,1390,1351,1389,1428,1468,1469,1470,1253,1292,1291,1252,1251,1290,1329,1368,1367,1328,1289,1250,1407,1408,1447,1446,1406];

for (var i = 0; i < mapa.length; i++){
	var temp = mapa[i];
	bottonList[temp-1].style.opacity= "100%";
}

// whiteColorShine - pattern.
// sh = shine
// w = white

var in_color = "aparencyPersoNPC";
var sh1_gNPC = "shineNPC_WASD_1";
var sh1_1_gNPC = "shineNPC_WDWASADS_1_1";
var sh2_gNPC = "shineNPC_WASD_2";
var sh2_1_gNPC = "shineNPC_WDWASADS_2_1";
var sh2_2_gNPC = "shineNPC_WDWASADS_2_1";

var pm_color = "aparencyPersoMain";
var sh1_w = "shineSide_WASD_1";
var sh1_1_w = "shineSide_WDWASADS_1_1";
var sh2_w = "shineSide_WASD_2";
var sh2_1_w = "shineSide_WDWASADS_2_1";
var sh2_2_w = "shineSide_WDWASADS_2_1";

/*-----------------------------------------------------------------*/

var lastPositionRED = 218;
var positonRed = 219;
var pLRed = 3;

lightScattering(pLRed, positonRed, lastPositionRED, in_color, sh1_gNPC, sh1_1_gNPC, sh2_gNPC, sh2_1_gNPC, sh2_2_gNPC);

var lastPosition = 163;
var futurePosition = 0;

/*atualizar_parametros_persoMain();*/
lightScattering(pLPersoMain, positionPersoMain, lastPosition, pm_color, sh1_w, sh1_1_w, sh2_w, sh2_1_w, sh2_2_w);

var aud = document.querySelector('audio');

/*-------------------------------------------------------------------------*/

let numColetados = [];
var painelMap = document.querySelector(".painel-mapa")

document.addEventListener('keydown', function(){
	if (event.key == 'w' || event.key == 'W'){ verificarPosicaoW(); painelMap.textContent = "";}
	if (event.key == 'a' || event.key == 'A'){ verificarPosicaoA(); painelMap.textContent = "";}
	if (event.key == 's' || event.key == 'S'){ verificarPosicaoS(); painelMap.textContent = "";}
	if (event.key == 'd' || event.key == 'D'){ verificarPosicaoD(); painelMap.textContent = "";}
	if (event.key == 'P'){ numColetados.push(positionPersoMain); bottonList[positionPersoMain-1].style.opacity= "0%";}
	if (event.key == 'O'){ painelMap.textContent = numColetados; alert("O Mapeamento está disponivel no Topo");}
});

function atualizar_parametros_persoMain() {
	// White position update
    bottonList[positionPersoMain-1].classList.add("aparencyPersoMain");
    bottonList[lastPosition-1].classList.remove("aparencyPersoMain");
}

function setFocus() {
  document.getElementById("foco").focus(); 
}


// OUTRO MÉTODO PARA DESATIVAR SCROLL;

/*window.onscroll = function () { window.scrollTo(0, 0); };*/

/*window.scrollTo({ left: 0, top: document.body.scrollHeight, behavior: "smooth" });*/


// MÉTODO DECIMA, PORÉM UM POUCO APRIMORADO;

/*function disableScrolling(){
    var x=window.scrollX;
    var y=window.scrollY;
    window.onscroll=function(){window.scrollTo(x, y);};
}

function enableScrolling(){
    window.onscroll=function(){};
}
*/


// MÉTODO PARA DESATIVAR O SCROLL (COM ERROS);

/*// left: 37, up: 38, right: 39, down: 40,
// spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
var keys = {37: 1, 38: 1, 39: 1, 40: 1};

function preventDefault(e) {
  e.preventDefault();
}

function preventDefaultForScrollKeys(e) {
  if (keys[e.keyCode]) {
    preventDefault(e);
    return false;
  }
}

// modern Chrome requires { passive: false } when adding event
var supportsPassive = false;
try {
  window.addEventListener("test", null, Object.defineProperty({}, 'passive', {
    get: function () { supportsPassive = true; } 
  }));
} catch(e) {}

var wheelOpt = supportsPassive ? { passive: false } : false;
var wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel';

// call this to Disable
function disableScroll() {
  window.addEventListener('DOMMouseScroll', preventDefault, false); // older FF
  window.addEventListener(wheelEvent, preventDefault, wheelOpt); // modern desktop
  window.addEventListener('touchmove', preventDefault, wheelOpt); // mobile
  window.addEventListener('keydown', preventDefaultForScrollKeys, false);
}

// call this to Enable
function enableScroll() {
  window.removeEventListener('DOMMouseScroll', preventDefault, false);
  window.removeEventListener(wheelEvent, preventDefault, wheelOpt); 
  window.removeEventListener('touchmove', preventDefault, wheelOpt);
  window.removeEventListener('keydown', preventDefaultForScrollKeys, false);
}*/










/*let list = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16];

let total = 7;
let numrest = 0;
let numsorteado = [];

while(total != numrest){
	let num = Math.floor(Math.random() * 16);
	numsorteado.push(num);
    numrest = verificar(num, list, numrest);
}

console.log(numsorteado);
var minhaSelecao = [];*/
/*------------------------------------------------------*/
/*botton.addEventListener("click", function() {
	var numselecionado = event.target.textContent;
	var numformatado = parseInt(numselecionado);
	minhaSelecao.push(numformatado);
	event.target.style.backgroundColor= "red";
	console.log(minhaSelecao);
});*/
/*---------------------------------------------------------*/
/*bottons.addEventListener("click", function() {
	for (var i = 0; i != numsorteado.length; i++){
		var n = numsorteado[i];
		var alvo = event.target.textContent;

		if (numsorteado[i] == alvo){
			event.target.style.backgroundColor= "red";
			event.target.style.boxShadow= "-5px -5px 45px red";
			return;
		}else{
			console.log("errouuu");
			event.target.style.backgroundColor= "white";
			event.target.style.boxShadow= "-5px -5px 45px white";
		}
	}
});

document.addEventListener('keydown', function(){
	if (event.key === 'q'){
		button1.style.backgroundColor= "red";
		button1.style.boxShadow= "-5px -5px 45px red";
	}

	if (event.key === 'w'){
		button2.style.backgroundColor= "red";
		button2.style.boxShadow= "-5px -5px 45px red";
	}

	if (event.ctrlKey & event.key === 'q'){
		button1.style.backgroundColor= "white";
		button1.style.boxShadow= "-5px -5px 45px white"
	}

	if (event.ctrlKey & event.key === 'w'){
		button2.style.backgroundColor= "white";
		button2.style.boxShadow= "-5px -5px 45px white"
	}
});

document.addEventListener('keyup', function(){
	if (event.key === 'q'){
		button1.style.backgroundColor= "";
		button1.style.boxShadow= "";
	}

	if (event.key === 'w'){
		button2.style.backgroundColor= "";
		button2.style.boxShadow= "";
	}

});

button1.addEventListener('scroll', function() {
	button1.style.backgroundColor= "white";
	button1.style.boxShadow= "-5px -5px 45px white";
});
*/