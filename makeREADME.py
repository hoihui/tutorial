import os, glob, re
os.chdir(os.path.dirname(os.path.realpath(__file__)))

out=open('README.md','w')
out.write('* files starting with lower-case letters are tutorials for packages\n')
out.write('* files starting with capitalized letters are sample codes for respective topics\n')
out.write('# TOC\n')

for fi,fn in enumerate(sorted(glob.glob('*.ipynb'))):
    out.write('## {}\n'.format(fn))
    with open(fn) as f:
        text = f.read()
    for pre, title in re.findall(r'cell_type[^\w]*markdown[^\w]*metadata": \{[^\}]*[^\w]*source": \[\n\s*"(#{1,2})\s+([^\n]*)"',text):
        out.write('  '*len(pre)+'* '+title.decode('string_escape')+'\n')
        
out.close()