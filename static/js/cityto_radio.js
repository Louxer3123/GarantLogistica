$('input.ShowOrHide').click(function() {

  var checked = $("input.ShowOrHide:checked");

  if (checked.length == 0) {
    $("div.ShowOrHide").show();
  } else {
    $("div.ShowOrHide").hide();
    $('div#' + $(this).val()).show();
  }
});