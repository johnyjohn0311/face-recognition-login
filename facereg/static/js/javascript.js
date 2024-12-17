let menu = document.querySelector('.menu');
let main = document.querySelector('.main');
let sidebar = document.querySelector('.sidebar');
let aSpans = document.querySelectorAll('.sidebar__btn__span');
menu.onclick = function() {
  let sidebarWidth = sidebar.clientWidth;
  aSpans.forEach(span => {
    span.classList.toggle('show');
  });
  
  console.log(sidebarWidth);
  if (sidebarWidth == 70) {
    main.style.left = 220 + 'px';
  } else {
    main.style.left = 70 + 'px';
  }
}
