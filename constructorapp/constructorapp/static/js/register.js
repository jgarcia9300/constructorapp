const usernameField = document.querySelector("#usernameField"); // id of the input field
const feedBackArea = document.querySelector(".invalid-feedback"); // class of the div where the error message will be displayed
const emailField = document.querySelector("#emailField"); // id of the input field
const emailFeedBackArea = document.querySelector(".emailFeedBackArea"); // class of the div where the error message will be displayed
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput"); // class of the div where the success message will be displayed

emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value; // value of the input field

  console.log("emailVal:", emailVal);

  emailField.classList.remove("is-invalid"); //agrega la clase is-invalid al input. Esta clase es de bootstrap
  emailFeedBackArea.style.display = "none"; //muestra el div con la clase invalid-feedback

  if (emailVal.length > 0) {
    fetch("/authentication/validate-email", {
      //fetch tiene la función de hacer una petición a una URL
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json()) //primera promesa, convierte la respuesta en un objeto json
      .then((data) => {
        //segunda promesa, recibe el objeto json y lo imprime en consola
        console.log("data", data);

        if (data.email_error) {
          emailField.classList.add("is-invalid"); //agrega la clase is-invalid al input. Esta clase es de bootstrap
          emailFeedBackArea.style.display = "block"; //jace visible el elemento en la pagina web como un elemento de bloque
          emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`; //agrega el mensaje de error al div con la clase invalid-feedback
        }
      });
  }
});

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value; // value of the input field

  usernameSuccessOutput.textContent = `Checking ${usernameVal}`; //agrega el mensaje de exito al div con la clase usernameSuccessOutput

  console.log("usernameVal:", usernameVal);

  usernameField.classList.remove("is-invalid"); //agrega la clase is-invalid al input. Esta clase es de bootstrap
  feedBackArea.style.display = "none"; //muestra el div con la clase invalid-feedback

  if (usernameVal.length > 0) {
    fetch("/authentication/validate-username", {
      //fetch tiene la función de hacer una petición a una URL
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json()) //primera promesa, convierte la respuesta en un objeto json
      .then((data) => {
        //segunda promesa, recibe el objeto json y lo imprime en consola
        console.log("data", data);
        usernameSuccessOutput.style.display = "block"; //muestra el div con la clase usernameSuccessOutput
        if (data.username_error) {
          usernameField.classList.add("is-invalid"); //agrega la clase is-invalid al input. Esta clase es de bootstrap
          feedBackArea.style.display = "block"; //muestra el div con la clase invalid-feedback
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`; //agrega el mensaje de error al div con la clase invalid-feedback
        }
      });
  }
});
