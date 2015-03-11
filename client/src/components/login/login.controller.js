'use strict';
/*jshint esnext: true */

// TODO - refactor into directive

class LoginCtrl {
  constructor($scope, $auth, $modal) {
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

    $scope.signupUser = function (event) {
      event.preventDefault();
      $modal.open(
        {
          templateUrl: "components/login/signup.modal.html"

        }
      )
    };
  }
}

LoginCtrl.$inject = ['$scope', '$auth', '$modal'];

export default LoginCtrl;
