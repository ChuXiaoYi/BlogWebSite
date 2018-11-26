
var app = angular.module('myApp',['ngSanitize']);
app.controller('myCtrl', function($scope,$http) {
    $scope.load = function () {
        $http({
            url:'http://127.0.0.1:8000/post/post_list/',
            method: 'GET',
            params :{

            },
            timeout:10000
        }).success(function(data){
            $scope.jsondata = data;
            //for(i=0;i<data.length;i++){
            //    var converter = new showdown.Converter();
            //    $scope.jsondata[i].body = converter.makeHtml(data[i].body);
            //}
            console.dir(data)
        }).error(function(data){

        });

        $http({
            url:'http://127.0.0.1:8000/post/cate_list/',
            method: 'GET',
            params :{

            },
            timeout:10000
        }).success(function(data){
            $scope.cate_list = data
            console.dir(data)
        }).error(function(data){

        });

        $http({
            url:'http://127.0.0.1:8000/post/achive_list/',
            method: 'GET',
            params :{

            },
            timeout:10000
        }).success(function(data){
            $scope.achive_list = data
            console.dir(data)
        }).error(function(data){

        });
    };
    $scope.top = function(){
        $("body,html").scrollTop(0);
    }
    $scope.cli = function(e){
        if($(e.currentTarget).parent().parent().find(".post-content").hasClass("cli")){
            $(e.currentTarget).parent().parent().find(".post-content").removeClass("cli")
        }else{
            $(e.currentTarget).parent().parent().find(".post-content").addClass("cli")
        }
    }
    $scope.$on("ngRepeatFinished", function (repeatFinishedEvent, element){

    });
});
app.directive('onRepeatFinishedRender', function ($timeout) {
    return {
        restrict: 'A',
        link: function (scope, element, attr) {
            if (scope.$last === true) {
                $timeout(function () {
                    scope.$emit('ngRepeatFinished', element);
                });
            }
        }
    };
});



