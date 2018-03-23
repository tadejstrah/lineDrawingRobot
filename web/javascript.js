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
var drawing = false;

window.onload = function() {
    canvas = document.getElementById('myCanvas');
    canvasContext = canvas.getContext('2d');

    var FPS = 60;

    setInterval(function(){drawEverything();},1000/FPS);


    canvas.addEventListener('mousemove',
                            function(evt){
        if(currentLineLength >= lineLen || drawing == false) return;
        var mousePos = calculateMousePos(evt);
        Xcurrent = mousePos.x;
        Ycurrent = mousePos.y;
    }
                           )
    canvas.addEventListener('mousedown', function(evt) {
        handleMouseClick(evt);

    });
    canvas.addEventListener('mouseup', function() {
        currentLineLength = lineLen;
        drawing=false;
    });
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
        //console.log(currentLineLength);

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

function handleMouseClick(evt){

    console.log(Xs)
    console.log(Ys)
    currentLineLength = 0;

    Xs = [];
    Ys = [];
    canvasContext.fillStyle = 'lightblue';
    canvasContext.fillRect(0,0,canvas.width,canvas.height);
    drawing=true;
    var tmp = calculateMousePos(evt);
    Xprev=tmp.x;Yprev=tmp.y;
    Xcurrent=Xprev;Ycurrent=Yprev;
    
   
    //var blob = new Blob([Xs,Ys],{type:"text/plain;charset=utf-8"});
    //FileSaver.saveAs(blob, "test123.txt")

    return
}

function sendData(){
    console.log("tuki dodej funkcijo ki pošlje POST request RPI-ju");
    return
}