import numpy as np

efile = 'earth00-19-DE405.dat'
fp1 = open(efile,'r') #opens data file
 
if False:
    print('Error, could not open Earth ephemeris file');   # displays error message
else:  print ('yay!') # so file opened

for line in fp1:
  if line.startswith('#'): # skips comment lines
    continue
    lines = fp1.readline() # should read all lines except comment
    break #### doesnt work at all, will just pretend to have data...
  
# read first line, check right number of values and assign names to those entries
#line1vals = array of values


ephemEentries = 6 # temp fill

ephemEpos = np.zeros((ephemEentries,3))   # allocate memory for eph info
ephemEvel = np.zeros((ephemEentries,3))
ephemEacc = np.zeros((ephemEentries,3))

ephemEgps = np.zeros((ephemEentries,1))
print(ephemEpos)

#read remaining lines - Use np.loadtxt( 10 columns of ephemEentries length) will create array

# name variables apropriate columns of above array

fp1.close() #closes fp1
# del(line1vals)


####### now repeat pretty much whole process for sun file

sfile = 'sun00-19-DE405.dat'
fp1 = open(sfile,'r') #opens data file
 
if False:
    print('Error, could not open Sun ephemeris file');   # displays error message
else:  print ('yay!') # so file opened

for line in fp1:
  if line.startswith('#'): # skips comment lines
    continue
    lines = fp1.readline() # should read all lines except comment
    break #### doesnt work at all, will just pretend to have data...
  
# read first line, check right number of values and assign names to those entries
#line1vals = array of values


ephemSentries = 6 # temp fill

ephemSpos = np.zeros((ephemSentries,3))   # allocate memory for eph info
ephemSvel = np.zeros((ephemSentries,3))
ephemSacc = np.zeros((ephemSentries,3))

ephemSgps = np.zeros((ephemSentries,1))


#read remaining lines - Use np.loadtxt( 10 columns of ephemEentries length) will create array

# name variables apropriate columns of above array

fp1.close() #closes fp1



        

