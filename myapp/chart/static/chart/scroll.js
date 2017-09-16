$(document).ready(function(){
var navpos = $("#navbar").offset().top;
	$(window).scroll(function(){
		
		var windpos = $(window).scrollTop();
		if (windpos>navpos){
			$("#navbar").addClass("navbar-fixed-top");
		}else{
			$("#navbar").removeClass("navbar-fixed-top");
		}
	})
	
	$(".channel").hide();
	$(".butt").click(function(){
	$(".channel").show();
	})
	
	$(".cancel").click(function(){
	$(".channel").hide();
	})
});