const button = document.querySelector('#button');

const jsConfetti = new JSConfetti();

button.addEventListener('click', () => {
    jsConfetti.addConfetti({
        confettiRadius: 5,
        confettiNumber: 1500,
        spread: 200
    })
})
