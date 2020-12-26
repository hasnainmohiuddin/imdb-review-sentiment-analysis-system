$(function(){
    $("#calculateButton").click(function(){
        if (!$("#review").val()) {
            $('#error_msg').removeClass('fade');
        }
        else{
            $('#error_msg').addClass('fade');
        }
    });
    $('#model_name').change(showResult);
    showM();
});

function showM(){
    console.log($("#showM").text().replace(/^\s+|\s+$/g,''))
    console.log($("#showM").text().replace(/^\s+|\s+$/g,'') == '');
    if(!($("#showM").text().replace(/^\s+|\s+$/g,'') == '')){
        $("#resultmodal").modal("show");
    }
}

function showResult(){
    var value = $("#model_name option:selected").attr('value');
    $("#resultmodal").modal("show");
    $("#prediction").empty();
    $("#prediction").append(`<h1>${value}</h1>`);
}
    
