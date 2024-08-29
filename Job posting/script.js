// Ensure the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", function() {
    // Get the 'Signup' and 'Login' elements
    const signupLink = document.getElementById('signup');
    const loginLink = document.getElementById('login');
    
    // Get the forms
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    
    // Event listener for the Signup link
    if (signupLink) {
        signupLink.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent the default anchor click behavior
            loginForm.style.display = 'none';
            signupForm.style.display = 'block';
        });
    }
    
    // Event listener for the Login link
    if (loginLink) {
        loginLink.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent the default anchor click behavior
            signupForm.style.display = 'none';
            loginForm.style.display = 'block';
        });
    }
});
