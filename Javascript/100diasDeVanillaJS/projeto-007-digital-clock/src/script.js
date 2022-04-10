function clock() {
  let hour = document.getElementById("hour");
  let minute = document.getElementById("minute");
  let seconds = document.getElementById("seconds");

  let h = new Date().getHours();
  let m = new Date().getMinutes();
  let s = new Date().getSeconds();

  //Adicionar zero no começo do numero se for menor que dez
  h = h < 10 ? "0" + h : h;
  m = m < 10 ? "0" + m : m;
  s = s < 10 ? "0" + s : s;

  hour.innerHTML = h;
  minute.innerHTML = m;
  seconds.innerHTML = s;
}

var interval = setInterval(clock, 1000);
