window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 0) {
        navbar.style.backgroundColor = '#191e29'; 
    } else {
        navbar.style.backgroundColor = 'transparent'; 
    }
});