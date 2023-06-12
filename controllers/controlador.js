let btnGenerar = document.getElementById("idbtngenerarreporte");
let btnOcultarReporte = document.getElementById("idbtnocultararreporte");
let contenedor = document.getElementById("conenedor");



btnGenerar.addEventListener('click', (evento) =>{
    evento.preventDefault()
    contenedor.classList.remove("d-none");
    let nombre = document.getElementById("nombre").value;
    let mensaje = document.getElementById("mensaje");
    mensaje.textContent = `Apreciado usuario: ${nombre}, hemos generado su reporte `
})
