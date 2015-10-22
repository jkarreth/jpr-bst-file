Journal of Peace Research .bst file
==================================

# Introduction 
This is an update to Steven Miller's _Journal of Peace Research_ .bst file by Baobao Zhang and Allan Dafoe. Updates have been made to make the code conform to the style of the _JPR_ as of May 2015.

The official style guides for _JPR_ are found here:

http://file.prio.no/journals/JPR/JPR-Notes-for-Authors-140909.pdf

http://file.prio.no/journals/JPR/Technical-Requirements.pdf

# How to Use

## Download

Download the [.bst file](https://github.com/13bzhang/jpr-bst-file/blob/master/code/jpr.bst) and save it to the same folder as the .tex document you are working on.

## Preamble 

In the preamble of your .tex document, include the following:

```
\usepackage[round]{natbib}
# seperators
\setcitestyle{aysep={,},yysep={,},citesep={;},notesep={: }}
# hide boxes around hyperlinks
\usepackage[hidelinks]{hyperref}
\urlstyle{same}
# customized captions for tables and figures
\renewcommand{\thetable}{\Roman{table}}
\usepackage{caption}\captionsetup{labelsep = period}
```

Here is the explanation for the separators in `setcitestyle`:
* Between citations: citesep
* Between author and year: aysep
* Between years with common author: yysep
* Next before post-note: notesep

The last two lines ensure a full stop after table and figure numbers and Roman numerals for tables.

## An Example JPR Paper Typeset Using LaTeX

See an example of a paper conforming to the JPR format in the `example_latex` folder of this GitHub repo. We include the source code (.tex files) as well as the end results (PDF files).

* [Main paper .tex file](https://github.com/13bzhang/jpr-bst-file/blob/master/example_latex/example_latex_main.tex)
* [Main paper PDF output](https://github.com/13bzhang/jpr-bst-file/blob/master/example_latex/example_latex_main.pdf)
* [Tables and Figures .tex file](https://github.com/13bzhang/jpr-bst-file/blob/master/example_latex/example_latex_tables_figures.tex)
* [Tables and Figures PDF output](https://github.com/13bzhang/jpr-bst-file/blob/master/example_latex/example_latex_tables_figures.pdf)

# Bibliography Information

## Inline Citation

For inline citations, use `\citep{citekey}` to cite with parentheses and `\cite{citekey}` to cite without. 

#### `\citep`

```
Empirical evidence from lab experiments suggests this theory is not implausible \citep{smith2000}. 
```
produces:

Empirical evidence from lab experiments suggests this theory is not implausible (Smith, 2000).

#### `\cite`

```
\cite{smith2000} suggests this theory is not implausible . 
```

produces:

Smith (2000) suggests this theory is not implausible.

### BibTeX

In your .bib document, you can include the following types of references:

* academic journal articles (use `article`)
* books (use `book`)
* essays in books (use `incollection`)
* working papers (use `techreport`) 
* web resources (use `misc`)
* news articles (use `articlenews`)

Below are examples of each reference type:

#### Academic Journal Article

```
@article{journalarticle,
  title={This Is A Journal Article},
  author={Annie Anderson and Bobby Burt and Catherine Cate Cindle},
  journal={Journal Article},
  volume={1},
  number={1},
  pages={1-10},
  year={2014},
}
```

#### Book

``` 
@book{book,
author = {Devin Dee and Ellen East and Fred Fredrick Fitz and Genny Graham},
title = {Book},
address = {New Haven, CT},
publisher = {Major University Press},
year = {2004},
edition = {2nd Edition}
}
```

Note that the address should include the city; if the city is in the United States, please include the two-letter abbreivation for the state as well. Do not include the state abbreviation for New York (the city). We provide a [Python script](#python) that will replace full state names in your .bib file with abbreviations.

"University Press" should not be abbreviated. For instance, you write type `Princeton University Press` and not `Princeton UP`.

#### Essay in a Book

```
@incollection{incollection,
author = {Harry Henri},
title = {An Essay in a Book},
booktitle = {A Collection of Essays in a Book},
editor = {Ida Inman},
address = {New York},
publisher = {Incollection Book Publisher},
year = {2004},
pages = {9--33}
}
```

Note that the address should include the city and the two-letter state or country abbreviation unless the city is New York, London, or some other major world city. "University Press" should not be abbreviated.


#### Working Paper (Unpublished Work)

```
@techreport{workingpaper,
author = {Lynn Lens Lee and Martha Morris},
title = {A Working Paper},
type = {Working Paper},
institution = {Department of Working Papers, Working Papers University},
year = {2014},
url = {www.working.edu/lee/newtheory.pdf}
}
```

Note that `type` must be be `Working Paper`. Include both the department and the university. Include a URL when possible.

#### Web Resource

```
@misc{webresource,
       author = "{Web Resource Organization}",
       title = "{A Report on the Web}",
       year = {2012},
       url = {\url{www.webreports.org/2012_report}}
}
```

#### News Article

The `articlenews` reference type was especially created for this .bst. It is not included as one of the regular reference types for .bib. 

```
@articlenews{newsarticle,
author = {Nancy Norton},
title = {A Newspaper Article},
journal = {News Article Times},
year = {2009},
month = {4 December},
url = {\url{http://newsarticletimes.com/dec-4-news.html}}
}
```

Note that `month` also includes the date before the month. Include a URL when possible.

### <a name="python"></a> State Abbreviations Python Script

The JPR style for addresses requires that states within the United States be written in the two-letter abbreviations. We provide a [Python script "state_script.py"](https://github.com/13bzhang/jpr-bst-file/blob/master/code/state_script.py) that will replace full state names in a .bib file with abbreviations and export the fixed bibliography to a new .bib file. To use this script, download it. 

In terminal, change the directory to the folder with the "state_script.py" Python script and type:

```
python state_script.py
```

You will be prompted to enter the location and name of the original .bib file and the new .bib file:

```
Original bib file:
New bib file:
```

After each prompt, type the location and file name without quotation marks, like such:

```
Original bib file:/Users/baobaozhang/Dropbox/jpr-bst-file/tests/my_old_bib.bib
New bib file:/Users/baobaozhang/Dropbox/jpr-bst-file/tests/my_new_bib.bib
```

A new .bib file with the correct state abbreviations will be exported. For instance, `address = {Princeton, New Jersey},` in the old file will be changed to `address = {Princeton, NJ},` in the new file.

## Technical Details

The original repo: https://github.com/svmiller/jpr-bst-file

This is a work in process. Please check in for new updates. 

Code: https://github.com/13bzhang/jpr-bst-file/blob/master/code/jpr.bst

Test results: https://github.com/13bzhang/jpr-bst-file/blob/master/tests/my_test.pdf

To-do list: https://github.com/13bzhang/jpr-bst-file/blob/master/tasks/to_do_list.md

