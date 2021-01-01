function startRecording() {
    button = document.getElementById('recordingButton')
    var sound;
    if(button.classList.contains('Rec')) {
        console.log("hint");
        sound = new Audio('/sounds/hint.wav');
        sound.play()
    } else {
        console.log('start');
        sound = new Audio('/sounds/start.wav');
        sound.play()
    }
    button.classList.toggle("Rec")
}
