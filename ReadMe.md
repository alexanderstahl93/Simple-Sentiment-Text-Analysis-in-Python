# Simple Sentiment Analysis for URL & local text files
This repository contains Python scripts for **performing sentiment analysis on text using** the TextBlob library. The code includes two different examples:

**1. mainURL.py**:
This script demonstrates how to analyze the sentiment of an article obtained from a given URL.

**Instructions:** <br>
<ul>
<li>Install the required libraries by running "pip install textblob newspaper3k".</li>
<li>Replace the url variable with the URL of the article you want to analyze.</li>
<li>Run the script using "python mainURL.py".</li>
</ul>

The script will download the article, extract the summarized text, perform sentiment analysis, and display the sentiment polarity.

**2. mytext.py**:
This script shows how to analyze the sentiment of text stored in a file.

**Instructions:** <br>
<ul>
<li>Install the required library by running "pip install textblob".</li>
<li>Create a text file named mytext.txt in the same directory as the script.</li>
<li>Write the text you want to analyze in the mytext.txt file.</li>
<li>Run the script using "python mytext.py".</li>
</ul>
The script will read the contents of the mytext.txt file, perform sentiment analysis, and display the sentiment polarity.

Please note that the instructions assume you have Python and the required libraries already installed on your system. <br>
Learned from @NeuralNine: https://youtu.be/tXuvh5_Xyrw
