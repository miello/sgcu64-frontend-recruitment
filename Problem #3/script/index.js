const form = document.getElementById("register-form");
const input = document.getElementsByTagName("input");

function addInvalidInputStyle(name) {
  document.getElementsByName(name)[0].classList.add("invalid-input");
}

function removeInvalidInputStyle(name) {
  document.getElementsByName(name)[0].classList.remove("invalid-input");
}

for (let i = 0; i < input.length; i++) {
  input[i].addEventListener("input", () => {
    input[i].classList.remove("invalid-input");
  });
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const data = {};
  const invalidList = [];

  for (const [key, value] of formData.entries()) {
    /* USER CODE Begin: Validate data */
    removeInvalidInputStyle(key);
    data[key] = value;
    // Check is empty
    if (value === "") {
      addInvalidInputStyle(key);
      invalidList.push(`Required ${key}`);
    }
    /* USER CODE Begin: Validate data */
  }
  console.log(data)
  /* USER CODE Begin: What happened next after recieve form data (Optional) */

  /* USER CODE END: What happened next after recieve form data (Optional) */
})
