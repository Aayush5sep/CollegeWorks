const ibox = document.getElementById('initial-categories');
const fbox = document.getElementById('final-categories');
const btn = document.getElementById('catbtn');

btn.addEventListener('click', function handleClick(){
  fbox.style.display = 'block';
  ibox.style.display = 'none';
  fbox.scrollIntoView(true);
});