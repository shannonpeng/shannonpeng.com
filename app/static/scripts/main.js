$(document).ready(function () {
	console.log("👀");

	// hide flash messages
	setTimeout(function(){ $(".flashes").addClass("hidden")}, 2500);

	// color the nav border
	$(".nav").addClass(["one", "two", "three"][$(".selected").parent().index()]);

	// filter projects
	$(".category-filter .category").on("click", function(event) {

		var selected = $(event.target).hasClass("active");

		if (!selected) {
			var category = $(event.target).attr("category");
			$(".category-filter .category").removeClass("active");
			$(event.target).addClass("active");
			$(".project").fadeOut(300);
			if (category == 'all') {
				setTimeout(function(){
					$(".project").fadeIn(300).css("display","inline-block");;
				},300);
			}
			else {
				setTimeout(function(){
					$(".category-" + category).fadeIn(300).css("display","inline-block");;
				},300);
			}
		}
	});
});