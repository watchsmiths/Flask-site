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

		// Scroll into newsletter when mailing is clicked, form glow after scroll
		$('#mailing').click(function() {
			$("#newsletter-discount")[0].scrollIntoView({
				behavior: "smooth"
			});

			$(".newsletter_form").css({
				'transition': 'box-shadow 1s ease-in-out 1.5s',
				'box-shadow': '0px 40px 80px 20px #beb2a6'
			});

		});

		$('#newsletter-reveal')[0].click(function() {
			$('.newsletter-div').toggle();
		    $('.newsletter-div').css({
                'transition': 'all 2s ease-out',
                'opacity': 1,
				'content-visibility': 'visible'
			})
		});


	});	
	/* document.ready /- */	
	
	
	
})(jQuery);