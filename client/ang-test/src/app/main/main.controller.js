'use strict';
/*jshint esnext: true */

class MainCtrl {
  constructor ($scope) {
    $scope.tvseries = [
      {
        'name': 'Gotham',
        'previous': {
          's': '1',
          'e': '2',
          'episode': 'Batman Rises',
          'airdate': '12.11.2014'
        },
        'next': {
          's': '1',
          'e': '2',
          'episode': 'Batman Rises',
          'airdate': '12.11.2014'
        }
      },
      {
        'name': 'Flash',
        'previous': {
          's': '2',
          'e': '2',
          'episode': 'Fastest Man Alive',
          'airdate': '12.11.2014'
        },
        'next': {
          's': '2',
          'e': '2',
          'episode': 'Fastest Man Alive',
          'airdate': '12.11.2014'
        }
      },
      {
        'name': 'Vikings',
        'previous': {
          's': '3',
          'e': '4',
          'episode': 'Valhalla',
          'airdate': '12.11.2014'
        },
        'next': {
          's': '3',
          'e': '4',
          'episode': 'Valhalla',
          'airdate': '12.11.2014'
        }
      }
    ];
  }
}

MainCtrl.$inject = ['$scope'];

export default MainCtrl;
