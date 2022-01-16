/* Firebase Setup */
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.3/firebase-app.js";
import {getDatabase, ref, set, child, update, remove} 
from "https://www.gstatic.com/firebasejs/9.6.3/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyBIIYAufROoblUDgPahtLoWfvDNlrLAWw0",
  authDomain: "led-control-fc3ce.firebaseapp.com",
  databaseURL: "https://led-control-fc3ce-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "led-control-fc3ce",
  storageBucket: "led-control-fc3ce.appspot.com",
  messagingSenderId: "167274057880",
  appId: "1:167274057880:web:88c680ffd66c4b2dfac0ed",
  measurementId: "G-0JTZ7G1T52"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase();

/* Interaction with page and Firebase */

const btn_ligar = document.getElementById("btn-ligar");
const btn_desligar = document.getElementById("btn-desligar");
const text_status = document.getElementById('text-status');

window.addEventListener('load', function(e){
    e.preventDefault();
    set(ref(db, "LED"),{
       "LED":"OFF"
    }).then(() =>{
        console.log("LED Iniciado desligado")
    })
 })

btn_ligar.addEventListener('click', function(e){
   e.preventDefault();
   set(ref(db, "LED"),{
      "LED":"ON"
   }).then(() =>{
    btn_ligar.classList.add("disabled");
    btn_desligar.classList.remove("disabled")
    text_status.innerHTML = "O led está ligado!"
   })
})

btn_desligar.addEventListener('click', function(e){
    e.preventDefault();
    set(ref(db, "LED"),{
       "LED":"OFF"
    }).then(() =>{
        btn_ligar.classList.remove("disabled");
        btn_desligar.classList.add("disabled")
        text_status.innerHTML = "O led está desligado!"
    })
 })