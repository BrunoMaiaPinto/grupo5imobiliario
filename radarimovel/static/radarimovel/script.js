const form = document.querySelector(".formulario");

form.addEventListener("submit", function (e) {
  alert("Imovél adicionado com sucesso!");
});

document.getElementById("year").innerHTML = `${new Date().getFullYear()}`;
