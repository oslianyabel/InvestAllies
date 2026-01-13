document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('navbar_menu_icon');
    const mobileMenu = document.getElementById('mobile_menu');
    const submenuToggle = document.querySelector('.mobile_menu_submenu_toggle');
    const submenu = document.querySelector('.mobile_menu_submenu');
    const langBtn = document.getElementById('navbar_lang_btn');
    const langMenu = document.getElementById('language_menu');
    const desktopSubmenuToggle = document.querySelector('.desktop_menu_submenu_toggle');
    const desktopSubmenu = document.querySelector('.desktop_menu_submenu');

    if (!menuIcon || !mobileMenu) return;

    menuIcon.addEventListener('click', function(e) {
        e.stopPropagation();
        mobileMenu.classList.toggle('mobile_menu_open');
        if (langMenu.classList.contains('language_menu_open')) {
            langMenu.classList.remove('language_menu_open');
        }
    });

    if (submenuToggle && submenu) {
        submenuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            submenu.classList.toggle('open');
        });
    }

    if (langBtn && langMenu) {
        langBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            langMenu.classList.toggle('language_menu_open');
            if (mobileMenu.classList.contains('mobile_menu_open')) {
                mobileMenu.classList.remove('mobile_menu_open');
            }
        });
    }

    if (desktopSubmenuToggle && desktopSubmenu) {
        desktopSubmenuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            desktopSubmenu.classList.toggle('open');
        });

        desktopSubmenuToggle.addEventListener('mouseenter', function() {
            desktopSubmenu.classList.add('open');
        });

        desktopSubmenuToggle.addEventListener('mouseleave', function() {
            desktopSubmenu.classList.remove('open');
        });
    }

    document.addEventListener('click', function() {
        if (mobileMenu.classList.contains('mobile_menu_open')) {
            mobileMenu.classList.remove('mobile_menu_open');
        }
        if (langMenu && langMenu.classList.contains('language_menu_open')) {
            langMenu.classList.remove('language_menu_open');
        }
        if (desktopSubmenu && desktopSubmenu.classList.contains('open')) {
            desktopSubmenu.classList.remove('open');
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
            if (content && content.classList.contains('accordion_content')) {
                content.classList.toggle('open');
            }
        });
    });
});



