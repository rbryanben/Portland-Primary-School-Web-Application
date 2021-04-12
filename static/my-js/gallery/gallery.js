/* this function keeps track of the folders */
let PathTracking = [];


function trackPath(path) {

    PathTracking.push(path)

    //add to path 
    var pathBreadcrum = document.getElementById("breadcrum")

    //clear the breadcrum
    pathBreadcrum.innerHTML = "";

    for (var i = 0; i != PathTracking.length; i++) {
        pathBreadcrum.innerHTML += `<li class="breadcrumb-item"><a onclick="getFilesAt('${PathTracking[i]}')">` + PathTracking[i] + '</a></li>';
    }

}

function getFilesAt(folderName) {

    //clear path tracking
    var positionOfFolder = PathTracking.indexOf(folderName)

    PathTracking = PathTracking.slice(0, positionOfFolder)

    var url = document.location.href + 'filing/';
    var params = "folder=" + folderName;
    var http = new XMLHttpRequest();

    http.open("GET", url + "?" + params, true);
    http.onreadystatechange = function() {
        if (http.readyState == 4 && http.status == 200) {
            //add path to track list
            trackPath(folderName)
            document.getElementById("gallery-div").innerHTML = (http.responseText);
        }
    }
    http.send(null);
}

function getFiles(folderName) {
    var url = document.location.href + 'filing/';
    var params = "folder=" + folderName;
    var http = new XMLHttpRequest();

    http.open("GET", url + "?" + params, true);
    http.onreadystatechange = function() {
        if (http.readyState == 4 && http.status == 200) {
            //add path to track list
            trackPath(folderName)
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