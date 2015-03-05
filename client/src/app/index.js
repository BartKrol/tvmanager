'use strict';
/*jshint esnext: true */

import MainCtrl from './main/main.controller';
import NavbarCtrl from '../components/navbar/navbar.controller';
import LoginCtrl from '../components/login/login.controller';
//import EpisodeFactory from '../components/series/series.factory'

var dependencies = [
  'ngAnimate',
  'ngCookies',
  'ngTouch',
  'ngSanitize',
  'restangular',
  'ui.router',
  'ui.bootstrap',
  'ng-token-auth'
];

angular.module('angTest', dependencies)
  .controller('MainCtrl', MainCtrl)
  .controller('NavbarCtrl', NavbarCtrl)
  .controller('LoginCtrl', LoginCtrl)
  //.factory('SeriesFactory', SeriesFactory)

  .config(function ($stateProvider, $urlRouterProvider, $authProvider) {
    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: 'app/main/main.html',
        controller: 'MainCtrl'
      });

    $authProvider.configure({
      emailSignInPath: '/auth/'
    });

    $urlRouterProvider.otherwise('/');
  })
;

