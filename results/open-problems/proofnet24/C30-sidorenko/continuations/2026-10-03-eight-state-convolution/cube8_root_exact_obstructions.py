"""Exact subsidiary obstructions; neither is a Sidorenko counterexample."""
from pathlib import Path
from fractions import Fraction as Q
import json

def multiply(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def power(A,m):
    R=[[Q(int(i==j)) for j in range(len(A))] for i in range(len(A))]
    for _ in range(m): R=multiply(R,A)
    return R

def trace(A): return sum(A[i][i] for i in range(len(A)))

def main():
    here=Path(__file__).parent
    p=[Q(0)]+[Q(1,7)]*7
    density=Q(0)
    for line in (here/'continuation_20261002_cube8_vertex_polynomial.tsv').read_text().splitlines():
        key,count=map(int,line.split());term=Q(8**6*count)
        for i in range(8):term*=p[i]**((key>>(4*i))&15)
        density+=term
    bad=density-1-Q(5*7,7**4)-Q(14*7,7**6)
    assert density==Q(688615849984,678223072849)
    assert bad==Q(-58807078,678223072849)
    C=[[Q(-1,4),Q(2)],[Q(2),Q(-1,4)]]
    block=trace(power(C,5))-Q(-3,8)**5
    assert block==Q(-1351501,32768)
    p4=[Q(1),Q(1),Q(3,2),Q(0)]
    T=[[p4[i^j]*p4[i^l]*p4[k^j] for k in range(4) for l in range(4)]
       for i in range(4) for j in range(4)]
    full=4**5*trace(power(T,5))/sum(p4)**15
    assert full>=1
    report={'status':'PASS exact Fraction reconstruction','cube8_density':str(density),
            'cycle14_gap':str(bad),'individual_character_block_fifth_trace':str(block),
            'nonnegative_four_state_host':list(map(str,p4)),
            'normalized_full_host_density':str(full),
            'claims':'Two stronger-step failures only; both hosts satisfy Sidorenko.'}
    (here/'cube8_root_exact_obstructions.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
