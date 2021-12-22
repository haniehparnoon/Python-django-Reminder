$(document).ready(function () {
    console.log(URL)
    $(".click_form").submit( function () {
        // e.preventDefault();
        $.ajax({
            type: 'POST',
            url : URL,
            dataType    : 'json',
            data:{
                category   :   $('#category_name').val(),
                description     :   $('#description').val(),
                
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