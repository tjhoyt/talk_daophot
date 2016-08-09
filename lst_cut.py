'''
1)read in temp file of star ID numbers  produced from PSF after 
trashing bad stars

2) read in an inputted (via command line; prompts are too annoying) 
lst file from daophot

3) make a new .iter file of only the stars that match the temp file

bask

'''
import sys
import numpy as np
import os.path
f = sys.argv
head = [ ]
print(f[1])
with open(f[1]) as opfile:
    head.append(opfile.readline())
    head.append(opfile.readline())
    head.append(opfile.readline())
nums = np.loadtxt('psf_list.tmp')
rows = np.loadtxt(f[1],skiprows=3)
final = [ ]
for n in nums:
    for r in rows:
        if r[0] == n:
            final.append(r)
filename, file_ext = os.path.splitext(f[1])
ofile = filename + '.iter'
np.savetxt(ofile, final,fmt=['%8.0f'] + [ '%8.3f' for x in np.arange(len(r)-1) ] )
with open(ofile, 'r+') as fi:
    content = fi.read()
    fi.seek(0, 0)
    print(head)
    print(content)
    fi.writelines(head)
    fi.write(content)
