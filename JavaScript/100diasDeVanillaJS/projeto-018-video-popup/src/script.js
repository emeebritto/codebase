function toggle() {
  var trailer = document.querySelector(".trailer");
  var video = document.querySelector("video");
  trailer.classList.toggle("active");
  video.pause();
  video.currentTime = 0;
}
