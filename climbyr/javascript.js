
// Open target page when header navbar pagelink is clicked, hide all other pages.
function openpage(evt, pagename) {
    
    // Declare all variables
    var i, page_container, page_container_default, page_links;
  
    // Get all elements with class="page-container" and hide them
    page_container = document.getElementsByClassName("page-container");
    for (i = 0; i < page_container.length; i++) {
        page_container[i].style.display = "none";
    }

    // Declare default tab
    page_container_default = document.getElementsByClassName("page-container-default");
    for (i = 0; i < page_container_default.length; i++) {
        page_container_default[i].style.display = "none";
    }
    
    // Get all elements with class="header-navbar-pagelinks" and remove the class "active"
    page_links = document.getElementsByClassName("pagelinks");
    for (i = 0; i < page_links.length; i++) {
        page_links[i].className = page_links[i].className.replace(" active", "");
    }
  
    // Show the current tab, and 
    document.getElementById(pagename).style.display = "block";

    // Add an "active" class to the button that opened the tab
    evt.currentTarget.className += " active";
}

// Toggle between adding and removing the "responsive" class to header-navbar when the user clicks on the icon
function openHeaderNavbarDropdown() {
    var header_navbar = document.getElementById("header-navbar");
    if (header_navbar.className === "header-navbar") {
        header_navbar.className += " responsive";
    } 
    
    else {
        header_navbar.className = "header-navbar";
    }
}