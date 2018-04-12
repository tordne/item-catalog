$(document).ready(function(){

  $(".alert-close").click(function(){
    $(this).parentsUntil(".main-messages").hide();
  });

});