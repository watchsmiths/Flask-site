// JavaScript Document
(function($)
{
	"use strict"

	/* Event - Window Scroll */
	$(window).scroll(function()
	{
		var scroll	=	$(window).scrollTop();
		var height	=	$(window).height();

		/*** set sticky menu ***/
		if( scroll >= 92 )
		{
			$('.menu-block').addClass("navbar-fixed-top");
            $('#header').next('div').css({"margin-top": "81px"});
		}
		else
		{
			$('.menu-block').removeClass("navbar-fixed-top");
            $('#header').next('div').css({"margin-top": "0px"});
		} // set sticky menu - end

		if ($(this).scrollTop() >= 300)
		{
			// If page is scrolled more than px
			$('#back-to-top').css({"display": "block"}).fadeIn(200);    // Fade in the arrow
		}
		else
		{
			$('#back-to-top').css({"display": "none"}).fadeOut(200);   // Else fade out the arrow
		}
	});
	/* Event - Window Scroll /- */

	$('#back-to-top').click(function()
	{
		// When arrow is clicked
		$('body,html').animate(
		{
			scrollTop : 0 // Scroll to top of body
		},800);
	});		
	
	$('.dial').each(function ()
	{
		var $this = $(this);
		var myVal = $(this).data("value");		

		$this.appear(function()
		{
			// alert(myVal);
			$this.knob({ });
			$({ value: 0 }).animate({ value: myVal },
			{
				duration: 2000,
				easing: 'swing',
				step: function ()
				{
					$this.val(Math.ceil(this.value)).trigger('change');
				}
			});
		});
	});
	
	
	/* Event - Document Ready /- */	
	$(document).ready(function($)
	{
		var scroll	=	$(window).scrollTop();
		var height	=	$(window).height();

		/*** set sticky menu ***/
		if( scroll >= height -500 )
		{
			$('.menu-block').addClass("navbar-fixed-top");
            $('#header').next('div').css({"margin-top": "81px"});
		}
		else
		{
			$('.menu-block').removeClass("navbar-fixed-top");
            $('#header').next('div').css({"margin-top": "0px"});
		} // set sticky menu - end
		
		
		// Newsletter popup
		// Get the modal
		var modal = $("#myModal");

		// Get the button that opens the modal
		var btn = $("#myBtn");

		// Get the <span> element that closes the modal
		var span = $(".close");

		// When the user clicks the button, open the modal 
		btn.click(function() {
			modal.show();
		})

		// When the user clicks on <span> (x), close the modal
		span.click(function(){modal.hide()})

		// When the user clicks anywhere outside of the modal, close it
		$(document).click(function(event) {if (event.target == modal) {modal.hide();}})




	});	
	/* document.ready /- */	
	
	
	
})(jQuery);