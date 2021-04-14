function getEvents(from, keywords, location) {
    var xmlhttp = new XMLHttpRequest();
    var url = window.location.href + "get/";
    xmlhttp.open("POST", url)
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState === 4) {
            document.getElementById("event-results-content").innerHTML = xmlhttp.response;
        }
    }
    xmlhttp.send(JSON.stringify({ "from": from, "keywords": keywords, "location": location }))
}

document.addEventListener("DOMContentLoaded", function() {
    findEvents();
});

function findEvents() {
    getEvents(document.getElementById("date").value, document.getElementById("search").value, document.getElementById("location").value);
}