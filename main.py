import csv
import re
import time
import datetime
import uuid
import random
import flask
import traceback
from collections import Counter

from flask_cors import CORS, cross_origin

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from flask import Flask, request, jsonify, render_template

data = []

repl_save = True

# Change below depending on what you need (resolution of wordcloud)
# For an 8K monitor this is "width=7680, height=4320"
# Default: 1920, 1080
#width = int(input("Enter width: (recommended: 1920)\n>>> "))
#height = int(input("Enter height: (recommended: 1080)\n>>> "))

from flask import Flask, request, jsonify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/generate_word_cloud', methods=['POST'])
@cross_origin()
def generate_word_cloud():
    try:
        width = 1920
        height = 1080
    
        print(request.json)
        words = request.json.get('data_text')
        width = request.json.get('width')
        height = request.json.get('height')
        max_font_size = request.json.get('max_font_size')
    
        # Change depending on width/height
        # For 1080p a good size is around 140
        #max_font_size = 300#int(input("Enter max font size: (recommended: 30% of height, 300 for default)\n>>> "))
    
        data_text = ' '.join(words)
        
        words = re.findall(r'\b\w+\b', data_text.lower())  # Regex to find all words in the text data
        amount_of_words = len(words)
        print(f"\nThere are {amount_of_words} words in the text.")
        
        word_counts = Counter(words)
        print("Most common words:")
        
        for word, count in word_counts.most_common():
            print(f"{word}: {count}")
        
        print(f"\nAmount of words: {amount_of_words}")
        
        # now generate word cloud - https://www.datacamp.com/tutorial/wordcloud-python
        text = data_text
        
        print(f"\nGenerating word cloud with resolution {width}x{height}. Max wordsize = {max_font_size}")
        wordcloud = WordCloud(
            max_font_size=max_font_size,  # more common words should be the biggest
            # min_font_size=50,   # less common words should be the smallest
            background_color="grey",
            width=width,  # 8k monitor
            height=height,  # 8k monitor
            max_words=1000,     # we want to see all words
            collocations=True,
            collocation_threshold=80,
            normalize_plurals=True,    # removes plurals - better for word cloud
            prefer_horizontal=0.85,  # 80% chance of horizontal, which is easier to read
            #color_func=lambda *args, **kwargs: "hsl(330, 100%%, %d%%)" % random.randint(50, 80)
            ).generate(text)
        
        plt.figure(dpi=200)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        
        # uuid_to_use = uuid.uuid4()
        # TODO: Change from uuid to time + DateTime
        uuid_to_use = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        
        
        if not repl_save:
            print("saving to local directory as {}".format(uuid_to_use))
            wordcloud.to_file(f"D:\\OneDrive - Notre Dame High School\\[nea] Geo\\word cloud\\python_wordcloud_{uuid_to_use}.png")
        else:
            print(f'Saving on filesystem in generations folder as "{uuid_to_use}"')
            wordcloud.to_file(f"generations/python_wordcloud_{uuid_to_use}.png")

        return jsonify({
            "wordcloud": wordcloud
        }), 200
    except Exception as e:
        return jsonify({
                "error": True,
                "message": f"Error generating response: {e}\n\n{traceback.format_exc()}"
            }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=random.randint(2000,9000))