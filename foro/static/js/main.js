function validarFormulario(){
    var txtContrasena = document.getElementById('contrasena').value;
    var txtConfirmContra = document.getElementById('confirmContrasena').value;
    var txtDia = document.getElementById("fechaDia");
    var txtMes = document.getElementById('fechaMes');
    var txtAnno = document.getElementById('fechaAnno');
    var fechaNacimiento = txtDia.value + "/" + txtMes.value + "/" + txtAnno.value;

    if( txtConfirmContra != txtContrasena ){
        alert('Error: Las contraseñas no coinciden. Vuelve a intentarlo.');
        document.datosRegistro.confirmContrasena.value = "";
        document.datosRegistro.confirmContrasena.focus();
        return false;
    } 
        
    

}

function soloLetrasNumeros(e) {
    key = e.keyCode || e.which; //guarda el codigo de la tecla presionada--- usa wich o keyCode, dependiendo del soporte del navegador
    tecla = String.fromCharCode(key); //obtiene y guarda el caracter presionado. 
    letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"; //variable que guarda todas las teclas permitidas por mi
    especiales = [8, 37, 39, 46]; //guarda el keyCode de teclas especiales (BackSpace, flecha izquierda, flecha derecha, suprimir)

    //Verifica si la tecla presionada es una de las teclas especiales
    tecla_especial = false
    for(var i in especiales) {
        if(key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    //Condición que devuelve falso si la tecla no se encuentra dentro de la lista permitida, Ó si es un ".","'","%"
    if( ((letras.indexOf(tecla) == -1) && (!tecla_especial)) || (tecla == "." || tecla == "'" || tecla == "%"))
        return false;
}

function soloNumeros(e) {
    key = e.keyCode || e.which; //guarda el codigo de la tecla presionada--- usa wich o keyCode, dependiendo del soporte del navegador
    tecla = String.fromCharCode(key); //obtiene y guarda el caracter presionado. 
    letras = "0123456789"; //variable que guarda todas las teclas permitidas por mi
    especiales = [8, 37, 39, 46]; //guarda el keyCode de teclas especiales (BackSpace, flecha izquierda, flecha derecha, suprimir)

    //Verifica si la tecla presionada es una de las teclas especiales
    tecla_especial = false
    for(var i in especiales) {
        if(key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    //Condición que devuelve falso si la tecla no se encuentra dentro de la lista permitida, Ó si es un ".","'","%"
    if( ((letras.indexOf(tecla) == -1) && (!tecla_especial)) || (tecla == "." || tecla == "'" || tecla == "%"))
        return false;
}

//Corta desde el primer numero hasta el 2do para dia y mes, y hasta el 4to para el año 
function largoFechaNac(){
    var txtDia = document.getElementById("fechaDia");
    var txtMes = document.getElementById('fechaMes');
    var txtAnno = document.getElementById('fechaAnno');

    if(txtDia.value.length > 2){
        txtDia.value = txtDia.value.slice(0,2);
    }
    if(txtMes.value.length > 2){
        txtMes.value = txtMes.value.slice(0,2);
    }
    if(txtAnno.value.length > 4){
        txtAnno.value = txtAnno.value.slice(0,4);
    }
}


//Funcion Modo Oscuro - Main Tag
function modoOscuro() {
    x = document.getElementById('main-container');
    y = document.getElementById('redireccionar');
    isChecked = false;
    btnCheck = document.getElementById('modoOscuro');

    if (btnCheck.checked) {
        isChecked  = true;
    }else{
        isChecked = false;
    }
    
    if (isChecked) {
        x.style.background = "#1e1d1e";
        x.style.color = "#fff";
        y.style.color = "#fff";
    }
    else{
        x.style.background = "#c3e3ff";
        x.style.color = "#000";
        y.style.color = "#000";
    
    }
}

//Menu Desplegable
function desplegarMenu(){
     x = document.getElementById("menu-desplegable");
     //Condición si es que el menu NAV tiene como display igual valor y tipo a 'none'
     if (x.style.display === "none") {
         x.style.display = "block";     
    }else{
         x.style.display = "none";
     }
}



// window.matchMedia -- Para realizar Media Queries en JS
//Llamar método API, lo que nos permite comprobar si se cumple una @media query y ejecutar una función cuando cambia de estado
if (matchMedia) {
    //Creo constante de media query ancho min. 901px
    const mq = window.matchMedia("(min-width: 901px)");
    //Agrego un evento disparador a mi media query sobre el cambio de ancho de la ventana.
    mq.addListener(cambioAncho);
    //Enlazar mediaquery con función del cambio de ancho
    cambioAncho(mq);
}
    
// cambio de media query 
function cambioAncho(mq) {
    var x = document.getElementById("menu-desplegable");
    //Condicion, si el ancho es por lo menos 901px entonces muestra NAV, sino lo oculta
    if (mq.matches) {
        x.style.display = "block";
    }else{
        x.style.display = "none";
    }
}



