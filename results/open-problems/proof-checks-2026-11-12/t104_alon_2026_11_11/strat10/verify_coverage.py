"""PROVED: rational coverage summaries, separate from certificate replay."""
import json
from fractions import Fraction as F

def main():
    n6=json.load(open('moment_cells.json'));an=json.load(open('allN_optimized_cells.json'))
    rho6=F(json.load(open('small_ratio_certificate.json'))['rho'])
    rhoN=F(json.load(open('allN_ratio_certificate.json'))['rho'])
    assert rho6>=F(3,20) and rhoN>=F(1,10)
    for records,rho,wanted in [(n6,rho6,F(14,25)),(an,rhoN,F(64,125))]:
        assert all(F(c['alo'])==F(11,25)for c in records)
        assert all(F(c['ahi'])>=wanted for c in records if F(c['rhi'])>rho)
        for left,right in zip(records,records[1:]):assert F(left['rhi'])==F(right['rlo'])
        assert F(records[0]['rlo'])==0 and F(records[-1]['rhi'])==1
    print('PROVED: N=6 covers all scales for r<=',rho6,'and all ratios for a<=14/25.')
    print('PROVED: every N>=6 covers all scales for r<=',rhoN,'and all ratios for a<=64/125.')
if __name__=='__main__':main()
