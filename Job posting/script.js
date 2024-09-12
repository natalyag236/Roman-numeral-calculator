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
            e.preventDefault(); 
            loginForm.style.display = 'none';
            signupForm.style.display = 'block';
        });
    }
    
    // Event listener for the Login link
    if (loginLink) {
        loginLink.addEventListener('click', function(e) {
            e.preventDefault(); 
            signupForm.style.display = 'none';
            loginForm.style.display = 'block';
        });
    }

    // Password visibility toggle for Login Form
    const loginPasswordField = document.getElementById('password');
    const loginToggleIcon = document.querySelector('#loginForm .pw_hide');

    if (loginToggleIcon) {
        loginToggleIcon.addEventListener('click', function() {
            const type = loginPasswordField.getAttribute('type') === 'password' ? 'text' : 'password';
            loginPasswordField.setAttribute('type', type);
            this.classList.toggle('fa-eye');
            this.classList.toggle('fa-eye-slash');
        });
    }

    // Password visibility toggle for Signup Form
    const signupPasswordField = document.getElementById('sPassword');
    const confirmPasswordField = document.getElementById('confirmPassword');
    const signupToggleIcon = document.querySelector('#signupForm .pw_hide');

    if (signupToggleIcon) {
        signupToggleIcon.addEventListener('click', function() {
            const type = signupPasswordField.getAttribute('type') === 'password' ? 'text' : 'password';
            signupPasswordField.setAttribute('type', type);
            confirmPasswordField.setAttribute('type', type);
            this.classList.toggle('fa-eye');
            this.classList.toggle('fa-eye-slash');
        });
    }
    function postForm(event) {
        event.preventDefault(); // Prevent the default form submission
    
        const jobTitle = document.getElementById('jobtitle').value;
        const companyName = document.getElementById('companyname').value;
        const jobLocation = document.getElementById('joblocation').value;
        const jobDescription = document.getElementById('jobdescription').value;
        const jobType = document.getElementById('jobtype').value;
        const salary = document.getElementById('salary').value;
    
        // Create a new job listing element
        const jobListing = document.createElement('div');
        jobListing.classList.add('job-listing');
    
        // Populate the job listing with the entered information
        jobListing.innerHTML = `
            <h2>${jobTitle}</h2>
            <p><strong>Company:</strong> ${companyName}</p>
            <p><strong>Location:</strong> ${jobLocation}</p>
            <p><strong>Description:</strong> ${jobDescription}</p>
            <p><strong>Type:</strong> ${jobType}</p>
            <p><strong>Salary:</strong> ${salary}</p>
        `;
    
        // Add the job listing to the job listings container
        const jobListingsContainer = document.getElementById('job-listings');
        jobListingsContainer.appendChild(jobListing);
    
        // Clear the form fields
        document.getElementById('jobForm').reset();
    }
});
