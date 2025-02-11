// Seleccionar el campo de resultado
const resultado = document.getElementById("resultado");

// Seleccionar todos los botones de números y operadores
const botones = document.querySelectorAll(".numero, .operador");

// Seleccionar el botón de borrar
const botonBorrar = document.getElementById("borrar");

//Seleccionar el boton =
const botonIgual = document.getElementById("igual");

// Agregar evento de clic a cada botón
botones.forEach(boton => {
    boton.addEventListener("click", () => {
        resultado.value += boton.textContent; // Agregar el número u operador al resultado
    });
});


// Agregar evento de clic para borrar el contenido del input
botonBorrar.addEventListener("click", () => {
    resultado.value = ""; // Vaciar la pantalla
});

botonIgual.addEventListener("click", () => {
    fetch ('http://127.0.0.1:5000/calcular', {
        method: 'POST', // Metodo HTTP para enviar datos
        headers: {'Content-Type': 'application/json'}, // Especificamos que enviamos JSON
        body: JSON.stringify({ expresion: resultado.value.replace('x', '*')}) // Convertimos "x" en "*"

    })
    .then(Response=> Response.json())//Convertir respuesta en JSON
    .then(data => {
        //Condicional para saber si la respuesta tiene un resultado valido
        if (data.resultado !== undefined){
            resultado.value = data.resultado;
        }
        else{
            resultado.value = "Error en la operacion";
        }
    })
    .catch(() => resultado.value = "Error en la conexion con el API")
})
