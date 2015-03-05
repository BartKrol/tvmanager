'use strict';
/*jshint esnext: true */

// TODO - refactor into directive
class ShowsCtrl {
  constructor ($scope) {
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

ShowsCtrl.$inject = ['$scope', '$http'];

export default ShowsCtrl;
