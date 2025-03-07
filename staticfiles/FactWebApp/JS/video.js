document.addEventListener("DOMContentLoaded", () => {
    const videoItems = document.querySelectorAll(".video-item video");

    videoItems.forEach((video) => {
        // Behavior 1: Play video and unmute sound when played
        video.addEventListener("play", () => {
            // Pause all other videos
            videoItems.forEach((otherVideo) => {
                if (otherVideo !== video) {
                    otherVideo.pause();
                    otherVideo.muted = true; // Mute other videos
                }
            });

            // Unmute the current video
            video.muted = false;

            // Optional: Request fullscreen for the current video
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
                video.muted = true; // Ensure it's muted when hovered
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

        // Behavior 3: Allow video to continue playing after exiting fullscreen
        document.addEventListener("fullscreenchange", () => {
            if (!document.fullscreenElement) {
                // Optional: Adjust video size to "miniplayer" mode when exiting fullscreen
                video.style.width = "320px";  // Miniplayer width
                video.style.height = "180px"; // Miniplayer height
            }
        });

        // Behavior 4: Reset muted property when the video ends
        video.addEventListener("ended", () => {
            video.muted = false; // Ensure the video is unmuted for the next playback
        });
    });
});
