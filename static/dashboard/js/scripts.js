// Получаем элементы DOM
var modal = document.getElementById("myModal");
var btn = document.getElementById("myButton");
var okButton = document.querySelector(".okButton");

// Когда пользователь нажимает на кнопку, открываем модальное окно
btn.onclick = function() {
  modal.style.display = "block";
}

// Когда пользователь нажимает на кнопку "ОК", закрываем окно
okButton.onclick = function() {
  modal.style.display = "none";
}

// Когда пользователь кликает за пределами модального окна, закрываем его
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
