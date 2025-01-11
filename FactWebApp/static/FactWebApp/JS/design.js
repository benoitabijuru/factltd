
document.addEventListener("DOMContentLoaded", () => {
    const filterDropdown = document.getElementById("design-type"); // Dropdown for filtering
    const designItems = document.querySelectorAll(".design-item"); // All design items

    // Function to filter designs based on the selected category
    filterDropdown.addEventListener("change", () => {
        const selectedCategory = filterDropdown.value.toLowerCase(); // Get the selected value

        // Loop through all design items and filter based on category
        designItems.forEach(item => {
            const itemCategory = item.dataset.category.toLowerCase(); // Subcategory of the item

            if (selectedCategory === "all" || itemCategory === selectedCategory) {
                item.classList.remove("hidden"); // Show the item
                item.style.opacity = 1; // Ensure visible items have full opacity
            } else {
                item.classList.add("hidden"); // Hide the item
                item.style.opacity = 0; // Ensure hidden items have no opacity
            }
        });

        // Reset zoom and details when the filter changes
        resetZoomAndDetails();
    });

    // Function to handle zoom-in and detail-view on clicking an image
    document.querySelector(".design-grid").addEventListener("click", event => {
        if (event.target.classList.contains("design-image")) {
            // Reset previous zoom and details
            resetZoomAndDetails();

            // Zoom the clicked image
            const clickedImage = event.target;
            clickedImage.classList.add("zoomed");

            // Show details on the right
            const parentItem = clickedImage.closest(".design-item");
            const detailsSection = parentItem.querySelector(".design-right");
            if (detailsSection) {
                detailsSection.classList.remove("hidden");
            }
        }
    });

    // Function to handle click for returning to original size
    document.querySelector(".design-grid").addEventListener("dblclick", event => {
        if (event.target.classList.contains("design-image") && event.target.classList.contains("zoomed")) {
            // If image is zoomed, remove the zoom
            event.target.classList.remove("zoomed");

            // Optionally, hide the details as well
            const parentItem = event.target.closest(".design-item");
            const detailsSection = parentItem.querySelector(".design-right");
            if (detailsSection) {
                detailsSection.classList.add("hidden");
            }
        }
    });

    // Helper function to reset zoomed images and hide all details
    function resetZoomAndDetails() {
        document.querySelectorAll(".zoomed").forEach(zoomedImage => zoomedImage.classList.remove("zoomed"));
        document.querySelectorAll(".design-right").forEach(details => details.classList.add("hidden"));
    }
});

