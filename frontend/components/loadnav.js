document.addEventListener("DOMContentLoaded", function () {
  const includes = document.querySelectorAll("[data-include]");

  includes.forEach(async function (el) {
    const file = el.getAttribute("data-include");
    try {
      const res = await fetch(file);
      if (!res.ok) throw new Error("Error cargando " + file);
      const html = await res.text();
      el.innerHTML = html;
      // Si el include es el nav, activa el menú hamburguesa
      if (file.includes('nav.html')) {
        setupHamburgerMenu();
      }
    } catch (err) {
      el.innerHTML = "<!-- Error cargando el componente -->";
      console.error(err);
    }
  });

  // Función para menú hamburguesa responsive
  function setupHamburgerMenu() {
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links-container');
    if (!navToggle || !navLinks) return;
    navToggle.addEventListener('click', function () {
      const isOpen = navLinks.classList.toggle('open');
      navToggle.classList.toggle('open', isOpen);
      document.body.classList.toggle('menu-open', isOpen);
      navToggle.setAttribute('aria-expanded', isOpen);
    });
    // Cerrar menú al hacer click en un enlace (en móvil)
    var navLinkEls = navLinks.querySelectorAll('.nav-link');
    navLinkEls.forEach(function(link) {
      link.addEventListener('click', function() {
        if (window.innerWidth <= 700) {
          navLinks.classList.remove('open');
          navToggle.classList.remove('open');
          document.body.classList.remove('menu-open');
          navToggle.setAttribute('aria-expanded', false);
        }
      });
    });
    // Cerrar menú al cambiar tamaño de pantalla
    window.addEventListener('resize', function() {
      if (window.innerWidth > 700) {
        navLinks.classList.remove('open');
        navToggle.classList.remove('open');
        document.body.classList.remove('menu-open');
        navToggle.setAttribute('aria-expanded', false);
      }
    });
  }
});
