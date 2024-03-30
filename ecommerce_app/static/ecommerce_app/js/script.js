function activeTab() {
    var path = window.location.pathname + window.location.search;
    var activeLink = document.querySelector('a[href="' + path + '"]');

    if(activeLink) {
        activeLink.classList.add('active');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    function toggleButtonVisibility(productsElement, buttonElement) {
        productsElement.addEventListener('mouseover', () => {
            buttonElement.classList.add('showButton');
        });
        productsElement.addEventListener('mouseout', () => {
            buttonElement.classList.remove('showButton');
        });
    }

    const productsIntro = document.getElementById('productsIntro');
    const productsIntroButton = document.getElementById('productsIntroButton');
    toggleButtonVisibility(productsIntro, productsIntroButton);

    const womenProducts = document.getElementById('womenProducts');
    const womenButton = document.getElementById('womenButton');
    toggleButtonVisibility(womenProducts, womenButton);

    const menProducts = document.getElementById('menProducts');
    const menButton = document.getElementById('menButton');
    toggleButtonVisibility(menProducts, menButton);

    const kidsProducts = document.getElementById('kidsProducts');
    const kidsButton = document.getElementById('kidsButton');
    toggleButtonVisibility(kidsProducts, kidsButton);
});