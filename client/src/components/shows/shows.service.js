'use strict';
/*jshint esnext: true */

function popularShows($http) {
  var popularShows = $http.get('/api/v1/popular').
    success(function(data, status, headers, config) {
      return data;
    }).
    error(function(data, status, headers, config) {
    });

  return {
    popularShows: popularShows
  };
}

popularShows.$inject = ['$http'];

export default popularShows;
