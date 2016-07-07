var App=angular.module('formApp', [ 'ui.router'])

App.config(function($stateProvider, $urlRouterProvider) {

    $stateProvider
    
    .state('form', {
        url: '/form',
        templateUrl: 'form.html',
        controller: 'formController'
    })
    .state('form1', {
        url: '/form1',
        templateUrl: 'form1.html',
        controller: 'formController'
    })
    .state('form2', {
        url: '/form2',
        templateUrl: 'form2.html',
        controller: 'formController'
    })

    $urlRouterProvider.otherwise('/form');
})

App.controller('formController', function($scope,$document) {
    $scope.formData = {};
    $scope.clearSearch=function(){
        $scope.searchAll=null;
    };

    $scope.formData='';
// forword calculation
$scope.totalInvoceAmount=function(val){
    console.log("on-change",$scope.formData);
    console.log($scope.formData.baseAmount + " baseAmount");
    console.log($scope.formData.service +" service");
    console.log($scope.formData.Tds +" Tds");

    console.log(parseInt($scope.formData.baseAmount)+parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount));
    return parseInt($scope.formData.baseAmount)+parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount);

};
$scope.totalAmtinBank=function(val){
    console.log("on-change",$scope.formData);
    console.log($scope.formData.baseAmount + " baseAmount");
    console.log($scope.formData.service +" service");
    console.log($scope.formData.Tds +" Tds");
    console.log(parseInt($scope.formData.baseAmount)+parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount)-parseInt($scope.formData.Tds)/100*parseInt($scope.formData.baseAmount));
    return parseInt($scope.formData.baseAmount)+parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount)-parseInt($scope.formData.Tds)/100*parseInt($scope.formData.baseAmount);

};



$scope.invoiceBaseAmt=function(val){
 //    console.log("on-change",$scope.formData);
 console.log($scope.formData.service +" service");
 console.log($scope.formData.Tds +" tds");
 console.log($scope.formData.totalInAmount +" totalInAmount");

 console.log(parseInt($scope.formData.totalInAmount)/(parseInt($scope.formData.service)/100+1) +"total service " );
 $scope.formData.baseAmount = parseInt($scope.formData.totalInAmount)/(parseInt($scope.formData.service)/100+1);
 console.log($scope.formData.baseAmount+ "---------- $scope.formData.baseAmount");
 return parseInt($scope.formData.totalInAmount)/(parseInt($scope.formData.service)/100+1);    
};


$scope.invoiceTotalAmtInBankAmt = function(){
 console.log("on-change",$scope.formData);
 console.log($scope.formData.Tds +" tds");
 console.log($scope.formData.service +" service");
 console.log($scope.formData.baseAmount+ "$scope.formData.baseAmount123");
 return parseInt($scope.formData.baseAmount)+parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount)-parseInt($scope.formData.Tds)/100*parseInt($scope.formData.baseAmount);

}

// $scope.amtInBankBaseAmt = function(){
//     console.log("on-change",$scope.formData);
//     console.log($scope.formData.Tds +" tds");
//     console.log($scope.formData.service +" service");
//     console.log($scope.formData.totalAmtInBank + "totalAmtInBank");
// // $scope.formData.baseAmount=(parseInt($scope.formData.totalAmtInBank)-parseInt($scope.formData.service)+parseInt($scope.formData.Tds));
//     console.log($scope.formData.baseAmount + "@@@@#$$$scope.formData.baseAmount");
//    console.log (parseInt($scope.formData.totalAmtInBank)-parseInt($scope.formData.service)+parseInt($scope.formData.Tds));
// return parseInt($scope.formData.totalAmtInBank)-parseInt($scope.formData.service)+parseInt($scope.formData.Tds);


// }





$scope.total = function () {
  console.log($scope.Opearation);
  if ($scope.Opearation=="add") {
   console.log(parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount));
   return  parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount);
}
}
$scope.totalAmt = function(){
    console.log($scope.open);
    if ($scope.open=="sub") {
       console.log( parseInt($scope.formData.Tds)/100*parseInt($scope.formData.baseAmount));
       return parseInt($scope.formData.Tds)/100*parseInt($scope.formData.baseAmount);
   }

}





// $scope.BaseAmtInAmountInBank1= function (){
//         console.log($scope.formData.totalAmtInBank1+"totalAmtInBank1");

//  console.log($scope.formData.service +" service");
//        console.log($scope.formData.Tds +" tds");
// $scope.formData.baseAmount=parseInt($scope.formData.totalAmtInBank1)-parseInt($scope.formData.service)+parseInt($scope.formData.Tds);
// console.log($scope.formData.baseAmount + "$scope.formData.baseAmount");
//          console.log (parseInt($scope.formData.totalAmtInBank1)-parseInt($scope.formData.service)+parseInt($scope.formData.Tds)+"drtfgyh");
//  return parseInt($scope.formData.totalAmtInBank1)-parseInt($scope.formData.service)+parseInt($scope.formData.Tds);

// }
// $scope.baseAmountInBankservice = function(){
//         console.log($scope.formData.totalAmtInBank1+"totalAmtInBank1");
//         console.log($scope.formData.service +" service");
//         console.log($scope.formData.Tds +" Tds");
// // $scope.formData.baseAmount= parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount);
// // // $scope.formData.baseAmount=00000;
//         // $scope.formData.baseAmount = (parseInt($scope.formData.service)/100*parseInt($scope.textBaseAmt)+"baseAmountInBankservice");

//      console.log(parseInt($scope.formData.service)/100*parseInt($scope.textBaseAmt)+"baseAmountInBankservice");
//      return  parseInt($scope.formData.service)/100*parseInt($scope.formData.baseAmount);
// }

});
