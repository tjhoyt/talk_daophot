''' 
Upon execution, load in "coords.tmp" outputted from the DAOPHOT psf program upon the prompting of a new star and the question "use this one?"

Requirements:
    1) Need to have named your ds9 viewer object as "viewer" for this to work.
    2) numpy must be imported as np before running this.
    3) must %run this script with the -i flag to use these previously defined variables

Execute "%run -i check_star" in the ipython session to view the next star (without having to manually copy paste the coordinates from the PSF method!) that pops up from the PSF method.

Todo: ***automatic updating!!! ***

'''
x, y = np.loadtxt('coords.tmp',unpack = True)
viewer.panto_image(x, y)
viewer.imexam()
#with open('coords.tmp') as f:
