"""PROVED partial extension: test every OPEN box with one-axis Bernstein.
No node is excluded or declared positive on floating evidence.
"""
import json,time,resource
from collections import Counter
from fractions import Fraction as F
from cover_face import ROOT,split_box
from zero_face import construct
from centered_bounds import integer_polynomial
from axis_bernstein import analysis,bound_normal


def main():
    data=json.load(open('global_cover.json'));nodes=data['nodes']
    poly=integer_polynomial(construct()[-1],80);opened=[]
    def walk(i,box):
        if nodes[i]['kind']=='split':
            left,right=split_box(box,nodes[i]['axis'])
            walk(nodes[i]['children'][0],left);walk(nodes[i]['children'][1],right)
        elif nodes[i]['kind']=='open':opened.append((i,box))
    walk(0,[tuple(map(F,b))for b in ROOT])
    start=time.time();proved=0
    for count,(i,box)in enumerate(opened,1):
        normal,denom,impact=analysis(poly,box)
        for axis in sorted(range(6),key=lambda j:-impact[j])[:2]:
            lower,controls=bound_normal(normal,denom,axis)
            if lower>=0:
                nodes[i]={'kind':'positive','method':'axis_bernstein','axis':axis,
                          'lower_Cface':str(80*lower),
                          'control_lowers':[str(80*x)for x in controls]}
                proved+=1;break
        if count%500==0:
            print('PROVED: Bernstein tested',count,'OPEN boxes; certified',proved,'seconds',round(time.time()-start,1),flush=True)
            with open('LOG.md','a')as f:f.write('\nPROVED: One-axis Bernstein pass tested '+str(count)+' OPEN boxes; '+str(proved)+' exact new positive leaves.\n')
            time.sleep(.2)
    data['counts']=dict(Counter(n['kind']for n in nodes))
    data['bernstein_pass']=dict(examined=len(opened),proved=proved,seconds=time.time()-start,
                                maxrss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with open('global_cover.json','w')as f:json.dump(data,f,separators=(',',':'))
    print('PROVED: Bernstein pass saved',data['counts'],data['bernstein_pass'],flush=True)

if __name__=='__main__':main()
