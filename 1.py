from os.path import dirname, join as pjoin
import numpy as np
import scipy.io as sio
import lsh
from scipy.io import savemat
import os
os.chdir(r"C:\Users\MSI\OneDrive - Trường ĐH CNTT - University of Information Technology\Máy tính\New folder (2)\kpca_vec\data")
Nperm = 600
Nkernel = 2
Kwindow = 128
G_vecs=[]
"""for i in range(Nperm):
  G_vecs.append(np.zeros((2,298)))
for i in range(Nperm):
  G_vecs[i] = file.getGvec(299,Nkernel)"""
count1=0
G_vecs=lsh.randompern(Nperm,G_vecs,Nkernel)
for z in range(6,141):
    print(z)
    for ii in range(1,13):
       for iii in range(ii+1,13):
          name1=str(z)+'_'+str(ii)+'.mat'
          data = sio.loadmat(name1)
          a = data['Ftemplate']
          a=np.array(a).flatten()
          binary_codes=np.zeros(Nperm,dtype=np.int16)
          binary_codes,G_vecs=lsh.WTA_hashing(a,G_vecs,Nkernel, Kwindow, Nperm)
#print(binary_codes)
#mdic = {"binary_code": binary_codes}
#print(mdic)
          name2=str(z)+'_'+str(iii)+'.mat'
          data = sio.loadmat(name2)
          b = data['Ftemplate']
          b=np.array(b).flatten()
          binary_codes1=np.zeros(Nperm,dtype=np.int16)
          binary_codes1,G_vecs=lsh.WTA_hashing(b,G_vecs,Nkernel, Kwindow, Nperm)
          count=lsh.match(binary_codes,binary_codes1)
          if((count/600)>0.11):
              count1=count1+1
          print(str(ii)+" and "+str(iii))    
          print(count/600)
print(count1)        
#os.chdir(r"C:\Users\MSI\OneDrive - Trường ĐH CNTT - University of Information Technology\Máy tính\New folder (2)\IoM_Vector_full\URP_IoM\wta")
"""
for z in range(6,141):
    print(z)
    for ii in range(1,13):
       for iii in range(ii+1,13):
          name1=str(z)+'_'+str(ii)+'.mat'
          data = sio.loadmat(name1)
          a = data['binary_codes']
          a=np.array(a).flatten()
          binary_codes=a
#print(binary_codes)
#mdic = {"binary_code": binary_codes}
#print(mdic)
          name2=str(z)+'_'+str(iii)+'.mat'
          data = sio.loadmat(name2)
          b = data['binary_codes']
          b=np.array(b).flatten()
          binary_codes1=b
          count=lsh.match(binary_codes,binary_codes1)
          if((count/600)<0.20):
              count1=count1+1
          print(str(ii)+" and "+str(iii))    
          print(count/600)
print(count1)    
"""