document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('navbar_menu_icon');
    const mobileMenu = document.getElementById('mobile_menu');
    const submenuToggle = document.querySelector('.mobile_menu_submenu_toggle');
    const submenu = document.querySelector('.mobile_menu_submenu');

    if (!menuIcon || !mobileMenu) return;

    menuIcon.addEventListener('click', function(e) {
        e.stopPropagation();
        mobileMenu.classList.toggle('mobile_menu_open');
    });

    if (submenuToggle && submenu) {
        submenuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            submenu.classList.toggle('open');
        });
    }

    document.addEventListener('click', function() {
        if (mobileMenu.classList.contains('mobile_menu_open')) {
            mobileMenu.classList.remove('mobile_menu_open');
        }
    });

    mobileMenu.addEventListener('click', function(e) {
        e.stopPropagation();
    });
});
