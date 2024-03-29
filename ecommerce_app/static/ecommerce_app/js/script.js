function activeTab() {
    var path = window.location.pathname + window.location.search;
    var activeLink = document.querySelector('a[href="' + path + '"]');

    if(activeLink) {
        activeLink.classList.add('active');
    }
}