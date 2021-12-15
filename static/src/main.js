document.addEventListener('DOMContentLoaded', function(){

    if(window.location.pathname.includes('/pedidos/agregar')){

        console.log(document.querySelector('#agregarProducto'));

        // Agrega un nuevo campo para productos
        document.querySelector('#agregarProducto').addEventListener('click', function() {
            let nuevoProducto = document.querySelector('.nuevoProducto').cloneNode(true)
            nuevoProducto.classList.add('mt-3')
            nuevoProducto.childNodes[1].childNodes[5].classList.remove('invisible')
            document.querySelector('.productos').appendChild(nuevoProducto)
        })

        //Elimina un producto
        document.addEventListener('click', function(e) {
            if(e.target.id == "eliminarProducto"){
                e.target.parentElement.parentElement.remove()
            }
        })
    }

    if(window.location.pathname == "/pedidos/"){
        // Formatear fecha
        function formatear_fecha(fecha) {
            año = fecha[0]
            dia = fecha[2]
        
            if(fecha[1] == 1){
                mes = "enero"
            }
            if(fecha[1] == 2){
                mes = "febrero"
            }
            if(fecha[1] == 3){
                mes = "marzo"
            }
            if(fecha[1] == 4){
                mes = "abril"
            }
            if(fecha[1] == 5){
                mes = "mayo"
            }
            if(fecha[1] == 6){
                mes = "julio"
            }
            if(fecha[1] == 7){
                mes = "junio"
            }
            if(fecha[1] == 8){
                mes = "agosto"
            }
            if(fecha[1] == 9){
                mes = "septiembre"
            }
            if(fecha[1] == 10){
                mes = "octubre"
            }
            if(fecha[1] == 11){
                mes = "noviembre"
            }
            if(fecha[1] == 12){
                mes = "diciembre"
            }
        
            return `${dia} de ${mes} de ${año}`
        
        }
        
        let fechas_formateadas = []
        let fechas = document.querySelectorAll("#fecha")
        fechas.forEach(fecha => {
            fecha = fecha.innerHTML.split('-')
            fechas_formateadas.push(formatear_fecha(fecha))
        });

        fechas.forEach( (fecha, index) => {
            fecha.innerHTML = fechas_formateadas[index]
        });

    }

})