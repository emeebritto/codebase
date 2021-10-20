const cursor = document.querySelector(".cursor");
var timeout;

//segue o cursor ao movimento do mouse
document.addEventListener("mousemove", (e) => {
  let x = e.pageX;
  let y = e.pageY;

  cursor.style.top = y + "px";
  cursor.style.left = x + "px";
  cursor.style.display = "block";

  //efeito do mouse ao parar
  function mouseStopped() {
    cursor.style.display = "none";
  }
  clearTimeout(timeout);
  timeout = setTimeout(mouseStopped, 2000);
});

//efeito do mouse ao sair de tela
document.addEventListener("mouseout", () => {
  cursor.style.display = "none";
});
