function search(){
    $("#search").click(function(){
        //get input text
        var val=$("input").val();
        console.log("search clicked");

        //if input is blank or all whitespaces
        if(val.length==0 || val.trim().length==0){
            console.log("blank");
            $("input").val("");
            $("input").focus();
        }
        else{
            console.log("form submit");
            window.location.href="/search_result/"+val;
            $("input").val("");
            $("input").focus();
        }

    });
}

$(document).ready(function(){
    search();
    $("input").keydown(function(event){
		var key=event.which;
		if(key==13){
			$("#search").click();
		}
	});
})