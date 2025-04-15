document.addEventListener('DOMContentLoaded', function () {
    const hoverSound = new Audio("/static/sounds/bubble-popping.mp3");
    const popSound = new Audio("/static/sounds/bubble-pop.mp3");

    // hover-sound
    document.querySelectorAll('.hover-sound').forEach(link => {
        link.addEventListener('mouseenter', () => {
            hoverSound.currentTime = 0;
            hoverSound.play().catch(e => console.warn('Sound blocked:', e));
        });
    });

    // hover-pop-sound
    document.querySelectorAll('.hover-pop-sound').forEach(link => {
        link.addEventListener('mouseenter', () => {
            popSound.currentTime = 0;
            popSound.play().catch(e => console.warn('Sound blocked:', e));
        });
    });
});
