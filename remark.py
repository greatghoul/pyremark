# -*- coding: utf-8 -*-
import codecs, os, clik

remark = clik.App('remark', version='0.1.0', description='Remark slides utilities.')

@remark(usage='FOLDER-TO-CREATE')
def new(args, opts, console):
    """
    Create a new remark slides
    """

    if len(args) < 1:
        console.error('<red>error:</> you must provide a folder name to create')
        return 1

    slug = args[0]
    try:
        console.n('create: %s' % slug)
        os.mkdir(slug)
        with codecs.open(os.path.join(slug, 'slides.md'), 'w', encoding='utf-8') as f: 
            f.write('''title: Insert your title here
name: inverse
layout: true
class: inverse
---

Insert the content here.

---
name: last-page
template: inverse
class: center middle

## Thank you!
Slideshow created using [remark](http://github.com/gnab/remark).
''')
    except IOError, e:
        console.error(e)

if __name__ == '__main__':
    remark.main()
