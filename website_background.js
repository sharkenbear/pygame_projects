let t;
let t2;
let rand_int;
let rand;
let rand_run;

const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

const width = canvas.width;
const height = canvas.height;

function getRandomInt(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
   // The maximum is exclusive and the minimum is inclusive
}

function draw_rect(x, y, width, height, red, green, blue) {
  ctx.fillStyle = "rgb(" + red + ", " + green + ", " + blue + ")";
  ctx.fillRect(x, y, width, height);
}

function draw_square(r_change, g_change, b_change) {
    x = getRandomInt(0, width / 50);
    y = getRandomInt(0, height / 50);

    integer = Math.floor((x + y) / 2);

    r = getRandomInt(integer - 2, integer) * 16 + r_change;
    g = getRandomInt(integer - 2, integer) * 16 + g_change;
    b = getRandomInt(integer - 2, integer) * 16 + b_change;


    if (r < 0) {
        r = 0;
    }
    else if (r > 255) {
        r = 255;
    }
    
    if (g < 0) {
        g = 0;
    }
    else if (g > 255) {
        g = 255;
    }

    if (b < 0) {
        b = 0;
    }
    else if (b > 255) {
        b = 255;
    }

    draw_rect(x * 50, y * 50, 50, 50, r, g, b);
}

function draw() {

  if (rand_run) {
    rand_int = rand_int + 1;
    if (rand_int == 1800) {
    rand = true;
    rand_run = false;
    }
  }
  t = t + 1;
  if (t < 30) {
    new_square = false;
  }
  else {
    new_square = true;
    t = 0;
  }
  if (t2 > 2 * Math.PI) {
    t2 = 0;
  }
  if ((new_square && rand) || (true && !rand)) {
    t2 = t2 + 0.0001;
    blue = -3.1;
    green = -1.5;
    red = 0;

    r_change = Math.sin(t2+red) * 100;
    g_change = Math.sin(t2+green) * 100;
    b_change = Math.sin(t2+blue) * 100;

    draw_square(r_change, g_change, b_change);
  }

  requestAnimationFrame(draw);
}

function init() {
  t = 0;
  t2 = Math.random() * 2;

  rand_int = 0;
  rand = false;
  rand_run = true;

}

init();
draw();