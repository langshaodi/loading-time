
angular.module('app')
	.controller('MainCtrl', 
	['$scope', '$http', '$timeout', 'Games',
	function($scope, $http, $timeout, Games){

		//state variables
		$scope.user_set = false;
		$scope.feedback_set = false;
		$scope.load_screen = false;
		$scope.intermission = false;
		$scope.done = false;
		// currently visible game and puzzle
		$scope.active_game = 0;		
  		$scope.active_puzzle = 0;
		// timestamp variable for tracking response times
		var timer;

		// store user's answers to puzzles
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
			answers : [
			// puzzle id, answer id, game id, response time in ms
			]
		}
	

		$scope.save_user = function(){
			if ($scope.number_of_games){
				
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
			}else{return}
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
			$scope.response.answers.push(res);
			$scope.active_puzzle ++;
			if ($scope.active_puzzle >= $scope.games[$scope.active_game].puzzles.length ){
				console.log('here')
				console.log($scope.active_game);
				console.log($scope.number_of_games);
				if ($scope.active_game + 1 < $scope.number_of_games ){
					$scope.intermission = true;
				}else {
					submitResponses();
				}
			}else{
				$scope.load_screen = true;
				$timeout(function(){	
					$scope.load_screen = false;
					timer = new Date();
				}, $scope.games[$scope.active_game].delay )//* 1000)

			}
		};

		$scope.continue = function(){
			$scope.intermission = false;
			$scope.active_game ++;
			$scope.active_puzzle = 0;
		}

		submitResponses = function() {
			$scope.done = true;
			console.log($scope.response);
		}


	}])
