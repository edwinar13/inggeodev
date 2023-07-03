
/***************************************
 *              NEW PROJECT
 ***************************************/

function newProject() {
    // esta funcion deja ver el formulario de nuevo proyecto
    var div = document.getElementById("NewProjec");
    div.style.display = "block";
    window.setTimeout(function () {
        div.style.opacity = 1;
        div.style.transform = 'scale(1)';
        div.style.height = "auto"

    }, 0);


    var btn = document.getElementById("btnNewProjec");
    btn.style.display = "none"
}



function newProjectCancel() {
    // esta funcion oculta el formulario de nuevo proyecto 
    var div = document.getElementById("NewProjec");
    div.style.display = "none";
    window.setTimeout(function () {
        div.style.opacity = 0;
        div.style.transform = 'scale(0)';
        div.style.height = "0"
    }, 0);
    var btn = document.getElementById("btnNewProjec");
    btn.style.display = "block";

    document.getElementById("nombre").value = "";
    document.getElementById("localizacion").value = "";
}



document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("formulario").addEventListener('submit', validarFormulario);
});

function validarFormulario(evento) {
    // esta funcion valida el formulario de nuevo proyecto
    evento.preventDefault();
    var nombre = document.getElementById('nombre');
    if (nombre.value.length == 0) {
        alert('No has escrito nada en el nombre');
        nombre.focus();
        return;
    }
    var localizacion = document.getElementById('localizacion');
    if (localizacion.value.length < 4) {
        alert('La localizacion no es válida');
        localizacion.focus();
        return;
    }
    this.submit();
}

/***************************************
 *           SEARCH PROJETC
 ***************************************/




function checkSearchProject() {
    // esta funcion verifica el checkbox para filtrar 
    // por localizacion o nombre del proyecto
    var checkB = document.getElementById("cbFilterLoc");
    var inputS = document.getElementById("inp");
    
    if (checkB.checked) {
        inputS.placeholder = "Filtrar por ubicación";
    } else {
        inputS.placeholder = "Filtrar por nombre";
    }
    searchProject();

}

function searchProject() {
    // esta funcion es la que realiza el filtrado de proyectos
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('inp');
    filter = input.value.toUpperCase();
    ul = document.getElementById("ulProjects");
    li = ul.getElementsByTagName('li');
    
    var checkB = document.getElementById("cbFilterLoc");


    for (i = 0; i < li.length; i++) {

        if (checkB.checked) {
            a = li[i].getElementsByTagName("span")[0];
        } else {
            a = li[i].getElementsByTagName("p")[0];
        }
      

        console.log(a.textContent)
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}



/***************************************
 *           CHECK FAVORITES
 ***************************************/

 function favoritesValide(id){
    

     var favorites = document.getElementById(id);

     if (favorites.checked) {
        alert(" parsar a favorito");
        //method="POST" action="/newProjectPost"
        const div = document.createElement("div"); // <div></div>
        div.id = "page";          // <div id="page"></div>
        div.className = "item";   // <div id="page" class="data"></div>
        div.style = "color: red";
    } else {
        alert("no favorito :(");
        
    }

 }


