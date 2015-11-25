angular.module('app')
.factory('Games', [
	'$http', '$q',
	function($http, $q){
		var o = {
	    games: []
	  };

	  // retrieve 3 games
  	o.retrieveGames = function(num, cb) {
        var games = [];
        games.push($http.get('/api/game/default/'));
        for (var i = 1; i < num; i ++) {
            games.push($http.get('/api/game/'));
        }
        console.log(games);
  		$q.all(games).then(function(results){
  			 var data = [];
             for (j = 0; j < games.length ; j++){
                data[j] = results[j].data;
             }
		     angular.copy(data, o.games);
             cb();
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

