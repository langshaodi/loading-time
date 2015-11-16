angular.module('app')
.factory('Games', [
	'$http',
	function($http){

		var o = {
	    game: {}
	  };

  	o.retrieveGame = function() {
	    return $http.get('/api/game/').success(function(data){
	      angular.copy(data, o.game);
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

