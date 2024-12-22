document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/reviews/';  // Update with your Django API URL

    // Fetch reviews from the API
    function fetchReviews() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const reviewContainer = document.getElementById('reviews');
                reviewContainer.innerHTML = '';
                data.forEach(review => {
                    const reviewDiv = document.createElement('div');
                    reviewDiv.className = 'review';
                    reviewDiv.innerHTML = `
                        <h2>${review.course.title}</h2>
                        <p>By: ${review.user.username}</p>
                        <p>Rating: ${review.rating}</p>
                        <p>${review.comment}</p>
                        <button onclick="deleteReview(${review.id})">Delete</button>
                    `;
                    reviewContainer.appendChild(reviewDiv);
                });
            })
            .catch(error => console.error('Error fetching reviews:', error));
    }

    // Delete a review
    window.deleteReview = function(reviewId) {
        fetch(`${apiUrl}${reviewId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchReviews())
        .catch(error => console.error('Error deleting review:', error));
    }

    // Initial fetch of reviews
    fetchReviews();
});
