List of Things To Do for JPR .bst file
==========================================

[x] Middle names should not be reduced to just a first letter. Now, ‘Nils Petter Gleditsch’ is reduced to ‘Nils P Gleditsch’, ‘J David Singer’ to ‘J D Singer’, and ‘Bruce Bueno de Mesquita’ would be reduced to ‘Bruce B Mesquita’. This should be changed.

[x] In titles that include a question mark, the preceding letter is automatically converted to lower case. E.g. ‘Firing mortars? there’s an app for that.’ and ‘Empowering activists or autocrats? internet and authoritarian survival.’ This should be corrected for question marks as it has already been done for colon. 

[x] If journal volume and issue are written under ‘volume’, as e.g. ‘volume = {58(2)},’, this appears in italics. The italics should be removed. 
Ex. ‘Arellano, Manuel & Stephen Bond (1991) Some tests of specification for panel data: Monte Carlo evidence and an application to employment equations. Review of Economic Studies 58(2): 277–297.’

[ ] When there are four or more authors, semicolon should be used only after the first author. Comma should be used thereafter. 
Ex. ‘Gleditsch, Nils Petter; Peter Wallensteen; Mikael Eriksson; Margareta Sollenberg & Håvard Strand’ should be changed to ‘Gleditsch, Nils Petter; Peter Wallensteen, Mikael Eriksson, Margareta Sollenberg & Håvard Strand’. 

[x] Articles with three authors are now written as ‘et al.’ in the text. Et al. should rather be used for four or more authors. When there are three authors, all names should be spelled out in text references. We would like to change the default for when ‘et al.’ should be used, from three to four. Do you know of a way to do this?

[x] For book chapters, a space appears between publisher and the comma before page numbers, e.g. ‘New York: Columbia University Press , 47–69.’ This space should be removed. 

[x] In edited books with one editor, there should be a full stop in ‘(ed.)’, but in edited books with more than one editor, there should not be a full stop in ‘(eds)’. 

[x] URLs should be placed in parenthesis at the end of the reference without full stop before, and full stop after.

# additions to the .bst file

[?] References to books and book chapters should include city of publication, two-letter code for state if published in the United States (except for the city of New York), as well as publisher, in the following way: ‘Princeton, NJ: Princeton University Press’. There should not be full stop between the letters in the two-letter state code. Can this format be ensured automatically?

*POSSIBLE SOLUTION*: It's a bit tricky to convert the state names from long to the two-letter code. I could write a Python script that will convert people's .bib files to the right address format. 

[ ] There is currently no category for news articles, working papers or websites. Can these categories be added? Here is the JPR format: 

1) Newspaper articles should be in the following form: 

Polgreen, Lydia (2007) Raid on African Union imperils Darfur talks. International Herald Tribune 3 October: 2.
Perlroth, Nicole (2013) Syria loses access to the internet. New York Times Bits Blog 7 May (http://bits.blogs.nytimes.com/2013/05/07/syria-loses-access-to-the-internet/).

2) Working papers should be in the following form:
Morrison, Kevin (2010) Oil, conflict, and stability. Working paper. Department of Government, Cornell University (http://politics.as.nyu.edu/docs/IO/14563/Morrison.pdf).

3) Web references: 
Central Intelligence Agency (2013) The World Factbook (https://www.cia.gov/library/ publications/the-world-factbook/). 

4) World Bank (2011) World Development Indicators (http://data.worldbank.org/data-catalog/world-development-indicators).  

# instructions for submitters

In order to get not only the reference list, but also the text in JPR format, we will provide some additional information to authors using LaTeX. Below is what we have so far. If there are any particular issues that would require manual adjustment in the reference list, it would be great if you could add a description here.

To get the text references in JPR style, the following should be added: 

\usepackage{natbib}
\setcitestyle{aysep={,},yysep={,},citesep={;},notesep={: }}

Explanation:
Between citations: citesep
Between author and year: aysep
Between years with common author: yysep
Text before post-note: notesep

In order to ensure a full stop after table and figure numbers, and to insert roman numbers for tables, the following should be added:

\renewcommand{\thetable}{\Roman{table}}
\usepackage{caption}\captionsetup{labelsep = period}
