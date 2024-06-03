const usenameField = document.querySelector("#usernameField"); // id of the input field
const feedBackArea = document.querySelector(".invalid-feedback"); // class of the div where the error message will be displayed

usernameField.addEventListener("keyup", (e) => {

  const usernameVal = e.target.value; // value of the input field
  console.log("usernameVal:", usernameVal);

  usernameField.classList.remove("is-invalid"); //agrega la clase is-invalid al input. Esta clase es de bootstrap
  feedBackArea.style.display = "none"; //muestra el div con la clase invalid-feedback

  if (usernameVal.length > 0) {
    fetch("/authentication/validate-username", {  //fetch tiene la función de hacer una petición a una URL
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json()) //primera promesa, convierte la respuesta en un objeto json
      .then((data) => { //segunda promesa, recibe el objeto json y lo imprime en consola
        console.log("data", data);
      
        if (data.username_error) {
          usernameField.classList.add("is-invalid"); //agrega la clase is-invalid al input. Esta clase es de bootstrap
          feedBackArea.style.display = "block"; //muestra el div con la clase invalid-feedback
          feedBackArea.innerHTML=`<p>${data.username_error}</p>`; //agrega el mensaje de error al div con la clase invalid-feedback
        } 


      });
  }
});
