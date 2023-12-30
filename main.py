import re
import datetime
import io
import random
import traceback
import base64
import colorsys
from collections import Counter

from flask_cors import CORS, cross_origin

from wordcloud import WordCloud
from flask import Flask, request, jsonify

data = []

repl_save = True

print("Initialising word cloud generator")

# Change below depending on what you need (resolution of wordcloud)
# For an 8K monitor this is "width=7680, height=4320"
# Default: 1920, 1080
#width = int(input("Enter width: (recommended: 1920)\n>>> "))
#height = int(input("Enter height: (recommended: 1080)\n>>> "))

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/ping')
def pong():
    return 'Pong!'


@app.route('/generate_word_cloud', methods=['POST'])
@cross_origin()
def generate_word_cloud():
    try:
        width = 1920
        height = 1080

        print(request.json)
        try:
            width = int(request.json.get('width'))
            height = int(request.json.get('height'))
            max_font_size = int(request.json.get('max_font_size'))
            rgb_red = int(request.json.get('r'))
            rgb_green = int(request.json.get('g'))
            rgb_blue = int(request.json.get('b'))
            colour_variation = int(request.json.get('variation'))
        except Exception:
            return jsonify({
                "error": True,
                "message": "Invalid literal value type, please use numbers"
            }), 403

        pixels = width * height

        if pixels > 20000000:
            return jsonify({
                "error": True,
                "message": "Width and height must be less, currently too big!"
                }), 403

        data = request.json
        words = re.findall(r'\b\w+\b', data.get('data_text', '').lower())

        word_counts = Counter(words)
        print(f"\nThere are {len(words)} words in the text.")
        print("\nMost common words:")
        for word, count in word_counts.most_common():
            print(f"{word}: {count}")

        text = ' '.join(words)

        def color_func(r, g, b, variation):
            # Convert RGB values to a scale of 0 to 1
            r /= 255.0
            g /= 255.0
            b /= 255.0

            # Convert RGB to HLS
            h, l, s = colorsys.rgb_to_hls(r, g, b)

            # Generate a random variation within the specified range
            variation /= 200.0  # Convert percentage to decimal
            hue_variation = random.uniform(-variation, variation)

            # Adjust hue value with hue_variation
            h = (h + hue_variation) % 1.0

            # Convert HLS back to RGB
            r, g, b = colorsys.hls_to_rgb(h, l, s)

            # Convert RGB values back to a scale of 0 to 255
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            return "rgb({}, {}, {})".format(r, g, b)

        print(f"\nGenerating word cloud with resolution {width}x{height}. Max wordsize = {max_font_size}")
        wordcloud = WordCloud(
            max_font_size=max_font_size,  # more common words should be the biggest
            # min_font_size=50,   # less common words should be the smallest
            background_color="white",
            width=width,  # 8k monitor
            height=height,  # 8k monitor
            max_words=1000,  # we want to see all words
            collocations=True,
            collocation_threshold=80,
            normalize_plurals=True,  # removes plurals - better for word cloud
            prefer_horizontal= 0.85,  # 80% chance of horizontal, which is easier to read
            color_func=lambda *args, **kwargs: color_func(rgb_red, rgb_green, rgb_blue, colour_variation)
        ).generate(text)
        """plt.figure(dpi=200)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")"""

        # uuid_to_use = uuid.uuid4()
        # TODO: Change from uuid to time + DateTime
        """
    
        # Old code
        
        uuid_to_use = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        if not repl_save:
            print("saving to local directory as {}".format(uuid_to_use))
            wordcloud.to_file(f"D:\\OneDrive - Notre Dame High School\\[nea] Geo\\word cloud\\python_wordcloud_{uuid_to_use}.png")
        else:
            print(f'Saving on filesystem in generations folder as "{uuid_to_use}"')
            wordcloud.to_file(f"generations/python_wordcloud_{uuid_to_use}.png")

        # base64wordcloud = base64.b64encode(open(f"generations/python_wordcloud_{uuid_to_use}.png",'rb').read())
        # base64wordcloud = base64wordcloud.decode('utf-8')
        """

        img_io = io.BytesIO()
        wordcloud.to_image().save(img_io, 'PNG')
        img_io.seek(0)
        base64wordcloud = base64.b64encode(img_io.read()).decode('utf-8')

        print(f"Word cloud generated successfully at time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return jsonify({
            "error": False,
            "message": "Successfully generated word cloud",
            "wordcloud": base64wordcloud
        }), 200
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return jsonify({
            "error": True,
            "message": f"Error generating response: {e}\n\n{traceback.format_exc()}"
        }), 500


@app.route('/.git')
def go_away():
    return 'token="GO_AWAY_SCREW_YOURSELF"'


if __name__ == '__main__':
    print("Starting server")
    try:
        app.run(host='0.0.0.0', port=49763)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        input("Press enter to exit")
