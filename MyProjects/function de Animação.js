function testess(){

    var tl = gsap.timeline({repeat: 1, yoyo: true});

    tl.to(".nav_float", 3, {left: 340, rotate: 56}).to(".nav_float", 3, {y:123})
}