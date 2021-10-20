const cookieBox = document.querySelector(".wrapper"),
  acceptBtn = cookieBox.querySelector(".buttons button");

acceptBtn.onclick = () => {
  //configurado cookie por 1 mês. depois desse tempo ele expira automaticamente
  document.cookie = "CookieBy=Rangel.dev; max-age=" + 60 * 60 * 24 * 30;
  if (document.cookie) {
    cookieBox.classList.add("hide"); //esconde o card depois de aceitar uso do cookie
  } else {
    alert("Cookie não pode ser aplicado"); //mostra erro caso não puder ser aceito
  }
};

//vamos esconder o card de cookie se aceito e não expirado
let checkCookie = document.cookie.indexOf("CookieBy=Rangel.dev"); // conferi o cookie aceito
//se estiver aceito esconde o card. se não mostra ele
checkCookie != -1 ? cookieBox.classList.add("hide") : cookieBox.classList.remove("hide");
