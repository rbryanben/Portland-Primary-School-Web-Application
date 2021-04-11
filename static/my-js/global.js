///
/// This function is for the loading, it waits for the page to load before it displays 
/// The page
///
window.onload = function() {
    if (document.readyState == 'complete') {
        document.getElementById("load").style.display = "none";
    }
}

////
/// procedure to relocate window
////
function goto(location) {
    window.location.href = location
}


//light box
const lightBox = document.createElement("div")
lightBox.id = "lightBox"
lightBox.classList
document.body.appendChild(lightBox)


pictures = document.querySelectorAll(".image-panel-image")
pictures.forEach(pic => {
    pic.addEventListener("click", function() {
        lightBox.innerHTML = ''
        picViewing = document.createElement("img")
        picViewing.id = "picViewing"
        picViewing.src = pic.src
        lightBox.appendChild(picViewing)
        lightBox.classList.add("active")
    })
});


lightBox.addEventListener("click", e => {
    if (e.target != e.currentTarget) {
        return
    }

    lightBox.classList.remove("active")
})