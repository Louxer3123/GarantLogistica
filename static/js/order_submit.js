const order_submit = document.querySelector("#submit");
const container = document.querySelector(".container-order");

order_submit.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});