#!/usr/bin/env python3
import json,sys,time
import nested as N
from decimal_audit import witness

def run(part):
    rows=json.load(open('rows.json'));done=json.load(open('decimal_audit.json'));keys={(x['w'],x['coordinate'],x['order']) for x in done};out=[]
    for old in rows:
        w,D,c,k=old['w'],old['D'],old['coordinate'],old['order']
        if (w,c,k) in keys or (w==16)!=(part=='large'):continue
        T=N.Model(w,D);i={'root':0,'mate':1,'leaf':T.leaf(0,0,0)}[c];start=time.time()
        delta,r,negative=witness(w,D,i,T.order(k))
        row={'w':w,'D':D,'coordinate':c,'order':k,'decimal_inf':delta,'decimal_ratio':r,'float_ratio_difference':r-old['ratio'],'min_step':negative,'seconds':time.time()-start}
        out.append(row);print(json.dumps(row),flush=True)
        with open('decimal_'+part+'.json','w') as f:json.dump(out,f,indent=2)
if __name__=='__main__':run(sys.argv[1])
