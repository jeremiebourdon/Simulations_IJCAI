
# coding: utf-8

# In[27]:

import stochpy
import numpy
import matplotlib.pyplot as plt

nb_trajectories=100
gridsize=500

file = '/Users/jeremiebourdon/Stochpy/pscmodels/SmallModele1.psc'

smod = stochpy.SSA()
smod.Model(file)
smod.DoStochSim(end=gridsize,trajectories=20)
smod.PlotSpeciesTimeSeries(species2plot=['byp','byp2'])
smod.GetRegularGrid(n_samples=gridsize)
smod.PlotAverageSpeciesTimeSeries(species2plot=['byp','byp2'])
smod.PlotAverageSpeciesTimeSeries(species2plot=['A','B'])

# co-variance between byp and byp2
byp=smod.data_stochsim.species_labels.index('byp')
byp2=smod.data_stochsim.species_labels.index('byp2')

expesc1_100=numpy.empty([gridsize,nb_trajectories])
expesc2_100=numpy.empty([gridsize,nb_trajectories])

print ("Expes for modele 1")
for e in range (0,nb_trajectories):
    smod.DoStochSim(end=gridsize,trajectories=1)
    # smod.GetRegularGrid(n_samples=gridsize)
    data=smod.data_stochsim.species
    c1=data[:,byp]
    c2=data[:,byp2]
    for i in range (0,gridsize):
        expesc1_100[i,e]=c1[i]
        expesc2_100[i,e]=c2[i]
v1=[numpy.cov(expesc1_100[x,:],expesc2_100[x,:])[0,1] for x in range(0,gridsize)]

#data=smod.data_stochsim_grid.species
#v1=numpy.empty(500)
#for x in range(0,500):
#    c1=[t[x] for t in data[byp]]
#    c2=[t[x] for t in data[byp2]]
#    v1[x]=numpy.cov([c1,c2])[0,1]

plt.show()
plt.title('Correlation between byp and byp2')
plt.xlabel('Time')
plt.ylabel('Covariance')
plt.plot(numpy.linspace(0, gridsize, gridsize),v1)
plt.show()





file = '/Users/jeremiebourdon/Stochpy/pscmodels/SmallModele2.psc'

smod = stochpy.SSA()
smod.Model(file)
smod.DoStochSim(end=gridsize,trajectories=20)
smod.PlotSpeciesTimeSeries(species2plot=['byp','byp2'])
smod.GetRegularGrid(n_samples=gridsize)
smod.PlotAverageSpeciesTimeSeries(species2plot=['byp','byp2'])
smod.PlotAverageSpeciesTimeSeries(species2plot=['A','B'])

# co-variance between byp and byp2
byp=smod.data_stochsim.species_labels.index('byp')
byp2=smod.data_stochsim.species_labels.index('byp2')

expesc1_100=numpy.empty([gridsize,nb_trajectories])
expesc2_100=numpy.empty([gridsize,nb_trajectories])

print ("Expes for modele 2")
for e in range (0,nb_trajectories):
    smod.DoStochSim(end=gridsize,trajectories=1)
    # smod.GetRegularGrid(n_samples=gridsize)
    data=smod.data_stochsim.species
    c1=data[:,byp]
    c2=data[:,byp2]
    for i in range (0,gridsize):
        expesc1_100[i,e]=c1[i]
        expesc2_100[i,e]=c2[i]
v2=[numpy.cov(expesc1_100[x,:],expesc2_100[x,:])[0,1] for x in range(0,gridsize)]

#data=smod.data_stochsim_grid.species
#v1=numpy.empty(500)
#for x in range(0,500):
#    c1=[t[x] for t in data[byp]]
#    c2=[t[x] for t in data[byp2]]
#    v1[x]=numpy.cov([c1,c2])[0,1]

plt.show()
plt.title('Correlation between byp and byp2')
plt.xlabel('Time')
plt.ylabel('Covariance')
plt.plot(numpy.linspace(0, gridsize, gridsize),v2)
plt.show()


plt.title('Correlation between byp and byp2')
plt.xlabel('Time')
plt.ylabel('Covariance')
fig1,=plt.plot(numpy.linspace(0, gridsize, gridsize),[-i*0.25 for i in range(gridsize)], label='expected for Model 1')
fig2,=plt.plot(numpy.linspace(0, gridsize, gridsize),v1, label='Model 1')
fig3,=plt.plot(numpy.linspace(0, gridsize, gridsize),[i*0.25 for i in range(gridsize)], label='expected for Model 2')
fig4,=plt.plot(numpy.linspace(0, gridsize, gridsize),v2, label='Model 2')

plt.legend(handles=[fig1,fig2,fig3,fig4],loc=0)
plt.show()





# In[26]:

plt.title('Correlation between byp and byp2')
plt.xlabel('Time')
plt.ylabel('Covariance')
fig1,=plt.plot(numpy.linspace(0, gridsize, gridsize),[-i*0.25 for i in range(gridsize)], label='expected for Model 1')
fig2,=plt.plot(numpy.linspace(0, gridsize, gridsize),v1, label='Model 1')
fig3,=plt.plot(numpy.linspace(0, gridsize, gridsize),[i*0.25 for i in range(gridsize)], label='expected for Model 2')
fig4,=plt.plot(numpy.linspace(0, gridsize, gridsize),v2, label='Model 2')

plt.legend(handles=[fig1,fig2,fig3,fig4],loc=0)


plt.show()


# In[ ]:



