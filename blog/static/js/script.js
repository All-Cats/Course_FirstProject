const burgerBtnOpen = document.getElementById('open');
const burgerBtnClose = document.getElementById('close');
const burgerWrapper = document.querySelector('.burger-wrapper');
const openText = document.getElementById('open-text');
const text =  document.getElementById('text');
const body = document.body;
burgerBtnOpen.addEventListener('click', () => {
    burgerWrapper.style.display = 'flex';
    body.style.overflow = 'hidden';
});

burgerBtnClose.addEventListener('click', () => {
    burgerWrapper.style.display = 'none';
    body.style.overflow = 'auto';
});

openText.addEventListener('click', () => {
    openText.style.display = 'none';
    text.style.display = 'block';
});