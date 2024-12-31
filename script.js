// scripts.js
document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("disclaimer-popup");
    const closeButton = document.getElementById("close-popup");

    // Automatically close the popup after 2 seconds
    setTimeout(() => {
        popup.style.display = "none";
    }, 2000);

    // Close the popup when the close button is clicked
    closeButton.addEventListener("click", () => {
        popup.style.display = "none";
    });
});
