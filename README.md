# Geography-ALevel-NEA
A small repo for code that I write for my A-level Geography coursework/non-examined assessment (NEA)

Includes a word cloud generator that uses the `wordcloud` module and a `requirements.txt` file for easy installation of dependencies

Now also includes "crime_analyser.py" which is a script that summarises the data from the crime data set


# Wordcloud 

## How to run

The wordcloud generator is a python server that handles requests from the client and generates a wordcloud based on the data sent from the client. 
You can view it at [https://wordcloud.pages.dev](https://wordcloud.pages.dev).

## How to run locally

Firstly, clone this repository with `git clone https://github.com/Draggie306/Geography-ALevel-NEA.git`

Then, run `pip -r requirements.txt` to install dependencies.

Make sure the code has bool `repl_save` to `True` if you're running on a linux distro like Replit

You might want to change the parameters in the `WordCloud` function from an 8K output to something smaller like:

```py
    width=1920,  # This is a 1920x1080 16:9 monitor
    height=1080,  
    max_words=1000,
    background_color="white",
```

Change the code to not have any flask stuff - just the wordcloud generation (should be fairly easy to do)
Pass in the data you want to generate the wordcloud from as a string and magic should happen

# Crime Analyser

This script is a simple script that analyses the crime data set from https://data.police.uk/data/ and outputs a list of crime types and their average count per month for any given area (in this case, Norwich 007E) from Oct 2020 to Sept 2023. You can change the area and time period by changing the folder_path variable in the for loop.

## How to run

Firstly, clone this repository with `git clone https://github.com/Draggie306/Geography-ALevel-NEA.git`

The only dependencies are os, csv and collections, so you should be able to run it without installing anything
 
Currently there is no support for changing of directories so you will have to change the folder_path variable in the for loop to the directory of the data set you want to analyse

Go to https://data.police.uk/data/ and download the data set you want to analyse, and unzip it into the directory you have hardcoded into the script.

Then, run the script with `python crime_analyser.py` and it should output a list of crime types and their average count per month for any given area (in this case, Norwich 007E) from Oct 2020 to Sept 2023.

Example output:
```
Analytics:
Found 4,916 crime records across 30 months.
14 different crime types matched the LSOA code Norwich 007A.
Total crimes in Norfolk: 191,723


Crime Type                      Total Count             Average crimes/month
-----------------------------------------------------------------------------
Violence and sexual offences   1302                     43.40
Anti-social behaviour          951                      31.70
Shoplifting                    702                      23.40
Public order                   665                      22.17
Criminal damage and arson      265                      8.83
Other theft                    260                      8.67
Bicycle theft                  198                      6.60
Drugs                          165                      5.50
Burglary                       110                      3.67
Theft from the person          87                       2.90
Other crime                    76                       2.53
Possession of weapons          54                       1.80
Robbery                        50                       1.67
Vehicle crime                  31                       1.03

4,916 crimes in total, average of 163.87 crimes per month.
```

From this data, you can then analyse it - I trust you! :)

# Contributing
## Pull Requests
Pull requests are welcome! Please make sure that you have tested your code before submitting a pull request.

# Issues
If you find any issues, please submit an issue and I will try to fix it as soon as possible.
