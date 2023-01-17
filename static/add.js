function display(data){
    $("#add_data_result").empty();
    if (data.length!=0){
        $.each(data, function(index,value){
            var id=value
            $("#add_data_result").html("New item successfully created. <a href='/view/"+id+"'>See it here</a>");
        })
    }
    
}

function add_data(){
    $("#submit").click(function(){
        /*empty all error divs */
        $("#id_error").empty();
        $("#name_error").empty();
        $("#brand_error").empty();
        $("#image_error").empty();
        $("#price_error").empty();
        $("#size_error").empty();
        $("#decription_error").empty();
        $("#genre_error").empty();
        $("#highlight_error").empty();
        $("#instruction_error").empty();

        /*get inputs */
        var id_input=$("#add_id").val();
        var name_input=$("#add_name").val();
        var brand_input=$("#add_brand").val();
        var image_input=$("#add_image").val();
        var price_input=$("#add_price").val();
        var size_input=$("#add_size").val();
        var descriptionn_input=$("#add_description").val();
        var genre_input=$("#add_genre").val();
        var hightlights_input=$("#add_highlights").val();
        var instruction_input=$("#add_instruction").val();

        /*check inputs*/
        if (id_input.length==0 || id_input.trim().length==0){
            $("#id_error").html("This field cannot be empty.");
        }
        if (name_input.length==0 || name_input.trim().length==0){
            $("#name_error").html("This field cannot be empty.");
        }
        if (brand_input.length==0 || brand_input.trim().length==0){
            $("#brand_error").html("This field cannot be empty.");
        }
        if (image_input.length==0 || image_input.trim().length==0){
            $("#image_error").html("This field cannot be empty.");
        }
        if (price_input.length==0 || price_input.trim().length==0){
            $("#price_error").html("This field cannot be empty.");
        }
        if (size_input.length==0 || size_input.trim().length==0){
            $("#size_error").html("This field cannot be empty.");
        }
        if(descriptionn_input.length==0 || descriptionn_input.trim().length==0){
            $("#decription_error").html("This field cannot be empty.");
        }
        if(genre_input.length==0 || genre_input.trim().length==0){
            $("#genre_error").html("This field cannot be empty.");
        }
        if(hightlights_input.length==0 || hightlights_input.trim().length==0){
            $("#highlight_error").html("This field cannot be empty.");
        }
        if(instruction_input.length==0 || instruction_input.trim().length==0){
            $("#instruction_error").html("This field cannot be empty.");
        }
        /* If all inputs are full */
        if(instruction_input.length!=0 && hightlights_input.length!=0 && genre_input.length!=0 && id_input.length!=0 && name_input.length!=0 && brand_input.length!=0 && image_input.length!=0 && price_input.length!=0 && size_input.length!=0 && descriptionn_input.length!=0){
            //inputs can only be a number.
            if (isNaN(id_input)){
                $("#id_error").html("This field can only be a number.");
            }
            if (isNaN(price_input)){
                $("#price_error").html("This field can only be a number.");
            }
            
            if (!isNaN(id_input) && !isNaN(price_input)){
                new_data= {"id": id_input,
                "name": name_input,
                "brand": brand_input,
                "image": image_input,
                "price": price_input,
                "size":size_input,
                "description":descriptionn_input,
                "genre":genre_input,
                "highlights": hightlights_input,
                "instruction":instruction_input
                };
                $.ajax({
					type: "POST",
					url: "add",                
					dataType : "json",
					contentType: "application/json; charset=utf-8",
					data : JSON.stringify(new_data),
					success: function(result){
						let new_item = result["new_item"]
						display(new_item)
						//clear input
						$("#id_input").val("")
                        $("#id_input").focus()
						$("#name_input").val("")
                        $("#brand_error").val("")
                        $("#image_error").val("")
                        $("#price_error").val("")
                        $("#size_error").val("")
                        $("#decription_error").val("")
                        $("#genre_error").val("")
                        $("#highlight_error").val("")
                        $("#instruction_error").val("")
						
					},
					error: function(request, status, error){
						console.log("Error");
						console.log(request)
						console.log(status)
						console.log(error)
					}
				});
            }

        }

    })
}

$(document).ready(function(){
    display(data);
    add_data();
})