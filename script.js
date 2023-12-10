const backend_api = "https://wordcloud-backend.ibaguette.com"

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const output = document.querySelector('#output');
    const loadingText = document.getElementById('loading_text');
    let shouldStop = false;

    try {
        console.log("Attempting to wake up server")
        fetch(`${backend_api}/ping`, {
            method: 'GET',
        });
        console.log("Server seems to be awake")
    } catch (error) {
        console.error("Ping error:", error);
    }

    // displays elapsed time in seconds, recursively calls itself every 100ms
    function loadingTextTime(elapsed) {
        // elapsed = elapsed.toFixed(2);
        if (shouldStop) {
            console.log(`Finished in ${elapsed.toFixed(1)} seconds!`);
            loadingText.innerHTML = `Finished in ${elapsed.toFixed(1)} seconds!`;
        } else {
            console.log(`Waiting for server to generate image... ${elapsed.toFixed(1)} seconds elapsed`);
            loadingText.innerHTML = `Waiting for server to generate image... ${elapsed.toFixed(1)} seconds elapsed`;
            setTimeout(() => {
                loadingTextTime(elapsed + 0.1);
            }, 100);
        }
    }

    var colorPickerContainer = document.getElementById("colorPickerContainer");
    var colorPickerVariationContainer = document.getElementById("colorPickerVariationContainer");

    // Create a color picker and a number input for the randomness variation
    var colorPicker = document.createElement("input");
    colorPicker.type = "color";
    colorPicker.value = "#00acff";
    colorPicker.id = "colorPicker";

    colorPickerContainer.appendChild(colorPicker);

    var variationInput = document.createElement("input");
    variationInput.type = "number";
    variationInput.min = "0";
    variationInput.max = "255";
    variationInput.value = "10";
    variationInput.id = "variationInput";

    colorPickerVariationContainer.appendChild(variationInput);


    // Function to convert a hex color to RGB
    function hexToRgb(hex) {
        var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    }

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        shouldStop = false;

        const dataText = form.elements['data_text'].value;
        const width = form.elements['width'].value;
        const height = form.elements['height'].value;
        const maxFontSize = form.elements['max_font_size'].value;
        const color = document.getElementById("colorPicker").value;
        const variation = document.getElementById("variationInput").value;
        // Convert the color to RGB
        var rgb = hexToRgb(color);

        output.innerHTML = "Loading response...";
        // start loading text timer
        loadingTextTime(0);

        try {
            const response = await fetch(`${backend_api}/generate_word_cloud`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    data_text: dataText,
                    width: width,
                    height: height,
                    max_font_size: maxFontSize,
                    r: rgb.r, 
                    g: rgb.g, 
                    b: rgb.b, 
                    variation: variation 
                })
            });

            if (response.ok) {
                const result = await response.json();
                // stop loading text timer
                shouldStop = true;
                // get wordcloud base64 image from json response "wordcloud" field
                wordcloud_result = result.wordcloud;
                let base64Image = wordcloud_result.split(';base64,').pop();
                // create image element with base64 image
                let image = document.createElement('img');
                image.src = `data:image/png;base64,${base64Image}`;
                // add image to output
                output.innerHTML = "";
                // scale image to fit screen
                // output.appendChild(image);
                output.innerHTML = `<img src="data:image/png;base64,${base64Image}" style="max-width: 70%; max-height: 70%;">`;
                
                var bonusButtons = document.getElementById("bonusButtons"); // Download and Copy buttons
                bonusButtons.innerHTML = ""; // Clear the buttons
                // Create a download button
                var downloadButton = document.createElement("button");
                downloadButton.innerHTML = "Save";
                var currentUnixTime = Math.round((new Date()).getTime() / 1000);

                downloadButton.id = "downloadButton";
                downloadButton.onclick = function() {
                    var a = document.createElement("a");
                    a.href = `data:image/png;base64,${base64Image}`;
                    a.download = `wordcloud_${currentUnixTime}.png`;
                    a.click();
                };
                bonusButtons.appendChild(downloadButton);

                // Create a copy button
                var copyButton = document.createElement("button");
                copyButton.innerHTML = "Copy";
                copyButton.id = "copyButton";
                copyButton.onclick = function() {
                    // Convert base64 to raw binary data held in a string
                    var byteString = atob(base64Image);
                
                    // Write the bytes of the string to an ArrayBuffer
                    var ab = new ArrayBuffer(byteString.length);
                    var ia = new Uint8Array(ab);
                    for (var i = 0; i < byteString.length; i++) {
                        ia[i] = byteString.charCodeAt(i);
                    }
                
                    // Create a blob from the ArrayBuffer
                    var blob = new Blob([ab], {type: 'image/png'});
                
                    // Use the Clipboard API to copy the blob
                    navigator.clipboard.write([
                        new ClipboardItem({
                            'image/png': blob
                        })
                    ]).then(function() {
                        window.alert("Your word cloud has been copied to your clipboard! Have a nice day!");
                    }, function(err) {
                        console.error('Could not copy text! Please copy manually and report this as an issue on GitHub (the bottom of the page).', err);
                    });
                };
                bonusButtons.appendChild(copyButton);


            } else {
                shouldStop = true;
                // get json "message" field if it exists, otherwise use the status text
                const result = await response.json();
                output.innerHTML = `Error generating word cloud, server says: ${result.message || response.statusText}`;
            }
        } catch (error) {
            shouldStop = true;
            console.error('Error:', error);
            // get json "message" field if it exists, otherwise use the status text
            output.innerHTML = `Error generating word cloud! ${error.message || error}`;
        }
    });
});
