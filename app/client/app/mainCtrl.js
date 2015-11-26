
angular.module('app')
	.controller('MainCtrl', 
	['$scope', '$http', '$timeout', 'Games',
	function($scope, $http, $timeout, Games){

		//state variables
		$scope.user_set = false;
		$scope.feedback_set = false;
		$scope.load_screen = false;
		$scope.intermission = false;
		$scope.frustration = false;
		$scope.done = false;
		// currently visible game and puzzle
		$scope.active_game = 0;		
  		$scope.active_puzzle = 0;
		// timestamp variable for tracking response times
		var timer;
	

		$scope.save_user = function(){
			if ($scope.number_of_games && ($scope.age >= 18)){
						// store user's answers to puzzles
				var games = [];
				for (var i = 0; i < $scope.number_of_games; i ++) {
					games.push({frustration:null, responses:[]});
				}
				$scope.response = {
					participant : {
						//age
						//gender
					},
					feedback : {
						//frustration
						//difficulty
						//additional comments
					},
					games : games
				}
				//start game after 3 seconds
				// TODO countdown display
				$scope.load_screen = true;
		  		// load 3 games from Games service
				$scope.games = Games.games
				Games.retrieveGames($scope.number_of_games, function() {
					$scope.load_screen = false;
					$scope.user_set = true;	
					timer = new Date();				
				});
			} else {
				if ($scope.age < 18) {
					alert("You must be 18 years or older to complete this study.")
				}
				return
			}
		}

		// show next puzzle, pause for intermission between games, or complete submission
		$scope.save_response = function (game_id, puzzle_id){

			var time =  new Date().getTime() - timer.getTime()
			var res = {
				game_id : game_id,
				puzzle_id : puzzle_id,
				answer_id : $scope.selected_answer,
				response_time_in_ms : time
			}
			$scope.response.games[$scope.active_game].responses.push(res);
			$scope.active_puzzle ++;
			if ($scope.active_puzzle >= $scope.games[$scope.active_game].puzzles.length ){
				$scope.frustration = true;
			}else{
				$scope.load_screen = true;
				$timeout(function(){	
					$scope.load_screen = false;
					timer = new Date();
				}, $scope.games[$scope.active_game].delay * 1000)

			}
		};

		$scope.save_frustration = function () {
			if ($scope.frustrationValue != null) {
				$scope.response.games[$scope.active_game].frustration = parseInt($scope.frustrationValue);
				$scope.frustrationValue = null;
				$scope.frustration = false;
				if ($scope.active_game + 1 < $scope.number_of_games ){
					$scope.intermission = true;
				}else {
					submitResponses();
				}		
			} else {
				alert('Please indicate your level of frustration before continuing.')
			}
		}

		$scope.continue = function(){
			$scope.intermission = false;
			$scope.active_game ++;
			$scope.active_puzzle = 0;
		}

		$scope.terminate = function() {
			submitResponses();
			$scope.intermission = false;
		}

		submitResponses = function() {
			$scope.done = true;
			$http.post('/api/response/', $scope.response).then(
				function(resp){
					$scope.end_message = "Thank you! Your responses have been recorded."
				},
				function(resp){
					$scope.end_message = JSON.stringify(response) + "\n" + JSON.stringify($scope.response);
				}
			);
			console.log($scope.response);
		}
	}]);
