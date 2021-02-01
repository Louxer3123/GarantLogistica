$('input.ShowOrHide3').click(function () {

    var checked = $("input.ShowOrHide3:checked");

    if (checked.length == 0) {
        $("div.ShowOrHide3").show();
    } else {
        $("div.ShowOrHide3").hide();
        $('div#' + $(this).val()).show();
    }
});

