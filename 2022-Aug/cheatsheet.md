# What is rise?
- RISE IS **NOT** A JUPYTER EXTENSION!

- It is based on an open source HTML presentation framework called reveal.js:
	https://revealjs.com/
	
- Damian Avila then created a package called RISE
which is a repository that enables reveal.js in Jupyter Notebook 
	https://github.com/damianavila/RISE

- Here is a very comprehensive website explaining rise
	https://rise.readthedocs.io/en/stable/

---------------------------------------------------------------------
# How to install rise

- Two options:
1. In the root environment, open anaconda prompt (admin):
	```
	conda install -c damianavila82 rise OR pip install RISE
	jupyter nbextension install rise --py --sys-prefix
	jupyter nbextension enable rise --py --sys-prefix
	jupyter notebook # execute from prompt
	```

2. if not running in normal environment, open anaconda prompt (admin):
	```
	conda create -n foo
	activate foo
	conda install -c damianavila82 rise
	jupyter nbextension install rise --py --sys-prefix
	jupyter nbextension enable --py rise --sys-prefix
	jupyter notebook # execute from prompt
	```
	
---------------------------------------------------------------------
# Basic settings

## Enabling slide types for cells
View -> Cell toolbar -> Slideshow

- Types of cell:
	- Slide
	- Sub-slide
	- Fragment
	- Skip
	- Notes

## ADJUSTING WIDTH/HEIGHT WHEN PRESENTING RISE + ENABLING SCROLLBAR

- Use the following cell and adjust params accordingly:
```
from notebook.services.config import ConfigManager
cm = ConfigManager()
cm.update('livereveal', {
              'width': 1000,
              'height': 600,
              'scroll': True,
})
```

## Enabling scrollbar in output cells
	Cell -> Current Outputs-> Toggle scrolling

## Enabling spellchecking in Jupyter Notebook

```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable spellchecker/main
```

## Change default browser (use Chrome!)
- The most basic way is to change your default browser! If not, try this:

### for old notebook and JupyterLab < 3.0
```
jupyter notebook --generate-config
```
- Then, change the following line:
```
c.NotebookApp.browser = u'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
```
### for new nbclassic and JupyterLab >= 3.0
```
jupyter server --generate-config
```
- Then, change the following line:
```
c.ServerApp.browser = u'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
```
---------------------------------------------------------------------
# Hiding stuff

## Input (i.e. code)

### When working on your notebook & presenting rise slides (ALL CODE CELLS)
	- Enable the "Hide input" nbextension
	- Select the "eye" icon in your jupyter notebook

### In the html version of your notebook (once compiled)

```
jupyter nbconvert filename_guided.ipynb --no-input
```

## Output (i.e. results)

### In the live notebook & rise
- Press `o` when selecting the cell

---------------------------------------------------------------------
# Using chalkboard and markers when presenting
	Edit -> edit notebook metadata
- Add the following code, for example, after line 20
```
"rise": {
    "enable_chalkboard": true
  },
```

---------------------------------------------------------------------
# Enabling speaker notes (in my case only works with Chrome)
- Press `t` when in presentation mode

---------------------------------------------------------------------
# Insert images and video code in cells

## Images

Use a markdown cell
```
![some text](image name)
```
Examples:
Image in the same directory as the notebook
	![some text](Python-logo.png)
You can also use an online image (preferred)
	![some text](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/480px-Python-logo-notext.svg.png)
Save in dropbox & change `dl=0` for `raw=1`
	![some text](https://www.dropbox.com/s/5fqm316mito008t/Python-logo.png?raw=1)

## Video

Use a code cell:
```
import warnings; 
warnings.simplefilter('ignore')
from IPython.display import HTML
HTML('html code with <iframe> tag')
```
Example:
```
import warnings; 
warnings.simplefilter('ignore')
from IPython.display import HTML
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/r-uOLxNrNk8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

```

---------------------------------------------------------------------
# Double columns
- In command prompt:
```
jupyter nbextension enable splitcell/splitcell
```
- To enable split cell, the <-> button is used

---------------------------------------------------------------------
# Changing notebook and rise slide style (not the same!)

- For the notebook itself, add a `custom.css` in /Users/x/.jupyter/custom)
	- This will SOMETIMES create a placeholder and create a .js in:
	/C:/Anaconda/Lib/site-packages/notebook/static/custom
		- You need to delete them also from this directory to revert to original template! 
- For the rise slides, use a `rise.css` file and save it in the same folder as the notebook
	- If changes cannot be seen, open the file using Notepad++

---------------------------------------------------------------------
# Hiding certain code slides
- Only works if there is a rise.css in the same dir as the nb)
- In a new cell run this code:

```
def hide_code_in_slideshow():   
    from IPython import display
    import binascii
    import os
    uid = binascii.hexlify(os.urandom(8)).decode()    
    html = """<div id="%s"></div>
    <script type="text/javascript">
        $(function(){
            var p = $("#%s");
            if (p.length==0) return;
            while (!p.hasClass("cell")) {
                p=p.parent();
                if (p.prop("tagName") =="body") return;
            }
            var cell = p;
            cell.find(".input").addClass("hide-in-slideshow")
        });
    </script>""" % (uid, uid)
    display.display_html(html, raw=True)
```

- Then, run the function in the code cells you want to hide:

```
hide_code_in_slideshow()
```

---------------------------------------------------------------------
# Enabling white axis in dark modes
```
from matplotlib import style
style.use('dark_background')
```

OR

```
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)
```

OR (for seaborn)

```
sns.set(style="whitegrid")
```

- Example plot:
```
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

- [Source](https://medium.com/@rbmsingh/making-jupyter-dark-mode-great-5adaedd814db)

---------------------------------------------------------------------
# Saving your slides

## html SLIDES
```
jupyter nbconvert filename.ipynb --to slides --post serve
```
OR (even better)
```
jupyter nbconvert filename.ipynb --to slides --post serve  --SlidesExporter.reveal_scroll=True
```
- You can always edit this file using Notepad and change stuff
	- add input, erase output, etc!

## pdf
- replace the # after the the_notebook.slides.html in the browser URL with ?print-pdf
- Save the pdf (print to pdf)

---------------------------------------------------------------------
# MORE INFO

## Creating Slideshows in Jupyter Tips

https://www.markroepke.me/posts/2019/06/05/tips-for-slideshows-in-jupyter.html

## Jupyter Notebook Markdown Tips

https://medium.com/analytics-vidhya/the-ultimate-markdown-guide-for-jupyter-notebook-d5e5abf728fd

## Where to get dark rise.css
https://github.com/uc-python/intro-python-datasci/blob/master/notebooks/rise.css

## Where to get more custom.css
https://medium.com/@formigone/my-first-custom-theme-for-jupyter-notebook-a9c1e69efdfe
https://towardsdatascience.com/10-practical-tips-you-need-to-know-to-personalize-jupyter-notebook-fbd202777e20
https://gist.github.com/levabd/eb2db79567fe737b8232db046ee12eb3