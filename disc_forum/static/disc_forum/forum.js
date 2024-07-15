// disc_forum/static/disc_forum/forum.js

$(document).ready(function() {
    // Initialize counter for attachment inputs
    var attachmentCount = 1;

    // Function to add more attachment inputs
    $('#add-more-attachments').click(function(e) {
        e.preventDefault();
        attachmentCount++;
        var newInput = '<div><label for="id_attachment_' + attachmentCount + '">Attachment ' + attachmentCount + ':</label><input type="file" name="attachment_' + attachmentCount + '" id="id_attachment_' + attachmentCount + '"></div>';
        $('#attachment-container').append(newInput);
    });

    // Function to clear form fields and reset attachment inputs
    function clearForm() {
        $('form')[0].reset(); // Reset the form
        $('#attachment-container').html('<div><label for="id_attachment">Attachment 1:</label><input type="file" name="attachment" id="id_attachment"></div>');
        attachmentCount = 1; // Reset the attachment counter
    }

    // Clear form fields after form submission
    $('form').on('submit', function() {
        setTimeout(clearForm, 1000); // Delay the form reset to ensure the form is submitted before clearing
    });
});
