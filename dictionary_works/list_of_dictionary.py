weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22},

]
"""wc={}
for i in weather:
    for k,v in i.items():
        dist_name=k
        cur_weathr=v
        if dist_name in wc:
            old_weathr=wc[dist_name]
            if cur_weathr>old_weathr:
                wc[dist_name]=cur_weathr
        else:
            wc[dist_name]=cur_weathr
        
print(wc)"""

wc={}
for i in weather:
    for k,v in i.items():
        d_name=k
        c_weathr=v
        if d_name in wc:
            old_weathr=wc.get(d_name)
            if(c_weathr>old_weathr):
                wc[d_name]=c_weathr
                #pass
        else:
            wc[d_name]=c_weathr
print(wc)