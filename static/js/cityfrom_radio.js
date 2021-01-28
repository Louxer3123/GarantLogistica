$('input.ShowOrHide1').click(function() {

  var checked = $("input.ShowOrHide1:checked");

  if (checked.length == 0) {
    $("div.ShowOrHide1").show();
  } else {
    $("div.ShowOrHide1").hide();
    $('div#' + $(this).val()).show();
  }
});