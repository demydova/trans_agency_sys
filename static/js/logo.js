/*Funktion initPage() beim Laden der Seite referenzieren und "bereitstellen"*/
window.onload = initPage;
//Variable, die Radius der Kreis bestimmt
var amplitude = 40;
//Variable, die Drehungswinckel bestimmt
var position = 0;
//Variable obj ist eine Martix, die alle Objekte speichert
var obj;
//Variable, die ruft Funktion fly() mit der Zeitabstand von 10 ms wieder
var animate;
/*referenziert alle Funktionen, die im Falle eines events
(hier onclick und onmouseover) ausgeführt werden sollen*/
function initPage() {

    /*Zugriff über den Elementnamen*/
//Wenn der Mauszeiger aud der Logobereich plaziert, wird Funktion fly() aufgerufen
    document.getElementById('logo').onmouseover = function () {
        fly();
    }
    //Wenn der Mauszeiger die Logobereich verlaesst, wird Funktion clearTimeout() aufgerufen
    document.getElementById('logo').onmouseout = function () {
      //Funktion clearTimeout() stellt alle Positionen auf 0 px wieder, und es passiert keine Animation mehr 
        clearTimeout(animate);
        for (var i = 0; i < obj.length; i++) {

            obj[i].style.left = 0 + 'px';
            obj[i].style.top = 0 + 'px';
        }

    }
    //Variable obj wird initialisiert
    obj = document.getElementsByClassName('platzhalter');
    for (var i = 0; i < obj.length; i++) {
        obj[i].style.position = 'relative';
        obj[i].style.left = '0px';
        obj[i].style.top = '0px';
    }
}

/*Funktionen, die die eigentliche Arbeit am HTML-Dokument ausführen*/



function fly() {
    position = position + 1;
    for (var i = 0; i < obj.length; i++) {
        obj[i].style.left = amplitude * Math.sin(i + position / 10) * 0.1 + 'px';
        obj[i].style.top = amplitude * Math.cos(i + position / 10) * 0.1 + 'px';
    }
    animate = setTimeout(fly, 10);
}