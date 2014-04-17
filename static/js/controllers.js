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

    $scope.getDevelopers = function() {
      $http({method: 'GET', url: '/api/v1/developer/'}).
        success(function(data, status, headers, config) {
          // this callback will be called asynchronously
          // when the response is available
          $scope.developers = data.objects;
        }).
        error(function(data, status) {
          $scope.developers = data || status;
        });
    }

    $scope.getPlatforms = function() {
      $http({method: 'GET', url: '/api/v1/platform/'}).
        success(function(data, status, headers, config) {
          // this callback will be called asynchronously
          // when the response is available
          $scope.platforms = data.objects;
        }).
        error(function(data, status) {
          $scope.platforms = data || status;
        });
    }

    $scope.getGenres = function(){
      var genres = [];
      if ($scope.games){
        for (var i = $scope.games.length - 1; i >= 0; i--) {
          genres.push($scope.games[i].genre);
        };
      }
 
      // remove duplicates
      genres = genres.filter(function(elem, pos) {
        return genres.indexOf(elem) == pos;
      })
 
      return genres;
    }

    $scope.getManufacturers = function(){
      var manufacturers = [];
      if ($scope.platforms){
        for (var i = $scope.platforms.length - 1; i >= 0; i--) {
          manufacturers.push($scope.platforms[i].manufacturer);
        };
      }
 
      // remove duplicates
      manufacturers = manufacturers.filter(function(elem, pos) {
        return manufacturers.indexOf(elem) == pos;
      })
 
      return manufacturers;
    }
    $scope.exactCompare = function (actual, input) {
      if (input === "") {
         return true;
      }
      return angular.equals(input, actual);
    }

    $scope.getGames();
    $scope.getDevelopers();
    $scope.getPlatforms();

    $scope.gameOrderProp = "title";
    $scope.platformOrderProp = "name";
    $scope.developerOrderProp = "name";
 }])
