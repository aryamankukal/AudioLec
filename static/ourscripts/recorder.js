jQuery(document).ready(function () {
    var $ = jQuery;
    var myRecorder = {
        objects: {
            context: null,
            stream: null,
            recorder: null
        },
        init: function () {
            if (null === myRecorder.objects.context) {
                myRecorder.objects.context = new (
                    window.AudioContext || window.webkitAudioContext
                );
            }
        },
        start: function () {
            var options = { audio: true, video: false };
            navigator.mediaDevices.getUserMedia(options).then(function (stream) {
                myRecorder.objects.stream = stream;
                myRecorder.objects.recorder = new Recorder(
                    myRecorder.objects.context.createMediaStreamSource(stream),
                    { numChannels: 1 }
                );
                myRecorder.objects.recorder.record();
            }).catch(function (err) { });
        },
        stop: function (listObject) {
            if (null !== myRecorder.objects.stream) {
                myRecorder.objects.stream.getAudioTracks()[0].stop();
            }
            if (null !== myRecorder.objects.recorder) {
                myRecorder.objects.recorder.stop();

                // Validate object
                if (null !== listObject
                    && 'object' === typeof listObject
                    && listObject.length > 0) {
                    // Export the WAV file
                    myRecorder.objects.recorder.exportWAV(function (blob) {
                        var url = (window.URL || window.webkitURL)
                            .createObjectURL(blob);

                        // Prepare the playback
                        var audioObject = $('<audio controls></audio>')
                            .attr('src', url);

                        // Prepare the download link
                        var downloadObject = $('')
                            .attr('href', url)
                            .attr('download', new Date().toUTCString() + '.wav');

                        // Wrap everything in a row
                        var holderObject = $('<div class="row" style="margin: 0px;"></div>')
                            .append(audioObject);
                            // .append(downloadObject);

                        // Append to the list
                        listObject.append(holderObject);
                    });
                }
            }
        }
    };

    // Prepare the list
    var listObject = $('[data-role="recordings"]');

    // Prepare the record button
    $('[data-role="controls"] > button').click(function () {
        // Initialize the recorder
        myRecorder.init();

        // Get the button state
        var buttonState = !!$(this).attr('data-recording');

        // Toggle
        if (!buttonState) {
            $(this).attr('data-recording', 'true');
            myRecorder.start();
        } else {
            $(this).attr('data-recording', '');
            myRecorder.stop(listObject);
        }
    });
});