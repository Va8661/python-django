const form = document.getElementById("appointment-form");
const tokenNumberEl = document.getElementById("token-number");

form.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevent the form from submitting normally

  // Generate a random token number between 1 and 100
  const tokenNumber = Math.floor(Math.random() * 100) + 1;

  // Display the token number on the page
  tokenNumberEl.textContent = `Your token number is: ${tokenNumber}`;
});
