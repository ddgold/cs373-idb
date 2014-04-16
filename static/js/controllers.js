'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
  .controller('MyCtrl1', ['$scope', '$http', function($scope, $http) {
    $scope.games = [];
    $scope.getGames = function() {
    $http({method: 'GET', url: '/api/v1/game/'}).
      success(function(data, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        $scope.games = data.objects;
      }).
      error(function(data, status) {
        alert("hi");
        $scope.games = data || status;
      });
    }

   $scope.getGames();
   $scope.getGenres = function(){
     var genres = [];
     for (var i = $scope.games.length - 1; i >= 0; i--) {
       genres.push($scope.games[i].genre);
     };

     // remove duplicates
     genres = genres.filter(function(elem, pos) {
       return genres.indexOf(elem) == pos;
     })

     return genres;
   }
   $scope.genre = "";
   $scope.orderProp = "title";
 }])
