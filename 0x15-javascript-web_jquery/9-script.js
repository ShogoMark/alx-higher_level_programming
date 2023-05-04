$(document).ready(function(){
$.get({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  dataType: 'jsonp',
  success: function(data){
   $("DIV#hello").text(data.hello);
 }
});
});
