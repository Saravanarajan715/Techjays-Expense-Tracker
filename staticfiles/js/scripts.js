
function confirmDelete() {
    return confirm("Are you sure you want to delete this expense?");
}


function validateExpenseForm() {
    const description = document.querySelector('input[name="description"]').value.trim();
    const amount = document.querySelector('input[name="amount"]').value.trim();
    const date = document.querySelector('input[name="date"]').value;
    const category = document.querySelector('select[name="category"]').value;

    if (!description || !amount || !date || !category) {
        alert("All fields are required!");
        return false;
    }

    if (isNaN(amount) || parseFloat(amount) <= 0) {
        alert("Please enter a valid amount greater than zero.");
        return false;
    }

    return true;
}


document.addEventListener('DOMContentLoaded', () => {
    const expenseForm = document.querySelector('form');
    if (expenseForm) {
        expenseForm.onsubmit = validateExpenseForm;
    }

    
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        button.onclick = confirmDelete;
    });
});
