document.addEventListener('DOMContentLoaded', function (event) {

	document.getElementById('save_button').disabled = true;



});

var imdbidMovie;
var titleMovie;
var releaseMovie;
var runtimeMovie;
var actorsMovie;
var boxofficeMovie;


function requestAPI() {
	let api_key = 'fe80b8c5';
	var text_elem = document.getElementById('TextBox').value;

	var url = 'http://www.omdbapi.com/?t=' + text_elem + '&apikey=' + api_key;
	fetch(url)
		.then(function (response) {
			if (response.ok) {
				response.clone().json().then(function (data) {



					var movie_title = document.getElementById('Title');
					var movie_release = document.getElementById('Release');
					var movie_runtime = document.getElementById('Runtime');
					var movie_actors = document.getElementById('Actors');
					var movie_boxoffice = document.getElementById('BoxOffice');

					imdbidMovie = data.imdbID;
					titleMovie = data.Title;
					releaseMovie = data.Released;
					runtimeMovie = data.Runtime;
					actorsMovie = data.Actors;
					boxofficeMovie = data.BoxOffice;

					movie_title.innerHTML = 'Title: ' + titleMovie;
					movie_release.innerHTML = 'Release: ' + releaseMovie;
					movie_runtime.innerHTML = 'Runtime: ' +  runtimeMovie;
					movie_actors.innerHTML = 'Actors: ' + actorsMovie;
					movie_boxoffice.innerHTML = 'Box office: ' + boxofficeMovie;

					if (data.Title) {
						document.getElementById('save_button').disabled = false;
					}
					else {
						document.getElementById('save_button').disabled = true;
					}
				});
			}
			else {
				console.log('response failed');
			}
		});
}


function saveToDb() {

	let sendId = {imdbId: imdbidMovie,
				  titleMovie: titleMovie,
				  releaseMovie: releaseMovie,
				  runtimeMovie: runtimeMovie,
				  actorsMovie: actorsMovie,
				  boxofficeMovie: boxofficeMovie};
	sendId = JSON.stringify(sendId);
	let csrfToken = Cookies.get('csrftoken');

	let header = {
		'method': 'POST',
		'body': sendId,
		'headers': {
			'X-CSRFToken': csrfToken,
			'Accept': 'application/json',
			'Content-Type': 'application/json'
		}
	};

	fetch('/save_movie/', header).then(function (response) {
		// console.log(response);
	});
}

function enter(e) {
    if (e.keyCode == 13) {
		requestAPI();
    }
}