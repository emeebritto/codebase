const senha_1 = document.querySelector("#senha_1");
const senha_2 = document.querySelector("#senha_2");
const showBtn = document.querySelector(".show");
const errorText = document.querySelector(".error-text");
const btn = document.querySelector("button");

function active() {
  if (senha_1.value.length >= 6) {
    btn.removeAttribute("disabled", "");
    btn.classList.add("active");
    senha_2.removeAttribute("disabled", "");
  } else {
    btn.setAttribute("disabled", "");
    btn.classList.remove("active");
    senha_2.setAttribute("disabled", "");
  }
}

btn.onclick = function () {
  if (senha_1.value != senha_2.value) {
    errorText.style.display = "block";
    errorText.classList.remove("matched");
    errorText.textContent = "Erro! Senhas não combinam!";
    return false;
  } else {
    errorText.style.display = "block";
    errorText.classList.add("matched");
    errorText.textContent = "Perfeito! Senha confirmada";
    return false;
  }
};

function active_2() {
  if (senha_2.value != "") {
    showBtn.style.display = "block";
    showBtn.onclick = function () {
      if (senha_1.type == "password" && senha_2.type == "password") {
        senha_1.type = "text";
        senha_2.type = "text";
        this.textContent = "Hide";
        this.classList.add("active");
      } else {
        senha_1.type = "password";
        senha_2.type = "password";
        this.textContent = "Show";
        this.classList.remove("active");
      }
    };
  } else {
    showBtn.style.display = "none";
  }
}
