// JavaScript Document


$(document).ready(function() {
	
	console.log('script loaded successfully')
	
	
	$('.btn-random').on('click', function() {
	
		const $randomHero = Math.ceil(Math.random()*731);
		const $inputText = $('input:text');
		
		$.get(`https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/${$randomHero}.json`, function(data) {
			
			$("#name").text(data['name']);
			$("img").attr("src", data['images']["sm"]);
			
		$('.btn-guess').on('click', function() {
			
			console.log(data['biography']['publisher']);
			if ($inputText.val() == data['biography']['publisher']) {
				alert('You are correct!')
			} else {
				alert('Please try again!')
			}
		})	
			
				
		})
		
		
	})
	
})




