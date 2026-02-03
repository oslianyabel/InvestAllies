document.addEventListener('DOMContentLoaded', function () {
    const title = document.querySelector('.hero__image-title');
    const description = document.querySelector('.hero__image-description');
    const buttons = document.querySelector('.hero__image-buttons');
    const img1 = document.querySelector('.hero__image-1');
    const img2 = document.querySelector('.hero__image-2');
    const img3 = document.querySelector('.hero__image-3');
    const img4 = document.querySelector('.hero__image-4');

    // Effect 1: Title fade-in happens automatically via CSS animation (1s)

    // Effect 2: Starts after 1 second
    setTimeout(function () {
        // Start title oscillation (runs once, then title stays visible permanently)
        if (title) {
            title.classList.add('oscillating');
        }

        // Slide in description and buttons
        if (description) {
            description.classList.add('slide-in');
        }
        if (buttons) {
            buttons.classList.add('slide-in');
        }

        // Image sequence: 1 -> 2 -> 3 -> 4 (1 second each, crossfade to prevent flicker)
        // Transition to image 2 after 1 second
        setTimeout(function () {
            if (img2) {
                img2.style.zIndex = '3';
                img2.style.opacity = '1';
            }
            // Wait slightly longer than transition (0.5s) to hide previous
            setTimeout(function () {
                if (img1) img1.style.opacity = '0';
            }, 600);
        }, 1000);

        // Transition to image 3 after 2 seconds
        setTimeout(function () {
            if (img3) {
                img3.style.zIndex = '4';
                img3.style.opacity = '1';
            }
            setTimeout(function () {
                if (img2) img2.style.opacity = '0';
            }, 600);
        }, 2000);

        // Transition to image 4 (final) after 3 seconds
        setTimeout(function () {
            if (img4) {
                img4.style.zIndex = '5';
                img4.style.opacity = '1';
            }
            setTimeout(function () {
                if (img3) img3.style.opacity = '0';
            }, 600);
        }, 3000);

    }, 1000); // Start Effect 2 after 1 second
});
