import numpy as np

# read in file
f = open('earth00-19-DE405.dat', 'r')
if False:
    print('Error, could not open Earth ephemeris file');   # displays error message
filecontents = f.readlines()
f.close()


# skip through header lines starting with '#'
filestart = 0
while 1:
    if filecontents[filestart][0] == '#':
        filestart += 1
    else:
        break

# find number of entries in the file
nentries = int((filecontents[filestart].split()[2]).strip())

# create array for data (nentries rows by 10 columns)
ephemdata = np.zeros((nentries, 10)) 

# read in the actual data
for i in range(nentries):
    thisline = []
    for j in range(4):
        lines = filecontents[filestart+1+(i*4)+j].split()
        for val in lines:
            thisline.append(float(val.strip()))
    ephemdata[i,:] = np.array(thisline)

#assign each variable
[ephemEgps, xpos, ypos, zpos, velx, vely, velz, accx, accy, accz] = [ephemdata[:,0], ephemdata[:,1], ephemdata[:,2], ephemdata[:,3], ephemdata[:,4], ephemdata[:,5], ephemdata[:,6], ephemdata[:,7], ephemdata[:,8], ephemdata[:,9]]
ephemEpos = [xpos, ypos, zpos]
ephemEvel = [ velx, vely, velz]
ephemEacc = [accx, accy, accz]

[Einitgps, Edttables, Eentries] = filecontents[22].split() ### cheating mode, FIX!
Eephem = [ephemEgps, Edttables, Eentries, ephemEpos, ephemEvel, ephemEacc]


####### Sun Stuff

# read in file
f = open('sun00-19-DE405.dat', 'r')
if False:
    print('Error, could not open Sun ephemeris file');   # displays error message
filecontents = f.readlines()
f.close()


# skip through header lines starting with '#'
filestart = 0
while 1:
    if filecontents[filestart][0] == '#':
        filestart += 1
    else:
        break

# find number of entries in the file
nentries = int((filecontents[filestart].split()[2]).strip())

# create array for data (nentries rows by 10 columns)
ephemdata = np.zeros((nentries, 10)) 

# read in the actual data
for i in range(nentries):
    thisline = []
    for j in range(4):
        lines = filecontents[filestart+1+(i*4)+j].split()
        for val in lines:
            thisline.append(float(val.strip()))
    ephemdata[i,:] = np.array(thisline)

#assign each variable
[ephemSgps, xpos, ypos, zpos, velx, vely, velx, accx, accy, accz] = [ephemdata[:,0], ephemdata[:,1], ephemdata[:,2], ephemdata[:,3], ephemdata[:,4], ephemdata[:,5], ephemdata[:,6], ephemdata[:,7], ephemdata[:,8], ephemdata[:,9]]

ephemSpos = [xpos, ypos, zpos]
ephemSvel = [ velx, vely, velz]
ephemSacc = [accx, accy, accz]


[Sinitgps, Sdttables, Sentries] = filecontents[22].split()

Sephem = [ephemSgps, Sdttables, Sentries, ephemSpos, ephemSvel, ephemSacc] ### gives all data as a structured list (probably not perfect)
        

