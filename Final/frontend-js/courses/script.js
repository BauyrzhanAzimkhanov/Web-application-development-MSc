document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/courses/';  // Update with your Django API URL

    // Fetch courses from the API
    function fetchCourses() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const courseContainer = document.getElementById('courses');
                courseContainer.innerHTML = '';
                data.forEach(course => {
                    const courseDiv = document.createElement('div');
                    courseDiv.className = 'course';
                    courseDiv.innerHTML = `
                        <h2>${course.title}</h2>
                        <p>${course.description}</p>
                        <button onclick="deleteCourse(${course.id})">Delete</button>
                    `;
                    courseContainer.appendChild(courseDiv);
                });
            })
            .catch(error => console.error('Error fetching courses:', error));
    }

    // Delete a course
    window.deleteCourse = function(courseId) {
        fetch(`${apiUrl}${courseId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchCourses())
        .catch(error => console.error('Error deleting course:', error));
    }

    // Initial fetch of courses
    fetchCourses();
});
