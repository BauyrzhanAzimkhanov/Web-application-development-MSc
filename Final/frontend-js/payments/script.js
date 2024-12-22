document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = 'http://localhost:8000/payments/';  // Update with your Django API URL

    // Fetch payments from the API
    function fetchPayments() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const paymentContainer = document.getElementById('payments');
                paymentContainer.innerHTML = '';
                data.forEach(payment => {
                    const paymentDiv = document.createElement('div');
                    paymentDiv.className = 'payment';
                    paymentDiv.innerHTML = `
                        <h2>${payment.user.username}</h2>
                        <p>Amount: ${payment.amount}</p>
                        <p>Status: ${payment.status}</p>
                        <button onclick="deletePayment(${payment.id})">Delete</button>
                    `;
                    paymentContainer.appendChild(paymentDiv);
                });
            })
            .catch(error => console.error('Error fetching payments:', error));
    }

    // Delete a payment
    window.deletePayment = function(paymentId) {
        fetch(`${apiUrl}${paymentId}/`, {
            method: 'DELETE',
        })
        .then(() => fetchPayments())
        .catch(error => console.error('Error deleting payment:', error));
    }

    // Initial fetch of payments
    fetchPayments();
});
