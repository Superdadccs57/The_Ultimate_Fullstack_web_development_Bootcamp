// JavaScript Document


$(document).ready(function() {
	
	console.log('script loaded successfully')
	
	
	$('.btn-random').on('click', function(e) {
	
		e.preventDefault()
		
		const $randomHero = Math.ceil(Math.random()*731);
		const $inputText = $('input:text');
		
		$.get(`https://superheroapi.com/api.php/10165589462060227/${$randomHero}/`, function(data) {
			
			$("#name").text(data['name']);
			$("img")
				.attr("src", data['image']['url'])
				.show();
			
		$('.btn-guess').on('click', function(e) {
			e.preventDefault()
			console.log(data['biography']['publisher']);
			if ($inputText.val() == data['biography']['publisher']) {
				alert('You are correct!')
			} else {
				alert('Please try again!')
			}
			
			location.reload();
		})	
			
				
		})
		
		
	})
	
})




