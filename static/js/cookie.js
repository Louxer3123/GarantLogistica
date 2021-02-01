var panel = document.querySelector('.js-notification'),
    panelButton = panel.querySelector('.button');

if (localStorage['cookie-data'] == undefined) {
    panel.classList.remove('hidden');
}

panelButton.addEventListener('click', function () {
    panel.classList.add('hidden');
    localStorage['cookie-data'] = true;
});