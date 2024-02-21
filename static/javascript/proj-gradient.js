document.addEventListener('DOMContentLoaded', function() {
    var interBubble = document.querySelector('.interactive');
    var curX = 0;
    var curY = 0;
    var tgX = 0;
    var tgY = 0;
    function move() {
        curX += (tgX - curX) / 1;
        curY += (tgY - curY) / 1;
        interBubble.style.transform = "translate(" + Math.round(curX) + "px, " + Math.round(curY) + "px)";
        requestAnimationFrame(move);
    }
    window.addEventListener('mousemove', function(event) {
        tgX = event.clientX;
        tgY = event.clientY;
    });
    move();
});