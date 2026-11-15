"""Exact strengthened single rank-three zero-edge target."""
import sys
from pathlib import Path
from sympy.polys.domains import QQ
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited20/inherited19/inherited18/inherited17/inherited16'))
from rank_three_target import construct

def target():
    rr,V,R,mats,controls,gs,bounds=construct();T=5*rr.gens[0];margin=QQ(1,5);gamma=4
    M=[[controls[2][i][j]+(2*gamma-2)*T*(R[i][j]-R[i][4]-R[4][j]+R[4][4])-2*margin*T*T*(1+int(i==j))for j in range(4)]for i in range(4)]
    return rr,M,gs
