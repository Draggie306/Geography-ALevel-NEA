document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const output = document.querySelector('#output');


    // displays elapsed time in seconds, recursively calls itself every 100ms
    function loadingTextTime(elapsed, is_end) {
        const text_loading = document.getElementById("loading_text");
        if (is_end) {
            text_loading.innerHTML = `Finished in ${elapsed} seconds`;
        } else {
            text_loading.innerHTML = `Waiting for server to generate image... ${elapsed} seconds elapsed`;
            setTimeout(() => {
                loadingTextTime(elapsed + 0.1, false);
            }, 100);
        }

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const dataText = form.elements['data_text'].value;
        const width = form.elements['width'].value;
        const height = form.elements['height'].value;
        const maxFontSize = form.elements['max_font_size'].value;
        output.innerHTML = "Loading response...";
        // start loading text timer
        loadingTextTime(0, false);

        try {
            const response = await fetch('https://geog-nea-wordcloud.draggie.repl.co/generate_word_cloud', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ data_text: dataText, width: width, height: height, max_font_size: maxFontSize })
            });

            if (response.ok) {
                const result = await response.json();
                // stop loading text timer
                loadingTextTime(0, true);
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
            } else {
                // get json "message" field if it exists, otherwise use the status text
                const result = await response.json();
                output.innerHTML = `Error generating word cloud, server says: ${result.message || response.statusText}`;
            }
        } catch (error) {
            console.error('Error:', error);
            // get json "message" field if it exists, otherwise use the status text
            output.innerHTML = `Error generating word cloud! ${error.message || error}`;
        }
    });
}});
