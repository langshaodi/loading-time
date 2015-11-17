angular.module('app')
.factory('Games', [
	'$http', '$q',
	function($http, $q){
		var o = {
	    games: []
	  };

	  // retrieve 3 games
  	o.retrieveGames = function() {
  		$q.all([
  			$http.get('/api/game/'),
  			$http.get('/api/game/'),
  			$http.get('/api/game/')
  		]).then(function(results){
  			 var data = [results[0].data,results[1].data,results[2].data]
		     angular.copy(data, o.games);
  		});
  	};
	  return o;
	}
	]);


// API FORMAT:
/* 
{
"id":5,
"puzzles":[
	{
	"id":1,
	"question":"Abba is to BAAB as XYYX is to ______. (YXXY)",
	"answers":[
		{"id":1,"correct":true,"text":"YXXY","puzzle":1},
		{"id":2,"correct":false,"text":"X","puzzle":1},
		{"id":3,"correct":false,"text":"ABCD","puzzle":1},
		{"id":4,"correct":false,"text":"BBBB","puzzle":1}
	]
	}
],
"delay":22
}

*/

