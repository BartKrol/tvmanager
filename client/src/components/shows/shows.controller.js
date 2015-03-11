'use strict';
/*jshint esnext: true */

// TODO - refactor into directive
class ShowsCtrl {
  constructor ($scope, popularShows) {
    popularShows.popularShows.then(function(response) {
      $scope.shows = response.data;
    });
  }
}

ShowsCtrl.$inject = ['$scope', 'popularShows'];

export default ShowsCtrl;
