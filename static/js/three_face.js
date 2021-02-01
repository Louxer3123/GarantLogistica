$('input.ShowOrHide4').click(function () {

    var checked = $("input.ShowOrHide4:checked");

    if (checked.length == 0) {
        $("div.ShowOrHide4").show();
    } else {
        $("div.ShowOrHide4").hide();
        $('div#' + $(this).val()).show();
    }
});
