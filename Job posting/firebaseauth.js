// Import Firebase SDK
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-auth.js";
import { getFirestore, setDoc, doc } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js";

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyC491xE4BYsG8Awv5fDjmCN2RGAC-lQw5g",
  authDomain: "job-postin.firebaseapp.com",
  projectId: "job-postin",
  storageBucket: "job-postin.appspot.com",
  messagingSenderId: "823216689485",
  appId: "1:823216689485:web:5de57144ae98fba7e1a704"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();
const db = getFirestore();

// Function to show messages
function showMessage(message, divId) {
  const messageDiv = document.getElementById(divId);
  messageDiv.style.display = "block";
  messageDiv.innerHTML = message;
  messageDiv.style.opacity = 1;
  setTimeout(() => {
    messageDiv.style.opacity = 0;
    setTimeout(() => { messageDiv.style.display = "none"; }, 500);
  }, 5000);
}

// Event listener for sign up
document.getElementById('submitSignUp').addEventListener('click', async (event) => {
  event.preventDefault();
  const email = document.getElementById('sEmail').value;
  const password = document.getElementById('sPassword').value;
  const confirmPassword = document.getElementById('confirmPassword').value;
  const firstName = document.getElementById('fName').value;
  const lastName = document.getElementById('lName').value;

  if (password !== confirmPassword) {
    showMessage('Passwords do not match!', 'signUpMessage');
    return;
  }

  try {
    const userCredential = await createUserWithEmailAndPassword(auth, email, password);
    const user = userCredential.user;
    
    const userData = {
      email: email,
      firstName: firstName,
      lastName: lastName
    };

    await setDoc(doc(db, "users", user.uid), userData);
    showMessage('Account Created Successfully', 'signUpMessage');
    setTimeout(() => { window.location.href = 'index.html'; }, 2000);
  } catch (error) {
    console.error("Error during sign up:", error);
    const errorCode = error.code;
    if (errorCode === 'auth/email-already-in-use') {
      showMessage('Email Address Already Exists !!!', 'signUpMessage');
    } else if (errorCode === 'auth/invalid-email') {
      showMessage('Invalid email address format.', 'signUpMessage');
    } else if (errorCode === 'auth/weak-password') {
      showMessage('Password should be at least 6 characters.', 'signUpMessage');
    } else {
      showMessage('Unable to create User: ' + error.message, 'signUpMessage');
    }
  }
});

// Event listener for sign in
document.getElementById('submitLogIn').addEventListener('click', async (event) => {
  event.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    showMessage('Login is successful', 'LogInMessage');
    
    const user = userCredential.user;
    localStorage.setItem('loggedInUserId', user.uid);
    setTimeout(() => { window.location.href = 'homepage.html'; }, 2000);
  } catch (error) {
    console.error("Error during sign in:", error);
    const errorCode = error.code;
    if (errorCode === 'auth/user-not-found' || errorCode === 'auth/wrong-password') {
      showMessage('Incorrect Email or Password', 'LogInMessage');
    } else {
      showMessage('Account does not Exist', 'LogInMessage');
    }
  }
});
