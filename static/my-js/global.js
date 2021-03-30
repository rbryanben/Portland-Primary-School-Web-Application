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
    window.location.replace(location)
}