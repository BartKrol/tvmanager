'use strict';
/*jshint esnext: true */

import MainCtrl from './main/main.controller';
import LoginCtrl from '../components/login/login.controller';
import ShowsService from '../components/shows/shows.service'
import ShowsCtrl from '../components/shows/shows.controller.js';

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

angular.module('TvManager', dependencies)
  .controller('MainCtrl', MainCtrl)
  .controller('LoginCtrl', LoginCtrl)
  .controller('ShowsService', ShowsService)
  .controller('ShowsCtrl', ShowsCtrl)

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

