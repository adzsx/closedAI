var canvas, ctx, flag = false,
        prevX = 0,
        currX = 0,
        prevY = 0,
        currY = 0,
        dot_flag = false;

var x = "white",
    y = 15;

function init() {
    canvas = document.getElementById('can');
    ctx = canvas.getContext("2d");
    w = canvas.width;
    h = canvas.height;

    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false);
}

function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = x;
    ctx.lineWidth = y;
    ctx.lineCap = "round";
    ctx.stroke();
}

function erase() {
    ctx.clearRect(0, 0, w, h);
    document.getElementById("canvasimg").style.display = "none";
}

function findxy(res, e) {
    if (res == 'down') {
        console.log(canvas.offsetLeft, canvas.offsetTop);
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft+140;
        currY = e.clientY - canvas.offsetTop+140;

        flag = true;
        dot_flag = true;
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = x;
            ctx.fillRect(currX, currY, 2, 2);
            ctx.closePath();
            dot_flag = false;
        }
    }
    if (res == 'up' || res == "out") {
        flag = false;
    }
    if (res == 'move') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft+140;
            currY = e.clientY - canvas.offsetTop+140;
            draw();
        }
    }
}

function post(path, params, method='post') {

    // The rest of this code assumes you are not using a library.
    // It can be made less verbose if you use one.
    const form = document.createElement('form');
    form.method = method;
    form.action = path;
  
    for (const key in params) {
      if (params.hasOwnProperty(key)) {
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = key;
        hiddenField.value = params[key];
  
        form.appendChild(hiddenField);
      }
    }
  
    document.body.appendChild(form);
    form.submit();
  }

function exportCanvasData(){
    let can = document.getElementById("can");

  const ctx = can.getContext('2d');

  // Get the image data from the canvas
  const imageData = ctx.getImageData(0, 0, can.width, can.height);
  const data = imageData.data;
  console.log(data);
  const grayscaleArray = [];
  for (let i = 3; i < data.length; i += 4) {
      grayscaleArray.push(data[i]/255);
    }
    console.log("Can height: ", can.height);
  console.log("Data length: ", grayscaleArray.length)
  post("#", {"data": grayscaleArray});
}