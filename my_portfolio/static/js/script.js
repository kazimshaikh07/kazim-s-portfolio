const greetings = [
    "Hello",                // English
    "नमस्ते",                // Hindi
    "السلام علیکم",          // Urdu
    "Hola",                 // Spanish
    "Bonjour",              // French
    "こんにちは",             // Japanese
    "안녕하세요",              // Korean
    "Ciao",                 // Italian
    "Olá",                  // Portuguese
    "مرحبا"                  // Arabic
];

let index = 0;
let greetingElement; // initialize after DOM loads

function changeGreeting() {
    greetingElement.style.opacity = 0; // fade out
    setTimeout(() => {
        greetingElement.textContent = greetings[index];
        greetingElement.style.opacity = 1; // fade in
        index = (index + 1) % greetings.length;
    }, 500); // match CSS transition time
}

// Start greeting animation after page loads
document.addEventListener('DOMContentLoaded', function() {
    greetingElement = document.querySelector('#greeting');
    if (greetingElement) {
        setInterval(changeGreeting, 2000); // change every 2 seconds
    }
});
    


// Navbar scroll functionality
function updateNavbarVisibility() {
  const navbar = document.querySelector('.navbar');
  const hero = document.querySelector('.hero');
  if (!navbar || !hero) return;
  const heroHeight = hero.offsetHeight || 0;
  if (window.scrollY > heroHeight - 1) {
    navbar.classList.add('visible');
  } else {
    navbar.classList.remove('visible');
  }
}

window.addEventListener('load', updateNavbarVisibility);
window.addEventListener('scroll', updateNavbarVisibility);
window.addEventListener('resize', updateNavbarVisibility);

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Footer reveal light when in view
const footer = document.querySelector('.footer');
if (footer) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        footer.classList.add('revealed');
      }
    });
  }, { threshold: 0.2 });
  io.observe(footer);
}

// Custom cursor with tail
const cursorDot = document.querySelector('.cursor-dot');
const cursorTail = document.querySelector('.cursor-tail');
if (cursorDot && cursorTail) {
  let tailX = 0, tailY = 0;
  const ease = 0.15;

  window.addEventListener('mousemove', (e) => {
    const x = e.clientX;
    const y = e.clientY;
    cursorDot.style.transform = `translate(${x}px, ${y}px)`;
  });

  function animateTail() {
    const dotRect = cursorDot.getBoundingClientRect();
    const targetX = dotRect.left + dotRect.width / 2;
    const targetY = dotRect.top + dotRect.height / 2;
    tailX += (targetX - tailX) * ease;
    tailY += (targetY - tailY) * ease;
    cursorTail.style.transform = `translate(${tailX}px, ${tailY}px)`;
    requestAnimationFrame(animateTail);
  }
  animateTail();
}