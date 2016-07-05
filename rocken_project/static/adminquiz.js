var quizApp = angular.module('adminQuizApp', [
// quizApp.config(['NotificationProvider', function(NotificationProvider){

//     NotificationProvider.setOptions({
//         delay: 2500,
//         startTop: 20,
//         startRight: 10,
//         verticalSpacing: 20,
//         horizontalSpacing: 20,
//         positionX: 'right',
//         positionY: 'top'
//     });

]);
quizApp.controller('QuizAdminCtrl', ['$scope', '$log', '$http', '$timeout', function($scope, $log, $http, $timeout){
    console.log('Quiz admin controller loads');
    $scope.tagList = []
    $scope.question = '';
    $scope.optionType = '';
    $scope.option = '';
    $scope.optionList = [];
    $scope.rightWrong = 'Wrong';
    $scope.isRightValue = false;
    $scope.questionList = null;
    $scope.validation = null;

    $scope.saveQuestion = function(){
        console.log({question:$scope.question, optionType:$scope.optionType, optionList: $scope.optionList});
        $http.post('/online/exam/save_question_options/', {question:$scope.question, optionType:$scope.optionType, optionList: $scope.optionList}).
        success(function(data, status, headers, config) {
            console.log(data);
            if (data.status){
                $scope.question = '';
                $scope.optionType = '';
                $scope.optionList = [];
                $scope.validation = data.validation;
                // Notification.success(data.validation);
            }else{
                // Notification.success(data.validation);
            }
        }).
        error(function(data, status, headers, config) {
            console.log(data);
        });
    }


    $scope.addOption = function(){
        if ($scope.option.length != 0){
            $scope.optionList.push({option: $scope.option, id:$scope.optionList.length+1, isRight: $scope.isRightValue})
            $scope.option = ''
            console.log($scope.optionList);
            $scope.rightWrong = 'Wrong';
            $(':checkbox').prop('checked', false);
            $scope.isRightValue = false;
        }
    }

    $scope.isRightWrong = function(){
        console.log($scope.rightWrong);
        if ($scope.rightWrong == 'Right'){
            $scope.rightWrong = 'Wrong';
            $(':checkbox').prop('checked', false);
            $scope.isRightValue = false;
        }else{
            $scope.rightWrong = 'Right';
            $(':checkbox').prop('checked', true);
            $scope.isRightValue = true;
        }
    }

    $scope.onClickNotification = function(){
        // Notification.success('Primary notification');
    }

}]);

