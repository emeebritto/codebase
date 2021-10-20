const copyText = document.querySelector("#copyText");
const pasteText = document.querySelector("#pasteText");
const button = document.querySelector("button");
const tooltip = document.querySelector(".tooltip");

button.addEventListener("click", function () {
  copyText.select();
  pasteText.value = "";
  if (document.execCommand("copy")) {
    pasteText.focus();
    tooltip.classList.add("show");
    setTimeout(function () {
      tooltip.classList.remove("show");
    }, 700);
  } else {
    alert("Algo parece errado...");
  }
});
