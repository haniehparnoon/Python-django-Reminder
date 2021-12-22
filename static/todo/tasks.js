$(document).ready(function () {
    $('#expired_tasks').on("click",function(){
        send_ajax_expired_tasks($(this).text())
       
      })
      function send_ajax_expired_tasks(input_data){
        data={'csrfmiddlewaretoken':CSRF_TOKEN, "text":input_data};

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            success: function(res) {
                console.log(res);
                show_expired_tasks(res)
            }
        });
    }
    

    function show_expired_tasks(data){
        my_ul_tag = $('#mu_ul')
        my_ul_tag.empty()
        if ( data['tasks'] ){
            console.log(data['tasks'])
            for (const [key, value] of Object.entries(data['tasks'])) {
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



    $('#unexpired_tasks').on("click",function(){
        send_ajax_expired_tasks($(this).text())
           
        })

    $('#last_tasks').on("click",function(){
        send_ajax_expired_tasks($(this).text())
       
      })






})