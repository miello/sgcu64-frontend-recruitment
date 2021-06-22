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

  // Email Format
  if (data["email"] !== "") {
    const email = data["email"];

    // Reference: http://emailregex.com/
    var mailformat =
      /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!mailformat.test(email)) {
      invalidList.push("Email badly formatted");
      addInvalidInputStyle("email");
    }
  }


  /* USER CODE END: What happened next after recieve form data (Optional) */
})
