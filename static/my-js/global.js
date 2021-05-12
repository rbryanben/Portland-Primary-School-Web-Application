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


function showDeveloperModal() {
    var developerModal = document.getElementById("developer-modal")

    if (!developerModal.classList.contains("show")) {
        developerModal.classList.add("show")
    }
}


function hideDeveloperModal() {
    var developerModal = document.getElementById("developer-modal")
    if (!developerModal.classList.contains("hide")) {
        developerModal.classList.remove("show")
    }
}



///
///procedure to show a live notification
///
function showLiveNotification(notificationText) {
    var notification = document.getElementById("live-notification")
    document.querySelector(".live-notification-text").innerHTML = notificationText;
    if (!notification.classList.contains("show")) {
        notification.classList.remove("hide")
        notification.classList.add("show")
        setTimeout(function() {
            if (!notification.classList.contains("hide")) {
                notification.classList.remove("show")
                notification.classList.add("hide")
            }
        }, 2000);
    }
}

function hideLiveNotification() {
    var notification = document.getElementById("live-notification")
    if (!notification.classList.contains("hide")) {
        notification.classList.remove("show")
        notification.classList.add("hide")
    }
}