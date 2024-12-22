document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/quiz_questions/';  // Update with your Django API URL

    // Fetch quiz questions from the API
    function fetchQuizQuestions() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const quizQuestionContainer = document.getElementById('quiz-questions');
                quizQuestionContainer.innerHTML = '';
                data.forEach(quizQuestion => {
                    const quizQuestionDiv = document.createElement('div');
                    quizQuestionDiv.className = 'quiz-question';
                    quizQuestionDiv.innerHTML = `
                        <h2>${quizQuestion.question_text}</h2>
                        <p>A: ${quizQuestion.option_a}</p>
                        <p>B: ${quizQuestion.option_b}</p>
                        <p>C: ${quizQuestion.option_c}</p>
                        <p>D: ${quizQuestion.option_d}</p>
                        <p>Correct: ${quizQuestion.correct_option}</p>
                        <button onclick="deleteQuizQuestion(${quizQuestion.id})">Delete</button>
                    `;
                    quizQuestionContainer.appendChild(quizQuestionDiv);
                });
            })
            .catch(error => console.error('Error fetching quiz questions:', error));
    }

    // Delete a quiz question
    window.deleteQuizQuestion = function(quizQuestionId) {
        fetch(`${apiUrl}${quizQuestionId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchQuizQuestions())
        .catch(error => console.error('Error deleting quiz question:', error));
    }

    // Initial fetch of quiz questions
    fetchQuizQuestions();
});
