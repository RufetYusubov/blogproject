document.addEventListener("DOMContentLoaded", function() {
    const toggleButtons = document.querySelectorAll(".blog-posts .content .toggle-reply");
    toggleButtons.forEach(function(button) {
      button.addEventListener("click", function() {
        const reply = this.nextElementSibling;
        if (reply.style.display === "none" || reply.style.display === "") {
          reply.style.display = "block";
          this.textContent = "Hide Reply";
        } else {
          reply.style.display = "none";
          this.textContent = "Show Reply";
        }
      });
    });
  });