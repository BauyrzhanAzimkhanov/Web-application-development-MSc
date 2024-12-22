document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/enrollments/';  // Update with your Django API URL

    // Fetch enrollments from the API
    function fetchEnrollments() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const enrollmentContainer = document.getElementById('enrollments');
                enrollmentContainer.innerHTML = '';
                data.forEach(enrollment => {
                    const enrollmentDiv = document.createElement('div');
                    enrollmentDiv.className = 'enrollment';
                    enrollmentDiv.innerHTML = `
                        <h2>${enrollment.user.username} - ${enrollment.course.title}</h2>
                        <p>${enrollment.status}</p>
                        <button onclick="deleteEnrollment(${enrollment.id})">Delete</button>
                    `;
                    enrollmentContainer.appendChild(enrollmentDiv);
                });
            })
            .catch(error => console.error('Error fetching enrollments:', error));
    }

    // Delete an enrollment
    window.deleteEnrollment = function(enrollmentId) {
        fetch(`${apiUrl}${enrollmentId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchEnrollments())
        .catch(error => console.error('Error deleting enrollment:', error));
    }

    // Initial fetch of enrollments
    fetchEnrollments();
});
