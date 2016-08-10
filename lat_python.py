import numpy as np
import os

"""
This package allow to convert pandas.DataFrame to latex matrix
Please, use only the first function

"""
datadir = os.path.expanduser('~')+'/'
txt = '5C'
charbar = ''.join([chr(int(''.join(c), 16)) for c in zip(txt[0::2],txt[1::2])])


        
def matrix_to_txt(pd_mat, adress="table_no_name") :
    """
    convert pandas.DataFrame matrice
    have to be conbined with the save protocol because of string
    """
    ll = len(pd_mat)
    lc = len(pd_mat.T)
    col = pd_mat.columns
    ind = pd_mat.index
    
    bali, balend = balise(text="tabular")
    
    with open(datadir+adress+".txt", "w") as f:
        #{| l | c | c | c | c | c | c | c | c | }
        
        f.write(bali+"{| l |"+ " c |"*lc+" } \\hline \n")                
                
        write_line(" ", sqb = col, seq=[], f=f)
                   
        for J in range(ll) :
            idx = ind[J]
            write_line(idx, sqb=[], seq=np.array(pd_mat.loc[idx]), f=f)
        f.write(balend)
    
    
    
    
def write_line(idx, sqb=[], seq=[], f=None) :
    
    f.write(charbar+"textbf{"+str(idx)+"} ")
    
    for i in sqb :
        f.write(charbar+"& textbf{"+str(i)+"} ")
    
    for i in seq :
        f.write("& {} ".format(i))
        
    f.write("{}{} \\hline \n".format(charbar, charbar)) # create \\ for a new line
    return

def balise(text="none") :
    ini = charbar+"begin{"+text+"}"
    end = charbar+"end{"+text+"}"
    return ini, end
