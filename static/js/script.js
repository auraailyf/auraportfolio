// DOM Elements
const navbar = document.getElementById('navbar');
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');
const ctaButton = document.getElementById('cta-button');
const contactForm = document.getElementById('contact-form');

// Navbar scroll effect
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Mobile menu toggle
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on links
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

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

// CTA button click effect
ctaButton.addEventListener('click', () => {
    document.getElementById('contact').scrollIntoView({
        behavior: 'smooth'
    });
});

// Intersection Observer for scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
    const animateElements = [
        { selector: '.section-title', class: 'fade-in' },
        { selector: '.about-description', class: 'fade-in' },
        { selector: '.stat-item', class: 'fade-in' },
        { selector: '.service-card', class: 'fade-in' },
        { selector: '.portfolio-item', class: 'fade-in' },
        { selector: '.team-member', class: 'fade-in' },
        { selector: '.contact-item', class: 'slide-in-left' },
        { selector: '.contact-form', class: 'slide-in-right' }
    ];
    
    animateElements.forEach(({ selector, class: className }) => {
        document.querySelectorAll(selector).forEach((el, index) => {
            el.classList.add(className);
            el.style.transitionDelay = `${index * 0.1}s`;
            observer.observe(el);
        });
    });
});


// ====================================================================
// =================== CONTACT FORM SUBMISSION LOGIC ==================
// ====================================================================
contactForm.addEventListener('submit', async (e) => { // Added 'async' here
    e.preventDefault();
    
    const formData = new FormData(contactForm);
    const name = formData.get('name').trim();
    const email = formData.get('email').trim();
    const message = formData.get('message').trim();
    
    // Clear previous errors
    document.querySelectorAll('.error-message').forEach(error => {
        error.classList.remove('show');
    });
    
    let isValid = true;
    
    // Validate name
    if (name.length < 2) {
        showError('name-error', 'Name must be at least 2 characters long');
        isValid = false;
    }
    
    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showError('email-error', 'Please enter a valid email address');
        isValid = false;
    }
    
    // Validate message
    if (message.length < 10) {
        showError('message-error', 'Message must be at least 10 characters long');
        isValid = false;
    }
    
    if (isValid) {
        const submitButton = contactForm.querySelector('.send-button');
        const originalText = submitButton.textContent;

        submitButton.textContent = 'Sending...';
        submitButton.disabled = true;

        try {
            // Send the data to your Django backend endpoint
            const response = await fetch('/api/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, email, message }),
            });

            const result = await response.json();

            if (!response.ok) {
                // Handle errors from the server (like 500, 400 status codes)
                throw new Error(result.message || 'An unknown error occurred.');
            }

            // --- SUCCESS ---
            submitButton.textContent = 'Message Sent!';
            submitButton.style.background = 'linear-gradient(45deg, #10b981, #059669)';
            contactForm.reset();
            
            // Reset the button after 2 seconds
            setTimeout(() => {
                submitButton.textContent = originalText;
                submitButton.disabled = false;
                submitButton.style.background = 'linear-gradient(45deg, #dc2626, #ef4444)';
            }, 2000);

        } catch (error) {
            // --- ERROR ---
            console.error('Submission failed:', error);
            alert(`Error: ${error.message}`); // Show an error popup to the user
            
            // Reset the button immediately on failure
            submitButton.textContent = originalText;
            submitButton.disabled = false;
        }
    }
});

function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    errorElement.textContent = message;
    errorElement.classList.add('show');
}