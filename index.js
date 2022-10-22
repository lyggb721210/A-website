window.onload=function(){
    var i=1
    while (i<2) {
        $("#as:eq("+i+")").animate({top:"-=10px",opacity:"-=1"},2500)
        i+1
    }
}