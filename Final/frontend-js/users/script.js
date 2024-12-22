document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/users/';  // Update with your Django API URL

    // Fetch users from the API
    function fetchUsers() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const userContainer = document.getElementById('users');
                userContainer.innerHTML = '';
                data.forEach(user => {
                    const userDiv = document.createElement('div');
                    userDiv.className = 'user';
                    userDiv.innerHTML = `
                        <h2>${user.username}</h2>
                        <p>${user.email}</p>
                        <button onclick="deleteUser(${user.id})">Delete</button>
                    `;
                    userContainer.appendChild(userDiv);
                });
            })
            .catch(error => console.error('Error fetching users:', error));
    }

    // Delete a user
    window.deleteUser = function(userId) {
        fetch(`${apiUrl}${userId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchUsers())
        .catch(error => console.error('Error deleting user:', error));
    }

    // Initial fetch of users
    fetchUsers();
});
