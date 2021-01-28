$('input.ShowOrHide2').click(function() {

  var checked = $("input.ShowOrHide2:checked");

  if (checked.length == 0) {
    $("div.ShowOrHide2").show();
  } else {
    $("div.ShowOrHide2").hide();
    $('div#' + $(this).val()).show();
  }
});