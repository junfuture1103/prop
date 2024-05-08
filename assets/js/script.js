function toggleDropdown(menuId) {
    var dropdown = document.getElementById(menuId);
    if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
    } else {
        dropdown.style.display = "block";
    }
}
