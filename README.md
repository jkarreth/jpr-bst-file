Journal of Peace Research .bst file
==================================

## Introduction 
This is an update to Steven Miller's Journal of Peace Research .bst file by Baobao Zhang and Allan Dafoe. Updates have been made to make the code conform to the style of the _Journal of Peace Research_ as of May 2015.

The official style guides for _JPR_ are found here:

http://file.prio.no/journals/JPR/JPR-Notes-for-Authors-140909.pdf

http://file.prio.no/journals/JPR/Technical-Requirements.pdf


## How to Use

### Download

Download the [.bst file](https://github.com/13bzhang/jpr-bst-file/blob/master/code/jpr.bst) and save it to the same folder as the .tex document you are working on.

### Preamble 

In the preamble of your .tex document, include the following:

```
\usepackage[round]{natbib}
\setcitestyle{aysep={,},yysep={,},citesep={;},notesep={: }}
\usepackage[hidelinks]{hyperref}
\urlstyle{same}
```

Here is the explanation for the separators in `setcitestyle`:
* Between citations: citesep
* Between author and year: aysep
* Between years with common author: yysep
* Next before post-note: notesep

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
address = {New Have, CT},
publisher = {Book Publisher},
year = {2004},
edition = {2nd Edition}
}
```

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

#### Working Paper

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

Note that `type` must be be `Working Paper`. 

#### Web Resources

```
@misc{webresource,
       author = "{Web Resource Organization}",
       title = "{A Report on the Web}",
       year = {2012},
       url = {\url{www.webreports.org/2012_report}}
}
```

#### News Articles

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

Note that `month` also includes the date before the month.
 

## Technical Details

The original repo: https://github.com/svmiller/jpr-bst-file

This is a work in process. Please check in for new updates. 

Code: https://github.com/13bzhang/jpr-bst-file/blob/master/code/jpr.bst

Test results: https://github.com/13bzhang/jpr-bst-file/blob/master/tests/my_test.pdf

To-do list: https://github.com/13bzhang/jpr-bst-file/blob/master/tasks/to_do_list.md
