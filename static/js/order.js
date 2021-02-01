var jsTabs = document.querySelectorAll('.js-tabs');

jsTabs.forEach(function (item) {
    var jsTriggers = item.querySelectorAll(".js-tab-trigger"),
        jsContents = item.querySelectorAll(".js-tab-content");

    jsTriggers.forEach(function (trigger) {
        trigger.addEventListener("click", function () {
            var id = this.getAttribute("data-tab"),
                content = item.querySelector(
                    '.js-tab-content[data-tab="' + id + '"]'
                ),
                activeTrigger = item.querySelector(".js-tab-trigger.active"),
                activeContent = item.querySelector(".js-tab-content.active");

            activeTrigger.classList.remove("active");
            trigger.classList.add("active");

            activeContent.classList.remove("active");
            content.classList.add("active");
        });
    });

});




