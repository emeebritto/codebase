const detect = document.querySelector("#detect"),
  button = document.querySelector("button"),
  wrapper = document.querySelector(".wrapper");

//Estas são algumas das possiveis classes que o adblock usará para evitar renderizar a página
let adClasses = ["ad", "ads", "adsbox", "ad-placement", "doubleclick", "ad-placeholder", "ad-badge"];
for (let item of adClasses) {
  detect.classList.add(item); //adiciona todo os items do array no elemento detect
}

//pega o valor da propriedade display do elemento detect
let getProperty = window.getComputedStyle(detect).getPropertyValue("display");

button.addEventListener("click", () => {
  wrapper.classList.remove("show"); // esconde o popup no click do botão
});

// Se wrapper não conter class "show" o checar adblock é mostrado ou não
if (!wrapper.classList.contains("show")) {
  // Se o valor da propriedade display é "none" então mostra o popup se não esconde ele
  getProperty == "none" ? wrapper.classList.add("show") : wrapper.classList.remove("show");
}
