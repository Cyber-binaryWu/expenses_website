const today = new Date().toLocaleDateString('en-CA');
const dateInput = document.getElementById("expense_date");
if (dateInput) {
    dateInput.value = today;
}


const modal = document.getElementById("modal");
const cancelButton = document.getElementById("update_cancel_button");
const submitBtn = document.getElementById("submitBtn"); 


const editButtons = document.querySelectorAll(".edit_button");


editButtons.forEach(button => {
    button.addEventListener("click", () => {
        modal.style.display = "flex";
    });
});


cancelButton.addEventListener("click", () => {
    modal.style.display = "none";
});


modal.addEventListener("click", (event) => {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});
