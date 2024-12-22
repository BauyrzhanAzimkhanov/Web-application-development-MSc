document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/quizzes/';  // Update with your Django API URL

    // Fetch quizzes from the API
    function fetchQuizzes() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const quizContainer = document.getElementById('quizzes');
                quizContainer.innerHTML = '';
                data.forEach(quiz => {
                    const quizDiv = document.createElement('div');
                    quizDiv.className = 'quiz';
                    quizDiv.innerHTML = `
                        <h2>${quiz.title}</h2>
                        <p>${quiz.course.title}</p>
                        <button onclick="deleteQuiz(${quiz.id})">Delete</button>
                    `;
                    quizContainer.appendChild(quizDiv);
                });
            })
            .catch(error => console.error('Error fetching quizzes:', error));
    }

    // Delete a quiz
    window.deleteQuiz = function(quizId) {
        fetch(`${apiUrl}${quizId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchQuizzes())
        .catch(error => console.error('Error deleting quiz:', error));
    }

    // Initial fetch of quizzes
    fetchQuizzes();
});
