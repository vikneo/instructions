let signinForm = document.querySelector('.signin-form');

let qweryForm = document.querySelector(".qwery-form")

function signIn() {

    // $(window).load(function () {
    //     console.log('reload')
    //     location.reload()
    // })
}

// function openSignIn() {
//     console.log('Open window');
//
//     $("#exampleModal").load("user/login/");
// }

const colors = document.querySelectorAll(".setting-color")

colors.forEach(stat => {

    console.log(stat.id)
    if (stat.id === "Температурный датчик фазы A") {
        stat.classList.add("text-bg-yellow");
    } else if (stat.id === "Температурный датчик фазы B") {
        stat.classList.add("text-bg-green");
    } else if (stat.id === "Температурный датчик фазы C") {
        stat.classList.add("text-bg-red");
    };
    return true;
});