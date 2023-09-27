var publicaciones = document.getElementById('publicaciones');
var html = '';
//funcion cargar post desde /api/posts
async function getPosts() {
    const res = await fetch('/api/posts');
    const data = await res.json();
    console.log(data);
    publicaciones.innerHTML = '';
    //voltiamos el array para que se muestre primero el ultimo post
    data.reverse();
    data.forEach(post => {
        console.log(post.image);
        html += `
<div class="card lg:mx-0 uk-animation-slide-bottom-small">

                        <!-- post header-->
                        <div class="flex justify-between items-center lg:p-4 p-2.5">
                            <div class="flex flex-1 items-center space-x-4">
                                <a href="#">
                                    <img src="${post.image}"
                                        class="bg-gray-200 border border-white rounded-full w-10 h-10">
                                </a>
                                <div class="flex-1 font-semibold capitalize">
                                    <a href="#" class="text-black dark:text-gray-100"> ${post.username}</a>
                                    <div class="text-gray-700 flex items-center space-x-2"> 5 <span> hrs </span>
                                        <ion-icon name="people"></ion-icon>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <a href="#"> <i
                                        class="icon-feather-more-horizontal text-2xl hover:bg-gray-200 rounded-full p-2 transition -mr-1 dark:hover:bg-gray-700"></i>
                                </a>
                                <div class="bg-white w-56 shadow-md mx-auto p-2 mt-12 rounded-md text-gray-500 hidden text-base border border-gray-100 dark:bg-gray-900 dark:text-gray-100 dark:border-gray-700"
                                    uk-drop="mode: click;pos: bottom-right;animation: uk-animation-slide-bottom-small">

                                    <ul class="space-y-1">
                                        <li>
                                            <a href="#"
                                                class="flex items-center px-3 py-2 hover:bg-gray-200 hover:text-gray-800 rounded-md dark:hover:bg-gray-800">
                                                <i class="uil-share-alt mr-1"></i> Compartir
                                            </a>
                                        </li>

                                        ${post.username == document.getElementById('userUsername').value ? `
                                        <li>
                                            <a href="#"
                                                class="flex items-center px-3 py-2 hover:bg-gray-200 hover:text-gray-800 rounded-md dark:hover:bg-gray-800">
                                                <i class="uil-edit-alt mr-1"></i> Editar publicacion
                                            </a>
                                        </li>
                                        <li>
                                            <a href="#"
                                                class="flex items-center px-3 py-2 hover:bg-gray-200 hover:text-gray-800 rounded-md dark:hover:bg-gray-800">
                                                <i class="uil-comment-slash mr-1"></i> Desactivar comentarios
                                            </a>
                                        </li>
                                        ` : ``}
                                        

                                        <li>
                                            <a href="#"
                                                class="flex items-center px-3 py-2 hover:bg-gray-200 hover:text-gray-800 rounded-md dark:hover:bg-gray-800">
                                                <i class="uil-favorite mr-1"></i> Agregar a favoritos
                                            </a>
                                        </li>
                                        <li>
                                            <hr class="-mx-2 my-2 dark:border-gray-800">
                                        </li>

                                        ${post.username == document.getElementById('userUsername').value ? `
                                        <li>
                                            <a href="#"
                                                class="flex items-center px-3 py-2 text-red-500 hover:bg-red-100 hover:text-red-500 rounded-md dark:hover:bg-red-600">
                                                <i class="uil-trash-alt mr-1"></i> Eliminar
                                            </a>
                                        </li>
                                        ` : ``}
                                    </ul>

                                </div>
                            </div>
                        </div>

                        <div uk-lightbox>
                            <a href="${post.image}">
                                <img src="${post.image}" alt="" class="max-h-96 w-full object-cover">
                            </a>
                        </div>


                        <div class="p-4 space-y-3">

                            <div class="flex space-x-4 lg:font-bold">
                                <a href="#" class="flex items-center space-x-2">
                                    <div class="p-2 rounded-full  text-black lg:bg-gray-100 dark:bg-gray-600">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
                                            fill="currentColor" width="22" height="22" class="dark:text-gray-100">
                                            <path
                                                d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z" />
                                        </svg>
                                    </div>
                                    <div> Like</div>
                                </a>
                                <button class="flex items-center space-x-2" onclick="cargarComentarios('comentarios${post.id}',${post.id});">
                                    <div class="p-2 rounded-full  text-black lg:bg-gray-100 dark:bg-gray-600">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
                                            fill="currentColor" width="22" height="22" class="dark:text-gray-100">
                                            <path fill-rule="evenodd"
                                                d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z"
                                                clip-rule="evenodd" />
                                        </svg>
                                    </div>
                                    <div> Comentarios</div>
                                </button>
                                <a href="#" class="flex items-center space-x-2 flex-1 justify-end">
                                    <div class="p-2 rounded-full  text-black lg:bg-gray-100 dark:bg-gray-600">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
                                            fill="currentColor" width="22" height="22" class="dark:text-gray-100">
                                            <path
                                                d="M15 8a3 3 0 10-2.977-2.63l-4.94 2.47a3 3 0 100 4.319l4.94 2.47a3 3 0 10.895-1.789l-4.94-2.47a3.027 3.027 0 000-.74l4.94-2.47C13.456 7.68 14.19 8 15 8z" />
                                        </svg>
                                    </div>
                                    <div> Compartir</div>
                                </a>
                            </div>
                            <div id="comentarios${post.id}" style="display: none;">

                            <div id="comentarios2${post.id}">
                            </div>
                            <div class="bg-gray-100 rounded-full relative dark:bg-gray-800 border-t">
                            <form action="/api/comentar/" id="formC${post.id}" method="POST">
                                <input placeholder="Agrega tu comentario.." required type="text"
                                    class="bg-transparent max-h-10 shadow-none px-5" id="inputC${post.id}" name="body">
                                    <input type="hidden" name="id_post" value="${post.id}">
                                </form>
                                    <button class="absolute right-3 inset-y-0 flex items-center btn btn-success" onclick="enviarComentario(${post.id});">
                                     >
                                        Publicar
                                    </button>
                                
                                    
                                
                            </div>
                            
                            </div>

                        </div>

                    </div>
                    <br>
`;
    });

    publicaciones.innerHTML = html;
}

async function cargarComentarios(div, id) {
    var div = document.getElementById(div);
    var div2 = document.getElementById('comentarios2' + id);
    var html = '';
    if (div.style.display == "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
    const res = await fetch('/api/comentarios/' + id);
    const data = await res.json();
    console.log(data);
    div2.innerHTML = '';

    data.reverse();
    data.forEach(post => {

        html += `
        <div class="flex items-center space-x-3 pt-2">
                                
                            </div>

                            <div class="border-t py-4 space-y-4 dark:border-gray-600">
                                <div class="flex">
                                    <div class="w-10 h-10 rounded-full relative flex-shrink-0">
                                        <img src="${post.userimage}" alt=""
                                            class="absolute h-full rounded-full w-full">
                                    </div>
                                    <div>
                                        <div
                                            class="text-gray-700 py-2 px-3 rounded-md bg-gray-100 relative lg:ml-5 ml-2 lg:mr-12  dark:bg-gray-800 dark:text-gray-100">
                                            <p class="leading-6">${post.body}</p>
                                            <div
                                                class="absolute w-3 h-3 top-3 -left-1 bg-gray-100 transform rotate-45 dark:bg-gray-800">
                                            </div>
                                        </div>
                                        
                                            ${post.username == document.getElementById('userUsername').value ? `
                                    <button class="btn btn-danger" onclick="eliminarComentario(${post.id},${id});">
                                    <i class="uil-trash-alt"></i>
                                    </button>
                                    ` : ``}
                                        </div>
                                    </div>
                                    
                                </div>
                                

                            </div>


                            
                            `

    }
    );
    div2.innerHTML = html;

}
async function cargarComentarios2(id) {
    
    var div2 = document.getElementById('comentarios2' + id);
    var html = '';
    const res = await fetch('/api/comentarios/' + id);
    const data = await res.json();
    console.log(data);
    div2.innerHTML = '';

    data.reverse();
    data.forEach(post => {

        html += `
        <div class="flex items-center space-x-3 pt-2">
                                
                            </div>

                            <div class="border-t py-4 space-y-4 dark:border-gray-600">
                                <div class="flex">
                                    <div class="w-10 h-10 rounded-full relative flex-shrink-0">
                                        <img src="${post.userimage}" alt=""
                                            class="absolute h-full rounded-full w-full">
                                    </div>
                                    <div>
                                        <div
                                            class="text-gray-700 py-2 px-3 rounded-md bg-gray-100 relative lg:ml-5 ml-2 lg:mr-12  dark:bg-gray-800 dark:text-gray-100">
                                            <p class="leading-6">${post.body}</p>
                                            <div
                                                class="absolute w-3 h-3 top-3 -left-1 bg-gray-100 transform rotate-45 dark:bg-gray-800">
                                            </div>
                                        </div>
                                        
                                            ${post.username == document.getElementById('userUsername').value ? `
                                    <button class="btn btn-danger" onclick="eliminarComentario(${post.id},${id});">
                                    <i class="uil-trash-alt"></i>
                                    </button>
                                    ` : ``}
                                        </div>
                                    </div>
                                    
                                </div>
                                

                            </div>


                            
                            `

    }
    );
    div2.innerHTML = html;

}

function enviarComentario(id) {
    if (document.getElementById('inputC' + id).value == "") {
        return;
    }
    var form = document.getElementById('formC' + id);
    fetch("/api/comentar/", {
        method: "POST",
        body: new FormData(form)
    }).then(function (res) {
        return res.json();
    }).then(function (data) {
        console.log(data);
        form.reset();
        cargarComentarios2('comentarios' + id, id);
    });



}
function eliminarComentario(id,div2) {
    //fetch get
    
    fetch("/eliminarcomentarios/" + id)
    .then(function (res) {
        console.log(res);
        cargarComentarios2(div2);
    });
}