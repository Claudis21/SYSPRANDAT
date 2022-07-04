function ListadoDocumentos() {
    $.ajax({
        url: "/usuario/listar_documentos/",
        type: "get",
        dataType: "json",
        success: function (response) {
            if($.fn.DataTable.isDataTable('#tabla_documentos')){
                $('#tabla_documentos').DataTable().destroy();
            }
            $('#tabla_documentos tbody').html("")
            for(let i =0;i< response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';
                fila += '<td>' + response[i]["fields"]['titulo'] + '</td>';
                fila += '<td>' + response[i]["fields"]['Usuario_id'] + '</td>';
                fila += '<td>' + response[i]["fields"]['fecha_publicacion'] + '</td>';
                fila += '<td>' + response[i]["fields"]['palabras_clave'] + '</td>';
                fila += '<td>' + response[i]["fields"]['archivo'] + '</td>';
                fila += '<td>' + response[i]["fields"]['tipo_producto'] + '</td>';
                fila += '<td><button>EDITAR</button><button>ELIMINAR</button></td>';
                fila += '</tr>';
                $('#tabla_documentos tbody').append(fila);
                 
            }
            $('#tabla_documentos').DataTable({
                language: {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas", 
                    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                        "first": "Primero",
                        "last": "Ultimo",
                        "next": "Siguiente",
                        "previous": "Anterior"
                    }
                },
            });
            console.log(response)
        },
        error: function(error) { 
          console.log(error)
        }
    });
}

function registrar(){
    activarBoton();
    var data= new FormData($('#form_creacion').get(0));
	$.ajax({
      data: data,
	  url: $('#form_creacion').attr('action'),
	  type: $('#form_creacion').attr('method'),
      cache: false,
      contentType:false,
      proccessData:false, 
	  success: function(response){
        notificacionSuccess(response.mensaje);
        ListadoDocumentos();
		cerrar_modal_creacion();
	  },
	  error: function(error){
        notificacionError(errror.responseJson.mensaje); 
        mostrarErroresCreacion(error);
        activarBoton();
	  }
	});
}

$(document).ready(function () {
    ListadoDocumentos();
});