
angular.module('app')
	.controller('MainCtrl', 
	['$scope', '$http', '$timeout', 'Games',
	function($scope, $http, $timeout, Games){

		$scope.user_set = false;
		

		// counter for controlling which puzzle should be visible
  	$scope.active_puzzle = 0;

  	$scope.load_screen = false;

  	// load from Games service
	  $scope.game = Games.game
	  Games.retrieveGame()

		// store user's answers to puzzles
		$scope.response = {
			participant : {
				age: 0,
				gender: ''
			},
			answers : []
		}
	
		$scope.save_user = function(){
			$scope.user_set = true;
		}

		$scope.increment = function(){
			$scope.active_puzzle ++;
		}

		$scope.save_response = function (puzzle_id){
			var res = {
				puzzle_id : puzzle_id,
				answer_id : $scope.selected_answer
			}
			$scope.response.answers.push(res);
			$scope.increment();

			if ($scope.active_puzzle >= $scope.game.puzzles.length ){

				submitResponses();

			}else{

				$scope.load_screen = true;
				$timeout(function(){	
					$scope.load_screen = false;
				}, $scope.game.delay)

			}
			


		};

		submitResponses = function() {
			//POST results
			alert("thank you!");
		}


	}])
