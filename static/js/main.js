$scope.submitButtonText = 'Submit';
$scope.loading = false;

$http.post('/images', {'url': userInput}).
  success(function(results) {
    $log.log(results);
    getWordCount(results);
    $scope.wordcounts = null;
    $scope.loading = true;
    $scope.submitButtonText = 'Loading...';
  }).
  error(function(error) {
    $log.log(error);
  });

var poller = function() {
    // fire another request
    $http.get('/results/'+jobID).success(function(data, status, headers, config) {
        if(status === 202) {
          $log.log(data, status);
        } else if (status === 200){
          $log.log(data);
          $scope.loading = false;
          $scope.submitButtonText = "Submit";
          $scope.wordcounts = data;
          $timeout.cancel(timeout);
          return false;
        }
        // continue to call the poller() function every 2 seconds
        // until the timeout is cancelled
        timeout = $timeout(poller, 2000);
      }).
      error(function(error) {
        $log.log(error);
        $scope.loading = false;
        $scope.submitButtonText = "Submit";
        $scope.urlerror = true;
    });
};