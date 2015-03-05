'use strict';
/*jshint esnext: true */

// TODO - refactor into directive

class LoginCtrl {
  constructor($scope, $auth) {
    $scope.logged = false;

    $scope.loginUser = function () {
      $auth.submitLogin({
        username: $scope.email,
        password: $scope.password
      })
        .then(function () {
          $scope.logged = true;
        })
        .catch(function () {
          alert('Wrong credentials');
        });
    };

    $scope.logoutUser = function () {
      $scope.logged = false;
    };
  }
}

LoginCtrl.$inject = ['$scope', '$auth'];

export default LoginCtrl;
