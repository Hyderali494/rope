$(document).ready(function(){
  var host = "http://0.0.0.0:8856"

  function api_call(url, method, data) {

    var url = host + url
    $.ajax({
      url: url,
      success: function(response) {
        alert(response);
      }
    });
  }


  $("body .loginmodal-submit").on("click", function(event){
     api_call("/user_login/", "POST", {})
     event.preventDefault();
  });


});
