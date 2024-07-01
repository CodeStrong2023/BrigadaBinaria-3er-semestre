/* Juego Avatar - Brigada Binaria */

let ataqueJugador;
let ataqueEnemigo;
let vidasJugador = 3;
let vidasEnemigo = 3;

function iniciarJuego() {
    let seccionSeleccionarAtaque = document.getElementById("seleccionar-ataque");
    seccionSeleccionarAtaque.style.display = "none";

    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    let botonPunio = document.getElementById('boton-punio');
    botonPunio.addEventListener('click', ataquePunio);
    let botonPatada = document.getElementById('boton-patada');
    botonPatada.addEventListener('click', ataquePatada);
    let botonBarrida = document.getElementById('boton-barrida');
    botonBarrida.addEventListener('click', ataqueBarrida);

    let botonReiniciar = document.getElementById('boton-reiniciar');
    botonReiniciar.addEventListener('click', reiniciarJuego);

    let botonReglas = document.getElementById('boton-reglas');
    botonReglas.addEventListener('click', mostrarReglas);

    let seccionReiniciar = document.getElementById("reiniciar");
    seccionReiniciar.style.display = "none";
}

function mostrarReglas() {
    let seccionReglas = document.getElementById("reglas-juego");
    seccionReglas.style.display = "block";
}

function seleccionarPersonajeJugador() {
    let inputZuko = document.getElementById('zuko');
    let inputKatara = document.getElementById('katara');
    let inputAang = document.getElementById('aang');
    let inputToph = document.getElementById('toph');
    let spanPersonajeJugador = document.getElementById('personaje-jugador');

    if (inputZuko.checked) {
        spanPersonajeJugador.innerHTML = 'Zuko';
    } else if (inputKatara.checked) {
        spanPersonajeJugador.innerHTML = 'Katara';
    } else if (inputAang.checked) {
        spanPersonajeJugador.innerHTML = 'Aang';
    } else if (inputToph.checked) {
        spanPersonajeJugador.innerHTML = 'Toph';
    } else {
        alert('Selecciona un personaje');
        return;
    }

    let seccionSeleccionarPersonaje = document.getElementById("seleccionar-personaje");
    seccionSeleccionarPersonaje.style.display = "none";

    let seccionReglas = document.getElementById("reglas-juego");
    seccionReglas.style.display = "none";

    let seccionSeleccionarAtaque = document.getElementById("seleccionar-ataque");
    seccionSeleccionarAtaque.style.display = "block";

    seleccionarPersonajeEnemigo();
}

function seleccionarPersonajeEnemigo() {
    let personajeAleatorio = aleatorio(1, 4);
    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo');

    if (personajeAleatorio == 1) {
        spanPersonajeEnemigo.innerHTML = 'Zuko';
    } else if (personajeAleatorio == 2) {
        spanPersonajeEnemigo.innerHTML = 'Katara';
    } else if (personajeAleatorio == 3) {
        spanPersonajeEnemigo.innerHTML = 'Aang';
    } else {
        spanPersonajeEnemigo.innerHTML = 'Toph';
    }
}

function ataquePunio() {
    ataqueJugador = 'Punio';
    ataqueAleatorioEnemigo();
}

function ataquePatada() {
    ataqueJugador = 'Patada';
    ataqueAleatorioEnemigo();
}

function ataqueBarrida() {
    ataqueJugador = 'Barrida';
    ataqueAleatorioEnemigo();
}

function ataqueAleatorioEnemigo() {
    let ataqueAleatorio = aleatorio(1, 3);

    if (ataqueAleatorio == 1) {
        ataqueEnemigo = 'Punio';
    } else if (ataqueAleatorio == 2) {
        ataqueEnemigo = 'Patada';
    } else {
        ataqueEnemigo = 'Barrida';
    }

    combate();
}

function reiniciarJuego() {
    location.reload();
}

function combate() {
    let spanVidasJugador = document.getElementById("vidas-jugador");
    let spanVidasEnemigo = document.getElementById("vidas-enemigo");

    if (ataqueEnemigo == ataqueJugador) {
        crearMensaje("EMPATE");
    } else if (
        (ataqueJugador == "Punio" && ataqueEnemigo == "Barrida") ||
        (ataqueJugador == "Patada" && ataqueEnemigo == "Punio") ||
        (ataqueJugador == "Barrida" && ataqueEnemigo == "Patada")
    ) {
        crearMensaje("GANASTE");
        vidasEnemigo--;
        spanVidasEnemigo.innerHTML = vidasEnemigo;
    } else {
        crearMensaje("PERDISTE");
        vidasJugador--;
        spanVidasJugador.innerHTML = vidasJugador;
    }

    revisarVidas();
}

function revisarVidas() {
    if (vidasEnemigo == 0) {
        crearMensajeFinal("FELICITACIONES GANASTE 🏆");
    } else if (vidasJugador == 0) {
        crearMensajeFinal("PERDISTE, NO TE RINDAS 😭");
    }
}

function crearMensajeFinal(resultadoFinal) {
    let sectionMensaje = document.getElementById("mensajes");
    let parrafo = document.createElement("p");

    parrafo.innerHTML = resultadoFinal;
    sectionMensaje.appendChild(parrafo);

    document.getElementById('boton-punio').disabled = true;
    document.getElementById('boton-patada').disabled = true;
    document.getElementById('boton-barrida').disabled = true;

    let seccionReiniciar = document.getElementById("reiniciar");
    seccionReiniciar.style.display = "block";
}

function crearMensaje(resultado) {
    let sectionMensaje = document.getElementById("mensajes");
    let parrafo = document.createElement("p");

    parrafo.innerHTML = "Tu personaje atacó con " + ataqueJugador + ", el personaje del enemigo atacó con " + ataqueEnemigo + " - " + resultado;
    sectionMensaje.appendChild(parrafo);
}

function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

window.addEventListener('load', iniciarJuego);
