# mk2mm
Markdown to mind map. Generating freeplane/freemind/baiduNaotu mind map(`.mm`,`.km`) from markdown file. 

## How to use
Run 
```python
import md2mm
md2mm.mk2km("test.md", "test.km")
md2mm.mk2mm("test.md", "test.mm")
```

## To do 

- markdown to graphviz
- extract bold sentence or words as  node note
- extract a brief report which contains heads, topic sentence(bold sentence), tables and figures
- fix mk2mm to generat mind map which includs topic sentence as notes(bold sentence), tables and figures etc for pre-writting
