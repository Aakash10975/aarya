a='<div class="col-lg-4 col-xl-3 col-sm-6">'
b='<a class="gallery-item fresco" href="img/projects/'
b1='.jpg" data-fresco-group="projects">'
c='<img src="img/projects/'
c1='.jpg" alt="">'
d='<div class="gi-text">'
e='<h4>Forest and Nature</h4>'
f='<p>Natures / Tree</p>'
g='</div>'
h='</a>'


import csv
fh = open('/Users/aakash10975/aarya/aarya/innovators.html', 'w')

for i in range(17,357):
    fh.write(a+'\n')
    fh.write('\t'+b+str(i)+b1+'\n')
    fh.write('\t'+c+str(i)+c1+'\n')
    fh.write('\t'+d+'\n')
    fh.write('\t'+e+'\n')
    fh.write('\t'+f+'\n')
    fh.write('\t'+g+'\n')
    fh.write('\t'+h+'\n')
    fh.write('</div>'+'\n')


fh.close()
