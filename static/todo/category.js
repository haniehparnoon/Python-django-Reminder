$(document).ready(function () {

    $('#empty_categories').on("click",function(){
        send_ajax_category($(this).text())
       
      })
    
      function send_ajax_category(input_data){
        data={'csrfmiddlewaretoken':CSRF_TOKEN, "text":input_data};

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            success: function(res) {
                console.log(res);
                show_category(res)
            }
       
        });
    }
    
    function show_category(data){
        my_ul_tag = $('#mu_ul')
        my_ul_tag.empty()
        if ( data['category'] ){
            console.log(data['category'])
            for (const [key, value] of Object.entries(data['category'])) {
                console.log("*", key, value);
                var li = document.createElement("li");  
                var span1 = document.createElement("span");   
                span1.append(value)
                li.append(span1)
                my_ul_tag.append(li)
              }
            
        }else{
            my_ul_tag.append()
        }
        
    }

    $('#popular_categories').on("click",function(){
        send_ajax_category($(this).text())
       
      })
    
})