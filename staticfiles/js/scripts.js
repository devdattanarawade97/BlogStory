/* static/js/script.js */
document.addEventListener('DOMContentLoaded', function() {
    // Display Toast notification for actions like logging in, liking, etc.
    if (document.querySelector('.toast')) {
        setTimeout(function() {
            let toast = new bootstrap.Toast(document.querySelector('.toast'));
            toast.show();
        }, 500);
    }
});
