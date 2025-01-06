document.getElementById('burger-menu-btn').addEventListener('click', function() {
    var mainMenu = document.getElementById('main-menu');
    mainMenu.classList.toggle('menu-hidden');
});

document.getElementById('scroll-button').addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});