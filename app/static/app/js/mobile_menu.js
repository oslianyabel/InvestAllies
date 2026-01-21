document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.querySelector('.navbar__menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const submenuToggle = document.querySelector('.mobile-menu__item');
    const submenu = document.querySelector('.mobile-menu__submenu');
    const langBtn = document.querySelector('.navbar__language-btn');
    const langMenu = document.querySelector('.language-menu');
    const desktopSubmenuToggle = document.querySelector('.desktop-menu__toggle');
    const desktopSubmenu = document.querySelector('.desktop-menu__submenu');

    if (!menuIcon || !mobileMenu) return;

    menuIcon.addEventListener('click', function(e) {
        e.stopPropagation();
        mobileMenu.classList.toggle('mobile-menu--open');
        if (langMenu.classList.contains('language-menu--open')) {
            langMenu.classList.remove('language-menu--open');
        }
    });

    if (submenuToggle && submenu) {
        submenuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            submenu.classList.toggle('mobile-menu__submenu--open');
        });
    }

    if (langBtn && langMenu) {
        langBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            langMenu.classList.toggle('language-menu--open');
            if (mobileMenu.classList.contains('mobile-menu--open')) {
                mobileMenu.classList.remove('mobile-menu--open');
            }
        });
    }

    if (desktopSubmenuToggle && desktopSubmenu) {
        desktopSubmenuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            desktopSubmenu.classList.toggle('desktop-menu__submenu--open');
        });

        desktopSubmenuToggle.addEventListener('mouseenter', function() {
            desktopSubmenu.classList.add('desktop-menu__submenu--open');
        });

        desktopSubmenuToggle.addEventListener('mouseleave', function() {
            desktopSubmenu.classList.remove('desktop-menu__submenu--open');
        });
    }

    document.addEventListener('click', function() {
        if (mobileMenu.classList.contains('mobile-menu--open')) {
            mobileMenu.classList.remove('mobile-menu--open');
        }
        if (langMenu && langMenu.classList.contains('language-menu--open')) {
            langMenu.classList.remove('language-menu--open');
        }
        if (desktopSubmenu && desktopSubmenu.classList.contains('desktop-menu__submenu--open')) {
            desktopSubmenu.classList.remove('desktop-menu__submenu--open');
        }
    });

    mobileMenu.addEventListener('click', function(e) {
        e.stopPropagation();
    });

    if (langMenu) {
        langMenu.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }

    if (desktopSubmenu) {
        desktopSubmenu.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }

    // Accordion toggle
    const accordions = document.querySelectorAll('.accordion');
    accordions.forEach(function(accordion) {
        accordion.addEventListener('click', function(e) {
            e.stopPropagation();
            const content = this.nextElementSibling;
            if (content && content.classList.contains('accordion__content')) {
                content.classList.toggle('accordion__content--open');
            }
        });
    });

    // Desktop articles carousel (infinite circular sliding)
    (function setupDesktopArticlesCarousel() {
        const mq = window.matchMedia('(min-width: 1024px)');
        if (!mq.matches) return;

        const container = document.querySelector('.articles-desktop-carousel');
        if (!container) return;

        const leftBtn = container.querySelector('.articles-desktop-carousel__button--left');
        const rightBtn = container.querySelector('.articles-desktop-carousel__button--right');
        const posts = Array.from(container.querySelectorAll('.articles-desktop-carousel-post'));
        if (!leftBtn || !rightBtn || posts.length === 0) return;

        // Create wrapper for posts to control transform animations
        const wrapper = document.createElement('div');
        wrapper.className = 'articles-desktop-carousel__wrapper';
        wrapper.style.display = 'flex';
        const computedGap = getComputedStyle(container).gap || '20px';
        wrapper.style.gap = computedGap;
        wrapper.style.transition = 'transform 0.6s cubic-bezier(.22,.9,.32,1)';
        wrapper.style.willChange = 'transform';

        // Move post nodes into wrapper preserving order
        posts.forEach(post => wrapper.appendChild(post));

        // Insert wrapper into DOM: put it after left button (if left button exists)
        if (leftBtn && leftBtn.nextSibling) {
            container.insertBefore(wrapper, leftBtn.nextSibling);
        } else {
            container.appendChild(wrapper);
        }

        // Ensure container hides overflow so posts slide cleanly
        container.style.overflow = 'hidden';

        let isAnimating = false;

        function getStep() {
            const firstPost = wrapper.querySelector('.articles-desktop-carousel-post');
            if (!firstPost) return 0;
            const postRect = firstPost.getBoundingClientRect();
            const gapPx = parseFloat(computedGap) || 0;
            return Math.round(postRect.width + gapPx);
        }

        function moveLeft() {
            if (isAnimating) return;
            isAnimating = true;
            const step = getStep();
            // animate left: transform from 0 -> -step, then move first to end
            wrapper.style.transition = 'transform 0.6s cubic-bezier(.22,.9,.32,1)';
            wrapper.style.transform = `translateX(-${step}px)`;

            function onEnd() {
                wrapper.removeEventListener('transitionend', onEnd);
                // move first child to end
                const first = wrapper.firstElementChild;
                if (first) wrapper.appendChild(first);
                // reset transform without animation
                wrapper.style.transition = 'none';
                wrapper.style.transform = 'translateX(0)';
                // force reflow then restore transition
                // eslint-disable-next-line no-unused-expressions
                wrapper.offsetHeight;
                wrapper.style.transition = 'transform 0.6s cubic-bezier(.22,.9,.32,1)';
                isAnimating = false;
            }

            wrapper.addEventListener('transitionend', onEnd);
        }

        function moveRight() {
            if (isAnimating) return;
            isAnimating = true;
            const step = getStep();
            // move last to front instantly, set transform to -step, then animate to 0
            const last = wrapper.lastElementChild;
            if (!last) {
                isAnimating = false;
                return;
            }
            wrapper.style.transition = 'none';
            wrapper.insertBefore(last, wrapper.firstElementChild);
            // place wrapper shifted left by step
            wrapper.style.transform = `translateX(-${step}px)`;
            // force reflow
            // eslint-disable-next-line no-unused-expressions
            wrapper.offsetHeight;
            // animate to 0
            wrapper.style.transition = 'transform 0.6s cubic-bezier(.22,.9,.32,1)';
            wrapper.style.transform = 'translateX(0)';

            function onEnd() {
                wrapper.removeEventListener('transitionend', onEnd);
                // ensure clean state
                wrapper.style.transition = 'none';
                wrapper.style.transform = 'translateX(0)';
                // eslint-disable-next-line no-unused-expressions
                wrapper.offsetHeight;
                wrapper.style.transition = 'transform 0.6s cubic-bezier(.22,.9,.32,1)';
                isAnimating = false;
            }

            wrapper.addEventListener('transitionend', onEnd);
        }

        leftBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            moveRight(); // left button shows previous (shift right visually)
        });

        rightBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            moveLeft(); // right button shows next (shift left visually)
        });
    })();
});



