/**
 * Scroll-triggered reveal animations using IntersectionObserver.
 * Adds the class 'scroll-visible' to elements with 'scroll-reveal' when they
 * enter the viewport, triggering CSS transitions.
 */
document.addEventListener('DOMContentLoaded', () => {
  const revealElements = document.querySelectorAll('.scroll-reveal');

  if (!revealElements.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('scroll-visible');
          
          // Trigger counter animation if element has counter-value class
          if (entry.target.classList.contains('counter-value')) {
            animateCounter(entry.target);
          } else {
            // Also check children for counter elements
            entry.target.querySelectorAll('.counter-value').forEach(animateCounter);
          }

          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealElements.forEach((el) => observer.observe(el));

  function animateCounter(el) {
    const target = parseFloat(el.getAttribute('data-target'));
    const duration = 2000; // 2 seconds
    const start = 0;
    const startTime = performance.now();

    function updateCounter(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      
      // Easing function (easeOutExpo)
      const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      
      const currentValue = start + (target - start) * easeProgress;
      
      el.textContent = `$ ${currentValue.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      }
    }

    requestAnimationFrame(updateCounter);
  }
});
