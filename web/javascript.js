var canvas;
var canvasContext;

var Xcurrent = 250;
var Ycurrent = 150;
var Xprev = 250;
var Yprev = 150;

var Xs = []
var Ys = []

var lineLen = 2000;

var currentLineLength = 0; 

window.onload = function() {
  canvas = document.getElementById('myCanvas');
  canvasContext = canvas.getContext('2d');
  
  var FPS = 60;

  setInterval(function(){drawEverything();},1000/FPS);
  

  canvas.addEventListener('mousemove',
    function(evt){
      var mousePos = calculateMousePos(evt);
      Xcurrent = mousePos.x;
      Ycurrent = mousePos.y;
    }
    )
  canvas.addEventListener('mousedown', handleMouseClick);
  }



function calculateMousePos(evt) {
  var rect = canvas.getBoundingClientRect();
  var root = document.documentElement;
  var mouseX = evt.clientX - rect.left - root.scrollTop;
  var mouseY = evt.clientY - rect.top - root.scrollTop;
  Xs.push(Xcurrent);
  Ys.push(Ycurrent); 
  return{
    x:mouseX,
    y:mouseY
}
}


function chooseLength() {
    var length1 = prompt("določi dolžino (nekje med 500 in 10k)");
    if (length1 != null) {
       lineLen = length1;
        canvasContext.fillStyle = 'lightblue';
       canvasContext.fillRect(0,0,canvas.width,canvas.height);
       currentLineLength = 0;
       Xs = [];
       Ys = [];


    }
}


function drawEverything(){
  if(Xprev != Xcurrent && currentLineLength < lineLen){

  currentLineLength += Math.sqrt((Yprev - Ycurrent)*(Yprev - Ycurrent) + (Xprev - Xcurrent)*(Xprev - Xcurrent));
  console.log(currentLineLength);

  canvasContext.stroke();
  canvasContext.beginPath();
  canvasContext.moveTo(Xprev,Yprev);
  canvasContext.lineTo(Xcurrent,Ycurrent);
  canvasContext.stroke();

  Xprev = Xcurrent;
  Yprev = Ycurrent;
}
  return
}

function handleMouseClick(){
  console.log(Xs)
  console.log(Ys)
  return
}

function sendData(){
  console.log("tuki dodej funkcijo ki pošlje POST request RPI-ju");
  return
}