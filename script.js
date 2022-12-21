document.addEventListener("DOMContentLoaded", () => {
    // Declare variables
    let time = 1500; // Time in seconds
    let running = false;
    let intervalId;
  
    // Select elements
    const timeDisplay = document.querySelector("#time-display");
    const startStopButton = document.querySelector("#start-stop-button");
    const resetButton = document.querySelector("#reset-button");
  
    // Update time display
    function updateTimeDisplay() {
      let minutes = Math.floor(time / 60);
      let seconds = time % 60;
      timeDisplay.textContent = `${minutes}:${seconds.toString().padStart(2, "0")}`;
    }
  
    // Start timer
    function startTimer() {
      intervalId = setInterval(() => {
        time--;
        updateTimeDisplay();
        if (time === 0) {
          resetTimer();
        }
      }, 1000);
    }
  
    // Stop timer
    function stopTimer() {
      clearInterval(intervalId);
    }
  
    // Reset timer
    function resetTimer() {
      time = 1500;
      updateTimeDisplay();
      stopTimer();
    }
  
    // Toggle timer on/off
    startStopButton.addEventListener("click", () => {
      if (running) {
        stopTimer();
        startStopButton.textContent = "Start";
      } else {
        startTimer();
        startStopButton.textContent = "Stop";
      }
      running = !running;
    });
  
    // Reset timer
    resetButton.addEventListener("click", resetTimer);
  });