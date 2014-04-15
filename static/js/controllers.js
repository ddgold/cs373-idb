'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
  .controller('MyCtrl1', ['$scope', '$http', function($scope, $http) {
    $scope.getGames = function() {
    $http({method: 'GET', url: '/api/v1/game/'}).
      success(function(data, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        $scope.games = data.objects;
      }).
      error(function(data, status) {
        $scope.games = data || status;
      });
    }
 $scope.getGames();
 }])
