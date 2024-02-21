const carousel = document.querySelector('.carousel');
const images = document.querySelectorAll('.carousel img');
let index = 0;
function showImage(index) {
images.forEach((image, i) => {
    if (i === index) {
    image.style.opacity = '1';
    } else {
    image.style.opacity = '0';
    }
});
}
function nextImage() {
index = (index + 1) % images.length;
showImage(index);
}
showImage(index);
setInterval(nextImage, 3000); 