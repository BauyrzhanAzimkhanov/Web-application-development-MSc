document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/lessons/';  // Update with your Django API URL

    // Fetch lessons from the API
    function fetchLessons() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const lessonContainer = document.getElementById('lessons');
                lessonContainer.innerHTML = '';
                data.forEach(lesson => {
                    const lessonDiv = document.createElement('div');
                    lessonDiv.className = 'lesson';
                    lessonDiv.innerHTML = `
                        <h2>${lesson.title}</h2>
                        <p>${lesson.content}</p>
                        <button onclick="deleteLesson(${lesson.id})">Delete</button>
                    `;
                    lessonContainer.appendChild(lessonDiv);
                });
            })
            .catch(error => console.error('Error fetching lessons:', error));
    }

    // Delete a lesson
    window.deleteLesson = function(lessonId) {
        fetch(`${apiUrl}${lessonId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchLessons())
        .catch(error => console.error('Error deleting lesson:', error));
    }

    // Initial fetch of lessons
    fetchLessons();
});
