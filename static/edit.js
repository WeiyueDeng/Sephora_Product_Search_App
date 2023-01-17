function edit_data(id){
    $("#edit_submit").click(function(){
        /*empty all error divs */
        $("#edit_name_error").empty();
        $("#edit_brand_error").empty();
        $("#edit_image_error").empty();
        $("#edit_price_error").empty();
        $("#edit_size_error").empty();
        $("#edit_decription_error").empty();
        $("#edit_genre_error").empty();
        $("#edit_highlight_error").empty();
        $("#edit_instruction_error").empty();

        /*get inputs */
        var name_input=$("#edit_name").val();
        var brand_input=$("#edit_brand").val();
        var image_input=$("#edit_image").val();
        var price_input=$("#edit_price").val();
        var size_input=$("#edit_size").val();
        var description_input=$("#edit_description").val();
        var genre_input=$("#edit_genre").val();
        var hightlights_input=$("#edit_highlights").val();
        var instruction_input=$("#edit_instruction").val();

        /*check inputs*/
        if (name_input.length==0 || name_input.trim().length==0){
            $("#edit_name_error").html("This field cannot be empty.");
        }
        if (brand_input.length==0 || brand_input.trim().length==0){
            $("#edit_brand_error").html("This field cannot be empty.");
        }
        if (image_input.length==0 || image_input.trim().length==0){
            $("#edit_image_error").html("This field cannot be empty.");
        }
        if (price_input.length==0 || price_input.trim().length==0){
            $("#edit_price_error").html("This field cannot be empty.");
        }
        if (size_input.length==0 || size_input.trim().length==0){
            $("#edit_size_error").html("This field cannot be empty.");
        }
        if(description_input.length==0 || description_input.trim().length==0){
            $("#edit_decription_error").html("This field cannot be empty.");
        }
        if(genre_input.length==0 || genre_input.trim().length==0){
            $("#edit_genre_error").html("This field cannot be empty.");
        }
        if(hightlights_input.length==0 || hightlights_input.trim().length==0){
            $("#edit_highlight_error").html("This field cannot be empty.");
        }
        if(instruction_input.length==0 || instruction_input.trim().length==0){
            $("#edit_instruction_error").html("This field cannot be empty.");
        }
        /* If all inputs are full */
        if(instruction_input.length!=0 && hightlights_input.length!=0 && genre_input.length!=0 && name_input.length!=0 && brand_input.length!=0 && image_input.length!=0 && price_input.length!=0 && size_input.length!=0 && description_input.length!=0){
            //inputs can only be a number.
            if (isNaN(price_input)){
                $("#edit_price_error").html("This field can only be a number.");
            }
            
            if (!isNaN(price_input)){
                new_data= {"id": id,
                "name": name_input,
                "brand": brand_input,
                "image": image_input,
                "price": price_input,
                "size":size_input,
                "description":description_input,
                "genre":genre_input,
                "highlights": hightlights_input,
                "instruction":instruction_input
                };
                console.log(new_data);
                $.ajax({
					type: "POST",
					url: ""+id+"",                
					dataType : "json",
					contentType: "application/json; charset=utf-8",
					data : JSON.stringify(new_data),
					success: function(result){
                        let new_id=result["id"]
                        window.location.href="/view/"+new_id+""
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

function discard_edit(id){
    $("#dialog_box").dialog({
        autoOpen: false,
        modal: true,
        buttons: {
            Yes: function(){
                $(this).dialog("close");
                window.location.href="/view/"+id+"";
            },
            No: function(){
                $(this).dialog("close");
            }
        }
    });
    $("#edit_discard_changes").click(function(){
        $( "#dialog_box" ).dialog( "open" );
    });
}

$(document).ready(function(){
    edit_data(id);
    discard_edit(id);
})
