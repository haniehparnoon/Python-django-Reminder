$(document).ready(function () {
    console.log(URL)
    $(".click_form").submit( function () {
        // e.preventDefault();
        $.ajax({
            type: 'POST',
            url : URL,
            dataType    : 'json',
            data:{
                categoryy   :   $('#category').val(),
                titlee    :   $('#title').val(),
                descriptionn     :   $('#description').val(),
                priorityy   :   $('#priority').val(),
                due_datee         :   $('#due_date').val(),
                csrfmiddlewaretoken     :   CSRF_TOKEN,
            },
            success:function(data){
               console.log(data)
               
            },
            error: function(data) {
                alert('error');
              }
       });
        
    })
    
})