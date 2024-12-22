document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/user_progress/';  // Update with your Django API URL

    // Fetch user progress from the API
    function fetchUserProgress() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const userProgressContainer = document.getElementById('user-progress');
                userProgressContainer.innerHTML = '';
                data.forEach(userProgress => {
                    const userProgressDiv = document.createElement('div');
                    userProgressDiv.className = 'user-progress';
                    userProgressDiv.innerHTML = `
                        <h2>${userProgress.user.username}</h2>
                        <p>Course: ${userProgress.course.title}</p>
                        <p>Completed Lessons: ${userProgress.completed_lessons}</p>
                        <p>Quiz Scores: ${userProgress.quiz_scores}</p>
                        <button onclick="deleteUserProgress(${userProgress.id})">Delete</button>
                    `;
                    userProgressContainer.appendChild(userProgressDiv);
                });
            })
            .catch(error => console.error('Error fetching user progress:', error));
    }

    // Delete a user progress
    window.deleteUserProgress = function(userProgressId) {
        fetch(`${apiUrl}${userProgressId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchUserProgress())
        .catch(error => console.error('Error deleting user progress:', error));
    }

    // Initial fetch of user progress
    fetchUserProgress();
});
