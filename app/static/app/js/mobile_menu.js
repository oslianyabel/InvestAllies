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
});



