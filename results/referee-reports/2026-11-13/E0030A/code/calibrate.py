#!/usr/bin/env python3
"""Matched stronger searches, plus complete-graph lower bounds on a subset."""
import csv
import json
from experiment import instance, ROOT
from validate import bound

def main():
    output=ROOT/'data'/'calibration.csv'
    with output.open('w',buffering=1) as f:
        writer=None
        for n,count in [(100,40),(300,30),(1000,24),(3000,16),(10000,12)]:
            for index in range(count):
                weak,xy,_=instance(n,index,80)
                strong,_,tour=instance(n,index,320)
                row={'n':n,'index':index,'point_seed':weak['point_seed'],
                     'baseline80':weak['best'],'strong320':strong['best'],
                     'combined':min(weak['best'],strong['best']),
                     'improvement':weak['best']-min(weak['best'],strong['best']),
                     'baseline_start1':weak['best1'],'baseline_start2':weak['best2'],
                     'strong_start1':strong['best1'],'strong_start2':strong['best2'],
                     'hk_lower':None,'hk_seconds':None,'hk_iterations':None}
                if index<3:
                    lower=bound(xy,row['combined'],200)
                    row.update(hk_lower=lower['lower_bound'],hk_seconds=lower['seconds'],
                               hk_iterations=lower['iterations'])
                    assert lower['lower_bound']<=row['combined']+1e-9
                if writer is None:
                    writer=csv.DictWriter(f,fieldnames=list(row));writer.writeheader()
                writer.writerow(row)
                print(json.dumps({'n':n,'calibrated':index+1,
                                  'improvement':round(row['improvement'],6),
                                  'hk_lower':row['hk_lower']}),flush=True)

if __name__=='__main__':main()
