$(document).ready(function() {
    // Hide the attachment container initially
    $('#attachment-container').hide();

    // Show attachment container and hide the Add More button when clicked
    $('#add-more-attachments').click(function(e) {
        e.preventDefault();
        $('#attachment-container').show();
        $(this).hide();
    });

    // Function to clear form fields and reset attachment inputs
    function clearForm() {
        $('form')[0].reset(); // Reset the form
        $('#attachment-container').hide(); // Hide the attachment container
        $('#add-more-attachments').show(); // Show the Add More button
    }

    // Clear form fields after form submission
    $('form').on('submit', function() {
        setTimeout(clearForm, 1000); // Delay the form reset to ensure the form is submitted before clearing
    });
});
