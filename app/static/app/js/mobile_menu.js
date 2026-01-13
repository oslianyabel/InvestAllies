document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('navbar_menu_icon');
    const mobileMenu = document.getElementById('mobile_menu');
    const submenuToggle = document.querySelector('.mobile_menu_submenu_toggle');
    const submenu = document.querySelector('.mobile_menu_submenu');
    const langBtn = document.getElementById('navbar_lang_btn');
    const langMenu = document.getElementById('language_menu');

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

    document.addEventListener('click', function() {
        if (mobileMenu.classList.contains('mobile_menu_open')) {
            mobileMenu.classList.remove('mobile_menu_open');
        }
        if (langMenu && langMenu.classList.contains('language_menu_open')) {
            langMenu.classList.remove('language_menu_open');
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


