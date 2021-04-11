function getFiles(folderName) {
    var url = document.location.href + 'filing/';
    var params = "folder=" + folderName;
    var http = new XMLHttpRequest();

    http.open("GET", url + "?" + params, true);
    http.onreadystatechange = function() {
        if (http.readyState == 4 && http.status == 200) {
            document.getElementById("gallery-div").innerHTML = (http.responseText);
        }
    }
    http.send(null);
}


document.addEventListener("DOMContentLoaded", function(event) {
    getFiles("root")
    createLightBox()
});


//create lightbox
const lightBox = document.createElement("div");


function createLightBox() {

    lightBox.id = "lightBox";
    document.querySelector('body').appendChild(lightBox);


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



}

lightBox.addEventListener("click", e => {
    if (e.target != e.currentTarget) {
        return
    }
    document.querySelector("body").style.overflow = "scroll"
    lightBox.classList.remove("active")
})

//procedure to add image to lightbox
function focusImage(obj) {
    document.querySelector("body").style.overflow = "hidden"
    lightBox.innerHTML = '';
    picViewing = document.createElement("img")
    picViewing.id = "picViewing"
    picViewing.src = obj.src
    lightBox.appendChild(picViewing)
    lightBox.classList.add("active")
}