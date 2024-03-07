document.addEventListener("DOMContentLoaded", function() {
    const ratings = document.querySelectorAll(".rating");

    ratings.forEach((rating) => {
        const stars = rating.querySelectorAll("i");

        stars.forEach((star, index) => {
            star.addEventListener("click", () => {
                resetStars(stars);
                setRating(stars, index);
            });
        });
    });

    function resetStars(stars) {
        stars.forEach((star) => {
            star.classList.remove("active");
        });
    }

    function setRating(stars, index) {
        for (let i = 0; i <= index; i++) {
            stars[i].classList.add("active");
        }
    }
});
