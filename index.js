window.onload=function(){
    var i=1
    while (i<3) {
        $("#as:eq(i)").css("top","10px")
        $("#as:eq(i)").css("","10px")
        $("#as:eq(i)").animate({top:"-=10px",opacity:"0"},2500)
        i+1
    }
}