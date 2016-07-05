var quizApp = angular.module('quizApp', [
    ]);
quizApp.controller('QuizCtrl', ['$scope', '$log', '$http', '$timeout' , function($scope, $log, $http, $timeout){
    $log.info('quiz controller loads');
    $scope.indexToShow = 0;
    $scope.isRight = null;
    $scope.quizEnd = null;
    $scope.totalMarks = 0;
    $scope.submittedQuestion = [];

    $scope.init =  function() {
        $scope.getQuestionAndAnswer();
    };

    $timeout($scope.init,1000);

    $scope.getQuestionAndAnswer = function(){
    $http.get('/online/exam/get_question_and_answer/').
    success(function(data, status, headers, config) {
        console.log(data);
        if (data.status){
            $scope.questionList = data.questionList
        }else{
            Notification.success(data.validation);
        }
    }).
    error(function(data, status, headers, config) {
        console.log(data);
    });
    }

    $scope.changeToNext = function(){
        $scope.alreadySubmit = null;
        $scope.isRight = null;
        if ($scope.indexToShow+1 >= $scope.questionList.length){
            $('#confirmation_modal').modal('show');
        }else{
            $scope.indexToShow = ($scope.indexToShow + 1) % $scope.questionList.length;
            $log.info($scope.indexToShow+1 +"  "+ $scope.questionList.length)
        }
        // $('#confirmation_modal').modal('hide');
    };
    $scope.showResult = function(){
        $scope.quizEnd = "Quiz ended !!";
         $('#confirmation_modal').modal('hide');
    }
    $scope.closeModal = function(){
        $('#confirmation_modal').modal('hide');
    }

    $scope.changeToPrevious = function(){
        $scope.alreadySubmit = null;
        if ($scope.indexToShow == $scope.questionList.length-1){
            $scope.quizEnd = null;
        }
        // $log.info($scope.indexToShow +"  "+ $scope.questionList.length)
        $scope.isRight = null;
        $scope.indexToShow = ($scope.indexToShow - 1) % $scope.questionList.length;
        // if ($scope.indexToShow <= 0){
        //     $scope.indexToShow = 1
        // }
    };

    var checkAvailable = function(list,item){
        if(list.length > 0){
            for(var i=0; i<list.length; i++){
                if (list[i].id == item.id){
                    console.log(list[i].id)
                    console.log(item.id)
                    // $scope.alreadySubmit = "Already submit...";
                    console.log("Already submit...");
                    return true;
                }else{
                    // list.push(item);
                    // $scope.alreadySubmit = false;
                    console.log("submit...");
                    return false;
                }
            }
        }else{
            console.log("length issue...");
            return false;
        }
    }

    $scope.checkAnswer = function(option, que){
        console.log(que);
        console.log(que);
        que.submittedAnswer = angular.copy(option);
        if (checkAvailable($scope.submittedQuestion, que)){
                $scope.alreadySubmit = "Already submit..."
                console.log("Already submit...");
        }else{
                console.log("submit...");
                $scope.alreadySubmit = "submit..."
                $scope.submittedQuestion.push(que);
        }

        // console.log(que);
        // console.log($scope.submittedQuestion);
        // console.log(option);
        $scope.isRight = option.isRight;
        if ($scope.isRight){
            $scope.totalMarks += 1;
        }
    }

    var marks=$('.text-center').text();
    console.log(marks);

}]);
