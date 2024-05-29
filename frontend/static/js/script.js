document.addEventListener('DOMContentLoaded', (event) => {

    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();

        const submitButton = document.querySelector('input[type="submit"]');
        if (submitButton) {
            submitButton.disabled = true;
        }

        let score = 0;
        quizData.forEach((item, index) => {
            const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
            const correctOption = document.querySelector(`input[name="question${index}"][value="${item.answer}"]`);
            const allOptions = document.querySelectorAll(`input[name="question${index}"]`);

            allOptions.forEach(option => option.disabled = true);

            if (correctOption) {
                correctOption.parentElement.style.color = 'green';
            }

            if (selectedOption) {
                if (selectedOption.value === item.answer) {
                    score++;
                } else {
                    selectedOption.parentElement.style.color = 'red';
                }
            }
        });

        let scoreElement = document.querySelector('#score');
        if (!scoreElement) {
            scoreElement = document.createElement('p');
            scoreElement.id = 'score';
            scoreElement.className = 'score mt-3';
            this.appendChild(scoreElement);
        }
        scoreElement.textContent = `Your score is ${score}/7`;
        
        if (score >= 3) {
            confetti.default({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        }
    });
});