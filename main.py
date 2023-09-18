import csv
import re
import time
import uuid
from collections import Counter

import matplotlib.pyplot as plt
from wordcloud import WordCloud

data = []

repl_save = True

def words_fromcsv():
    """
    Retrieve the words from the CSV generated by Google Forms\n
    Only run this locally due to the hardcoded directory!
    """
    csv_file_path = r"D:\OneDrive - Notre Dame High School\[nea] Geo\NEA - Anglia Square on-ground questionnaire results.csv"

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) >= 11:
                data.append(row[9])  # column J - question 10
                data.append(row[10])  # column K - question 11
        i = 0
        while i < 2:  # clean up first row on the two columns as
            data.remove(data[0])  # this is the question not results
            i += 1

    data2 = []
    for item in data:
        if item != "":
            data2.append(item.lower())
    return data2


def words_fromstring():
    """
    Generates a wordcloud from anything within the string.
    """
    
    new_data = """
        eyesore, derelict, useless	destination, fun, shopping
        Lifeless, baron, forgotten	Empty, boring, lifeless
        Barren, neglected, empty	Neglected, unloved, potential
        Outdated, Brutalist, Grey	Outdated, dirty, dark
        Empty, Rundown, Concrete	Empty, Rundown, Concrete
        Depressing, dirty, old	Quirky, community, old
        concrete, sad, historical	quiet, low income, unmaintained
        Antiquated, incitement, poverty	Treacherous, hazardous, dirty
        derelict, lifeless, rundown	derelict, lifeless, rundown
        Out-dated, curious, brutalism	Nervous, ugly, interesting
        Ugly, neglected, outdated	N/A,N/A,N/a
        Tired, pointless,empty	Empty,dirty,old
        Neglected, Brutalist, Potential 	poverty, depression, sad
        shabby, dated, nostalgic	shabby, dated, dangerous
        Old, tired, rundown	Old, tired, rundown
        ugly, purposeless, empty	ugly, purposeless, creepy
        Grey, concrete, quiet	Interesting, quiet, grey
        dreary, underused, run-down	plain, okay, normal
        Dangerous, dirty, dull	Dull, solitary, graffiti 
        decrepit, old, unattractive	worn, derelict, busy
        Concrete, grey, dull	Dull, unimaginative, boring
        derelict, ugly, depressing	disappointing, dirty, potential
        Gulag, Battle Royale, Hell	I, got, robbed
        rundown, sad, poor	rundown, poor, sad
        Dull, lifeless, cheap	Deprived, interesting, uneventful 
        grey, affordable, boring 	busy, concrete, boring
        concrete, open, useful 	Crowded, small, compact 
        Deprived, cramped, underinvested 	Dense, deprived, busy
        destitute, boring, rough	destitute, boring, rough
        Boring, mundane , dull	Prosperous,packed,intersting
        standard, uninviting, concrete	interesting, busy, useful
        Drab, Miserable, Derelict.	Variety, vibrant, essential
        Desolate,wasteland,run-down	Intimidating,dirty,overcrowded 
        Tepid, dilapidated, forlorn	Tepid, dilapidated, forlorn
        Dingy, bleak, ugly	Dirty, grey, bleak 
        Tatty, shops, poverty 	Tatty, shops, poverty 
        ugly, run down, concrete	ugly, concrete, shabby
        Eye sore, derelict, out dated	Eye sore, derelict, old
        Significant, brutalist, neglected 	Significant, brutalist, neglected 
        Brutal, useful, tired	Useful, local, varied
        Grey, rundown, eyesore	Derelict, rundown, outdated
        Dated, dirty, dangerous	Varied, colourful, useful
        Drab, dull, anti-social	Eyesore,spooky, dirty
        Intriguing, amusing, brutalist	Interesting, struggling, lacklustre
        stale, industrial, boring	 boring, concrete, lifeless
        Underdeveloped, accessible, cheap	Community, bustling, cheap
        Old, worn, urbanised	Old, worn, urbanised
        desolate, heritage, interesting 	desolate, heritage, interesting 
        quirky, alive, useful	useful, social, quirky
        Ugly, dated, uninviting	Ugly, dated, uninviting
        dodgy;,deprived, slum	boring, pale, dissatisfied 
        Derelict, ugly, abandoned	Derelict, ugly, abandoned
        eyesore, embarassing, old	eyesore, embarassing, old
        Ugly, unwelcoming, dirty	Ugly, bargains, surprising
        Bleak, unwelcoming, claustrophobic	Novel, characterdul, worrying
        Missing, Hollywood, cinema 	Fun, busy, entertaining 
        Adequate, run-down, dated	Adequate, run-down, dated
        Muddle, interesting, aimless	vibrant, workspace, decay
        Rundown, opportunity, waste 	Interesting, shopping, art 
        Brutalist, unwelcoming, dystopian.	Brutalist, unwelcoming, dystopian.
        Messy, eyesore, dangerous 	Messy, dangerous, eyesore
        Grey, rough, and dirty 	Grey, rough, and dirty 
        Bland, inaccessible, grey.	Mundane, soulless, lifeless. 
        Rundown, neglected, characterful	Fun, vibey, local
        Interesting, unique, tatty	Diverse, eclectic, accepting
        Ugly, functional, full	Ugly, functional, full
        Brutalist, decaying, unique	Odeon, skateboarding, shopping
        Dull, utilitarian, grey	Empty, crime, dull
        Zombie, apocalypse, hellscape	Zombie, apocalypse, hellscape
        Ugly, deprived, chavvy	Cheap, ugly, working class
        Dilapidated, dystopian, ugly 	Unsafe, poverty, lifeless
        Tired, old, run-down	Decline, Deprived, forgotten
        Underused, undervalued, Rundown	Unique, busy, affordable
        Depressed, vacant, grim	Social, mixed, alternative 
        Souless, dead, grey	Deteriorating, ethnic, interesting
        Dated, tired,rundown	Drab,sad,old people 
        Outdated, empty, landmark	Nostalgic, busy, dangerous
        Dilapidated, outdated, random	Forgotten, vandalised, threatening
        grey, uninspiring, unwelcoming	grey, uninspiring, unwelcoming
        Brutalist, grim, abandoned	Brutalist, grim, abandoned
        Old, crumbling, hub	Community, lifeblood, needed
        old, grey, dull	old, grey, dull
        Ugly, depressing, dystopian	Ugly, depressing, dystopian
        Community, tired, brutalist	Old, quiet, serving 
        Grey, disrepair, closed	Food, multicultural, interesting 
        scary, dangerous, unkempt	scary, dangerous, unkempt
        Eyesore, grotesque, soulless	Rough, grey, dull
        Concrete, Urban, Outdated	Busy, Outdated, Full
        Lifeless, grey, bland	Lifeless, grey, bland
        old, plain, dark	quiet, calm, helpful
        Eyesore, unsafe, embarrassment 	Uncomfortable, depressing, unwanted
        messy, disused, and looks sad	busy shopping center, old, small community
        Wasted, Crime, Poor	Wasted, Crime, Poor
        Drab,dull,sad	Sad, optimistic, unloved
        Dilapidated, community, worn 	Bustling, community, fun
        Ugly, underdeveloped, wasted	Ugly, underdeveloped, wasted
        Derelict, depressing, substandard	Useful, tolerable, exists
        Waste, potential, grey	Avoided, waste, useful
        Grotty, different, dated	Busy, run-down,  vibrant 
        Dull, empty, grey	Dull, empty, grey
        Concrete,ugly,derelict 	Concrete,threatening,ugly
         Crumbling, rough, affordable	Entertaining, useful, abandoned 
        Sad, misused, ugly	Cheap, dead, ugly
        Depleted, depressive, bleak	Tired, deprived, empty
        Affordable, cheap, concrete 	Affordable, comfortable, local 
        Functional, identifiable, large	Busy, functional, reachable 
        Shabby, grotty, quirky 	Dangerous, patchy, dirty
        gloomy, desolate, barren	gloomy, desolate, barren
        Saddening,waste,desolate 	Fun,focal-point,interesting 
        Drab, grey, concrete 	Diverse, local, run down
        Multicultural, brutalist, underutilised	Multicultural, brutalist, underutilised
        Ugly, grey, depressing	Hostile, scary, unwelcoming
        run-down, lifeless, derelict	empty, shady, grimy
        Ugly, seedy, downmarket 	Ugly, seedy, downmarket 
        Brutalist, drab, grey	Brutalist, drab, grey
        Creative, cheap, ugly	Creative, cheap, ugly
        Soviet, eighties, abandoned 	Community, service, interesting 
        Imposing, delapidated, abandoned	Deteriorating, closing, empty
        Old, cheap, broken	Old, cheap, broken
        Tatty, old, dated	Lively, busy, social
        Brutalist, sci-fi, ugly	Rough, old, dated
        Dilapidated, inefficient, artificial 	Dilapidated, inefficient, artificial 
        dirty, concrete, shops 	shops, concrete, dirty
        Grim, depressing, rotten	Unpleasant, unsafe, abandoned
        Dreary, dilapidated, eyesore	Melting pot, musical, fun
        Rough, Dangerous, Unneeded 	Rough, Dangerous, Unneeded
        Tired, uncared, dated	Fun, cheap, bargains 
        Grey, Soviet, Derelict 	Grey, Soviet, Derelict 
        Concrete, accessable, run-down	Necessary, accessable, useful 
        ugly, claustrophobic, oppressive	ugly, claustrophobic, oppressive
        Cheap, ignorable, tired	Unattractive, avoidable, ignored
        Dilapidated, worn,Weathered	Dilapidated, worn,Weathered
        Scary, distopian, eyesore	Entertaining, useful, familair
        Eyesore, Neglected, Impactful	Square, Building, Rhubarb
        grey, tired, legacy	reminiscent, local, bulwark
        Deprived, run-down, dirty	Busy, noisy, dirty
        Iconic, dishevelled, cold	Iconic, dishevelled, cold
        Derelict, grey, eyesore	Bustling, lively, chavvy
        depressing, dull, empty	depressing, dull, empty
        brutalist, grey, concrete	busy, oddly charming, run-down
        Ugly, messy, unkept	As, above, 
        Fascinating, useful, dated	Busy, useful, dated
        Outdated, ugly, crime	Poor, crime, sad
        Untidy, sad, quiet	Busy, noisy, colourful
        Miserable, disgusting, soulless	Miserable, disgusting, soulless 
        dull, drab, uninviting	dull, drab, uninviting
        Dilapidated,  poor, old	Poor, out-of-date, old-fashioned
        Eyesore, concrete, outdated	Cinema, exciting, fun
        Grey, unfriendly, down-at-heel	Grey, unfriendly, varied
        Dirty, useless, old	Uninteresting, bland, run-down
        grey, tired, neglected	bygone, diverse, inclusive
        Ugly, abandoned, dated	Useful, thriving, busy
        Ugly, concrete, lifeless	Boring, dirty, rough
        Cheap, cheerful, is what it is	Cheap, cheerful, 
        Shabby, vital, run down 	Vital, busy, multicultural 
        Neglected, unappealing, unsafe. 	Neglected, unappealing, unsafe
        Rundown, ugly, derelict	Rundown, ugly, derelict
        Dated, depressing, uninspiring	Dated, low-budget, sad
        tired, rundown, neglected	useful, friendly, bargains
        Sad, tires, dirty	Community, local, cheap
        Grey, sad, cold	Useful, handy, grey
        Rundown, dull, depressing 	Potential, quiet, good memories 
        essential, brutal, 1960s	declining, emptying, 
        Tired,dull,old	Busy, entertaining,alive
        Outdated, Tired, Seventies 	Scary, Embarrassing, Dirty
        Dated, decaying,  depressing	Dismal, sad, bleak
        Rough, old, not inviting	Interesting, dirty, messy
        Run down,desolate,sad	Variety,convenient,first
        Tried, ugly, unwelcoming 	Disappointing, sad, shame
        Concrete , dated , uninspiring 	Dull, boring, unsafe 
        Ugly, tired, depleted 	Ugly, tired, depleted 
        Community, charity shops, vegan frozen pastries from ernies	Familiar,affordable,fun
        Depressing, cold, lifeless	Exciting, busy, old
        Dated, ugly, busy	Colourful, quirky, frequented
        Dodgy, boring, lifeless	Packed, dodgy, lifeless
        Dated,poverty,dull	Dated,poverty,dull
        Neglected, unwelcoming, sad	Bustling, community, neglected
        Rundown, drab, lifeless.	Unappealing, depressing, rundown
        Crack-heads, cheap, nasty 	Run-down, awful, embarrassing 
        Outdated, tired, valuable	Sociable area, fun nightclubs, accessible 
        Worn-down, tired, brutalist	Grim, shady, worn-down
        Tired, lacking, vegetation	Charity, shops, bargains
        concrete-jungle, beruit, horrible	work, danger, bulldoze
        Underwhelming, forgotten, concrete	Busy, multicultural, underwhelming
        Unmaintained, depressing, unwelcoming	Busy, centric, transition
        Deserted, eerie, sad	Lonely, eerie, sad
        Industrial, real, brutalist 	Brutalist, packed, valuable 
        Rundown, drab, unsafe	Busy, friendly, convenient 
        Dilapidated, boring, run-down	Uninteresting, dingy, outdated
        Dull, dated, derelict 	Mundane, grey, dreary
        Sad, forgotten, decayed	Concrete, bustling, centre
        Abandoned, homelessness, old	Entertaining,lively, busy
        beautiful,exotic,luscious 	flamboyant,perpendicular,green
        Uninviting, bland, wasted space 	Convenient, bland, improvement
        Awful, Ugly, Dated	Impoverished, Grubby,lifeless
        Depressing, dirty, uninspiring	Depressing, dirty, uninspiring
        Misunderstood, brutal, local	Nostalgic, sad, grey
        Unwelcoming, depressing, ugly	Diverse, bustling, variety 
        Neglected, sad, unappreciated 	Useful, convenient, everyday
        Concrete, desolate, bare	Concrete, unsafe, abandoned
        Dilapidated, brutalist, eyesore 	Dilapidated, brutalist, eyesore
        Dilapidated, lifeless, boring	Community, independent, prosperous
        Obsolete, eyesore, defunct	Obsolete, eyesore, defunct
        Dull, Dated, Concreted.	Unattractive, Uninspiring,. Shabby.
        Eyesore, drab, concrete 	Chavvy, rundown, budget
        Embarrassing, Scummy,  Scary	Convenient, entertaining, eclectic 
        Old, functional, quirky	Busy, varied, multicultural 
    """
    # lower case all
    new_data = new_data.lower()

    new_data = new_data.split("\n")
    for item in new_data:
        if item != "":
            data.append(item)

    return data


data = words_fromstring()

data_text = ' '.join(data)

words = re.findall(r'\b\w+\b', data_text.lower())  # Regex to find all words in the text data
amount_of_words = len(words)


word_counts = Counter(words)

print("Most common words:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}")

print(f"\nAmount of words: {amount_of_words}")

# now generate word cloud - https://www.datacamp.com/tutorial/wordcloud-python
text = data_text

print("\nGenerating word cloud...")
wordcloud = WordCloud(
    max_font_size=1000,  # more common words should be the biggest
    # min_font_size=50,   # less common words should be the smallest
    background_color="white",
    width=7680,  # 8k monitor
    height=4320,  # 8k monitor
    max_words=1000,     # we want to see all words
    collocations=True,
    collocation_threshold=80,
    normalize_plurals=True,    # removes plurals - better for word cloud
    prefer_horizontal=0.85,  # 80% chance of horizontal, which is easier to read
    ).generate(text)

plt.figure(dpi=600)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

uuid_to_use = uuid.uuid4()

if not repl_save:
    print("saving to local directory as {}".format(uuid_to_use))
    wordcloud.to_file(f"D:\\OneDrive - Notre Dame High School\\[nea] Geo\\word cloud\\python_wordcloud_{uuid_to_use}.png")
else:
    print(f'Saving on Repl filesystem in generations folder as "{uuid_to_use}"')
    wordcloud.to_file(f"generations/python_wordcloud_{uuid_to_use}.png")
plt.show()
