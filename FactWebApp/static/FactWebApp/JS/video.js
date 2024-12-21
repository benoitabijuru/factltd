document.addEventListener("DOMContentLoaded", () => {
    const videoItems = document.querySelectorAll(".video-item video");

    videoItems.forEach((video) => {
        // Behavior 1: Play video in fullscreen when played
        video.addEventListener("play", () => {
            // Pause all other videos
            videoItems.forEach((otherVideo) => {
                if (otherVideo !== video) {
                    otherVideo.pause();
                    otherVideo.muted = true; // Mute other videos
                }
            });

            // Request fullscreen for the current video
            if (video.requestFullscreen) {
                video.requestFullscreen();
            } else if (video.webkitRequestFullscreen) { // For Safari
                video.webkitRequestFullscreen();
            } else if (video.msRequestFullscreen) { // For IE/Edge
                video.msRequestFullscreen();
            }
        });

        // Behavior 2: Play muted when hovered, with fixed size
        video.addEventListener("mouseenter", () => {
            if (video.paused) {
                video.muted = true; // Ensure it's muted
                video.play();
            }
        });

        // Stop playback when hover ends
        video.addEventListener("mouseleave", () => {
            if (!video.paused) {
                video.pause();
                video.currentTime = 0; // Reset video to the start
            }
        });

        // Reset size and behavior when video ends
        video.addEventListener("ended", () => {
            video.muted = false;
        });
    });
});
