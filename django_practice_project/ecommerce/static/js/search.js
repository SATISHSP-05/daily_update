const input = document.getElementById("searchInput");
const box = document.getElementById("suggestions");

input.addEventListener("keyup", function () {
    const query = this.value;

    if (query.length < 2) {
        box.style.display = "none";
        return;
    }

    fetch(`/api/search/?q=${query}`)
        .then(res => res.json())
        .then(data => {
            box.innerHTML = "";
            data.forEach(item => {
                box.innerHTML += `<div onclick="location.href='/?q=${item}'">${item}</div>`;
            });
            box.style.display = "block";
        });
});
