// script.js

document.addEventListener("DOMContentLoaded", function() {
    fetch('YOUR_FUNCTION_URL')
        .then(response => response.json())
        .then(data => {
            document.getElementById('countDisplay').textContent = data.count;
        })
        .catch(error => {
            console.error('Error fetching count:', error);
            document.getElementById('countDisplay').textContent = 'Error';
        });
});


function toggleMenu () {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open")
    icon.classList.toggle("open")
}