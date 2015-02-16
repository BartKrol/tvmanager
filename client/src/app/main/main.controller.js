'use strict';
/*jshint esnext: true */

class MainCtrl {
  constructor ($scope, Restangular) {
    Restangular.all('episodes').then(function(episodes){
      $scope.episodes = episodes;
    });
  }
}

MainCtrl.$inject = ['$scope', 'restangular'];

export default MainCtrl;
