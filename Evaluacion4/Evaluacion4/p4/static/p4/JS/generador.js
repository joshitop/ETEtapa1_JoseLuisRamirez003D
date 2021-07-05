function myFunction() {
    var numeroID = document.getElementById("numero").value;
    var a;
    var nombre = document.getElementById("nombre").value;
    var b;
    var pais = document.getElementById("pais").value;
    var c;
    var telefono = document.getElementById("telefono").value;
    var d;
    a = numeroID.substr(0,2);
    b = nombre.substr(0,2);
    c = pais.substr(-2);
    d = telefono.substr(-2);  
    document.getElementById("contrasena").value = a + "" + b.toUpperCase() + "" + c.toLowerCase() + "" + d;
}