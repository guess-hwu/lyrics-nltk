# lyrics-nltk


Creator: Shannon Hwu (shwu6@gatech.edu)
Author(s): Shannon Hwu,

A Natural Language Processing Project, with the Robotic Musicianship Vertically Integrated Projects under Gil Weinberg and Richard Savery:
studying the relationship between lyrics and emotions. Humans are able to understand the emotions of a song from lyric meaning and melodic choices,
like using a major/minor key, upbeat or slow song, etc. I wanted to study if an analysis of the lyrics, stripped of any meaning could also identify the type of emotion. In other words, does "60% nouns, 30% adjectives/adverbs, 10% verbs" reveal that the song is likely to be an informative song, not a sad or happy song?

In this project, I use languages: python & libraries: NLTK, xlwt.

NLTK is used to identify the grammar and parts of speech.
xlwt library is used to collect the statistics into an excel sheet.

In order to run:
- pip install both libraries (ex. "pip install xlwt" or "python -m pip install xlwt")
- * copy & paste the lyrics of your song choice (per emotion) into the .txt files in the directory
- use (Python 2 or) Python 3 to run the make file
(make.py includes more comments with instructions)

Ideas for future continuation on this project:
- Integrate Rob Firstman's usage of the genius library, JSON format in order to query songs
  (should replace * manual copy / pasting into .txt files, happy.txt, sad.txt, informative.txt, etc)
- Expand the emotional genres. More than just happy, sad, informative.
  Hypothesis: more specific categories should create better correlations between statistics and emotions.
- Collect data, find the ideal margins for each emotional genre.
- Test how accurate these margins are! Are the backwards correlations correctly identifying the emotional genre the statistics gave?
- Anything else you imagine!
