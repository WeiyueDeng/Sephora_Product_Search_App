function displayItems(data,val){
    $("#search_result").empty();
    var num=data.length;
    $("#search_content").html(""+val+"");
    $("#search_result_num").html(""+num+"");

    if(num==0){
        $("#search_result").html("No result found");
    }
    else{
        console.log(val);
        var custfilter= new RegExp(val,"gi");
        var repstr="<span class='highlight'>"+val+"</span>";
        $.each(data, function(index,value){
            var id=value["id"];
            var item=$("<div class='col-4' data-id='"+id+"'>");
            var name=value["name"];
            var brand=value["brand"];
            var image=value["image"];
            var price=value["price"];
            var genre_items=value["genre"];
            var genre_tag=""
            $.each(genre_items,function(index,value){
                if (index==genre_items.length-1){
                    genre_tag = genre_tag+value;
                }
                else{
                    genre_tag = genre_tag+value+">";
                }
                
            });
            var link=$("<a href='/view/"+id+"' class='link'>");

            var image_div=$("<div class='image_div'>");
            $(image_div).html("<img src='"+image+"' class='image' alt='"+name+" in "+brand+"'>");
            //console.log($(image_div).html());

            var content=$("<div class='search_product_info'>");
            name_highlight=name.replace(custfilter,repstr);
            brand_highlight=brand.replace(custfilter,repstr);
            genre_tag_highlight=genre_tag.replace(custfilter,repstr);
            text="<div class='search_brand' data-tag='"+brand+"'>"+brand_highlight+"</div><div class='search_name' data-tag='"+name+"'>"+name_highlight+"</div><div class='search_genre_tag' data-tag='genre'>"+genre_tag_highlight+"</div><div class='search_price' data-tag='"+price+"'>"+price+"</div>";
            $(content).html(text);
            console.log( $(content).text());

            $(link).append(image_div);
            $(link).append(content);
            $(item).append(link);

            //$(item).html("<a href='/view/"+id+"' class='link'><div class='image_div'><img src='"+image+"' class='image'></div><div class='search_product_info'><div class='search_brand' data-tag='"+brand+"'>"+brand+"</div><div class='search_name' data-tag='"+name+"'>"+name+"</div><div class='search_genre_tag' data-tag='genre'>"+genre_tag+"</div><div class='search_price' data-tag='"+price+"'>"+price+"</div></div></a>");
    
            //$(".search_brand").each(function(){
              //  $(this).html($(this).html().replace(custfilter,repstr));
            //})
       
            $("#search_result").append(item);
        }); 
        
        
        
    }
}


$(document).ready(function(){
    displayItems(data,val);

})