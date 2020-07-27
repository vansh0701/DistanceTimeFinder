const form =document.querySelector('#inputform');
const output_value=document.querySelector('#output');
const origin=document.querySelector('#origin');
const destination=document.querySelector('#destination');
const submit=document.querySelector('#submit');

form.addEventListener('submit', (e)=>{
	e.preventDefault();
	output_value.classList.add('output');
	origin.style.display = 'none';
	destination.style.display = 'none';
	submit.style.display = 'none';

	output_value.innerHTML= '<h1>21Km</h1>'


});
