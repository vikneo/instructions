
function searchID() {
    let search = document.getElementById('search')[0].value;
    console.log(search)
    btn_search.onclick = function (event) {
        if (event.which == 1) {
            console.log(`${event.which}; ${search}`);
            form.onsubmit = function () { return true; }
        }
    };

    if (search == 0) {
        console.log('Строка поиска должна быть не пустой!');
        form.onsubmit = function () { return false; }
        alert('Строка поиска должна быть не пустой!')
    }
}

const colors = document.querySelectorAll(".setting-color")

colors.forEach(stat => {

    console.log(stat.id)
    if (stat.id === "Температурный датчик фазы A") {
        stat.classList.add("text-bg-yellow");
    } else if (stat.id === "Температурный датчик фазы B") {
        stat.classList.add("text-bg-green");
    } else if (stat.id === "Температурный датчик фазы C") {
        stat.classList.add("text-bg-red");
    } else if (stat.id === "Температурный датчик шина N") {
        stat.classList.add("text-bg-blue");
    };
    return true;
});