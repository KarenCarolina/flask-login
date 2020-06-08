btn=document.querySelector(".burger-button");
menu=document.querySelector(".menu");
btn.addEventListener("click", function(){
    
    if (menu.classList.contains('is-active')) {
        menu.classList.remove('is-active');
      } else {
        menu.classList.add('is-active');
      }
})