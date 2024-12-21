document.addEventListener("DOMContentLoaded", function () {
    const designTypeSelect = document.getElementById("design-type");
    const designItems = document.querySelectorAll(".design-item");

    designTypeSelect.addEventListener("change", function () {
        const selectedCategory = this.value;
        designItems.forEach(function (item) {
            const itemCategory = item.dataset.category;
            if (selectedCategory === "all" || selectedCategory === itemCategory) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
    });

    // Smooth scrolling functionality for the design grid
    const designGrid = document.querySelector(".design-grid");
    designGrid.addEventListener("wheel", function (e) {
        e.preventDefault();
        designGrid.scrollLeft += e.deltaY;
    });
});


document.addEventListener("DOMContentLoaded", () => {
    // Select all design images
    const designImages = document.querySelectorAll(".design-image");
    const detailsContainer = document.getElementById("image-details");
    const descriptionElem = document.getElementById("description");
    const magazineTypeElem = document.getElementById("magazine-type");

    designImages.forEach(image => {
        image.addEventListener("click", () => {
            // Remove zoom from any previously zoomed image
            document.querySelectorAll(".design-image.zoomed").forEach(img => {
                img.classList.remove("zoomed");
            });

            // Add zoom effect to the clicked image
            image.classList.add("zoomed");

            // Fetch data attributes for description and magazine type
            const description = image.getAttribute("data-description");
            const magazineType = image.getAttribute("data-magazine-type");

            // Update the details container
            descriptionElem.textContent = `Description: ${description}`;
            magazineTypeElem.textContent = `Magazine Type: ${magazineType}`;

            // Show the details container
            detailsContainer.classList.remove("hidden");
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const designImages = document.querySelectorAll(".design-image");

    designImages.forEach(image => {
        image.addEventListener("click", () => {
            // Reset previously zoomed images and hide details
            document.querySelectorAll(".zoomed").forEach(zoomedImage => zoomedImage.classList.remove("zoomed"));
            document.querySelectorAll(".design-right").forEach(details => details.classList.add("hidden"));

            // Zoom the clicked image
            image.classList.add("zoomed");

            // Update details on the right
            const parent = image.closest(".design-item");
            const details = parent.querySelector(".design-right");
            const description = image.getAttribute("data-description");
            const magazineType = image.getAttribute("data-magazine-type");

            details.querySelector("#description").textContent = `Description: ${description}`;
            details.querySelector("#magazine-type").textContent = `Magazine Type: ${magazineType}`;
            details.classList.remove("hidden");
        });
    });
});
