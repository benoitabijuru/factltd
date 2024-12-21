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
});



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
