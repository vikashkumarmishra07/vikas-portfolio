// Old code
console.log("Portfolio Loaded Successfully");

// Fade-in animation on scroll
const elements = document.querySelectorAll('.fade-in');

function showOnScroll() {
    elements.forEach(el => {
        const position = el.getBoundingClientRect().top;
        if (position < window.innerHeight - 100) {
            el.classList.add('show');
        }
    });
}

window.addEventListener('scroll', showOnScroll);

// Run once when page loads
showOnScroll();
