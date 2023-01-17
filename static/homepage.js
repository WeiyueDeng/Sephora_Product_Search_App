function displayItems(data){
    $("#items").empty();

    $.each(data, function(index,value){
        var id=value["id"];
        var item=$("<div class='col-4' data-id='"+id+"'>");
        var name=value["name"];
        var brand=value["brand"];
        var image=value["image"];
        $(item).html("<a href='/view/"+id+"' class='link'><div class='image_div'><img src='"+image+"' class='image' alt='"+name+" in "+brand+"'></div><div class='brand'>"+brand+"</div><div class='name'>"+name+"</div></a>");
        $("#items").append(item);
    });      
}


$(document).ready(function(){
    displayItems(data);
})