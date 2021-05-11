//check if document has fully loaded 
window.addEventListener('DOMContentLoaded', function(event) {

    //check if there is a query 
    var query = localStorage.getItem("searchQuery")
    if (query != null) {
        localStorage.removeItem("searchQuery")
        document.getElementById("search").value = query
        getNews("", query, "")
        return
    }

    getNews("", "", "")
})


//function to trigger search news 
function searchNews() {
    var fromDate = document.getElementById("date").value
    var search = document.getElementById("search").value
    var school = document.getElementById("school").value
    getNews(fromDate, search, school)
}

//function to get news 
function getNews(from, search, school) {
    var xmlhttp = new XMLHttpRequest()
    var url = window.location.href + "get/";
    xmlhttp.open("POST", url)
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState === 4) {
            document.querySelector(".news-body-content").innerHTML = xmlhttp.response
        }
    }
    xmlhttp.send(JSON.stringify({ "from": from, "search": search, "school": school }))
}