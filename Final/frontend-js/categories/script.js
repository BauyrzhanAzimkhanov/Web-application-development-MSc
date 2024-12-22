document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/categories/';  // Update with your Django API URL

    // Fetch categories from the API
    function fetchCategories() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const categoryContainer = document.getElementById('categories');
                categoryContainer.innerHTML = '';
                data.forEach(category => {
                    const categoryDiv = document.createElement('div');
                    categoryDiv.className = 'category';
                    categoryDiv.innerHTML = `
                        <h2>${category.name}</h2>
                        <p>${category.description}</p>
                        <button onclick="deleteCategory(${category.id})">Delete</button>
                    `;
                    categoryContainer.appendChild(categoryDiv);
                });
            })
            .catch(error => console.error('Error fetching categories:', error));
    }

    // Delete a category
    window.deleteCategory = function(categoryId) {
        fetch(`${apiUrl}${categoryId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchCategories())
        .catch(error => console.error('Error deleting category:', error));
    }

    // Initial fetch of categories
    fetchCategories();
});
