$(document).ready(function () {
	console.log("👀");

	// hide flash messages
	setTimeout(function(){ $(".flashes").addClass("hidden")}, 2500);

	// color the nav border
	$(".nav").addClass(["one", "two", "three"][$(".selected").parent().index()]);

	// Sorry I made you load all of jQuery just for those two things :') Maybe I'll add more later.

});