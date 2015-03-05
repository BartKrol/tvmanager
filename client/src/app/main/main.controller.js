'use strict';
/*jshint esnext: true */

// TODO - refactor into directive

class MainCtrl {
  constructor ($scope) {
    $scope.elements = [
      {
        text: 'AAA'
      },
      {
        text: 'BBB'
      },
      {
        text: 'CCC'
      },
      {
        text: 'DDD'
      }
    ];

    _.forEach($scope.elements, function(element) {
     element.is_active = '';
    });

    _.first($scope.elements).is_active = 'active';


    $scope.makeActive = function(element){
      _.forEach($scope.elements, function(el){
        el.is_active = '';
      });
      element.is_active = 'active';
    }
  }
}

MainCtrl.$inject = ['$scope', '$http'];

export default MainCtrl;
