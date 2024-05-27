let loadbtn = document.getElementById("loadbtn");
let loader = document.getElementById("loader");
let load_status = document.getElementById("load-status");
let sq1 = document.getElementById("sq1");
let sq2 = document.getElementById("sq2");
let epochs = document.getElementById("epochs");
let form = document.getElementById("form");

loadbtn.style.display = "block";
load_status.style.display = "block";
sq1.style.display = "block";
sq2.style.display = "block";

function loadModels(){
    loadbtn.style.display = "none";
    sq1.style.display = "none";
    sq2.style.display = "none";
    epochs.style.display = "none";
    form.style.display = "none";
}