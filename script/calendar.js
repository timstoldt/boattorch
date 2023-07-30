var list = document.getElementById("days");
var items = list.getElementsByTagName("li").getElementsByTagName("span");
for (var i = 0; i < items.length; i++) {
  items[i].addEventListener("click", function() {
    element.classList.add("active");
  });
}
