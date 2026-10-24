"""Exact rational checks of the saved obstruction; not a formal proof checker."""
from fractions import Fraction as F
import json
import pathlib
import time

ROOT=pathlib.Path(__file__).resolve().parent

class Q:
    """a+b*s in Q(s), s^2=-3; s is interpreted as i*sqrt(3)."""
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,other):
        if not isinstance(other,Q): other=Q(other)
        return Q(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,other): return self+(-other if isinstance(other,Q) else Q(-other))
    def __mul__(self,other):
        if not isinstance(other,Q): other=Q(other)
        return Q(self.a*other.a-3*self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__=__mul__
    def __truediv__(self,other):
        if not isinstance(other,Q): other=Q(other)
        norm=other.norm2()
        if norm==0: raise ZeroDivisionError
        return self*Q(other.a/norm,-other.b/norm)
    def norm2(self): return self.a*self.a+3*self.b*self.b
    def __eq__(self,other):
        if not isinstance(other,Q): other=Q(other)
        return self.a==other.a and self.b==other.b
    def encode(self): return [str(self.a),str(self.b)]

def rank_rational(rows):
    a=[[F(x) for x in row] for row in rows]
    rank=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        value=a[rank][col]
        a[rank]=[x/value for x in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][col]:
                coefficient=a[i][col]
                a[i]=[x-coefficient*y for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a): break
    return rank

def verify(delta):
    omega=Q(F(1,2),F(1,2))
    vertices=[Q(delta)]
    for _ in range(5): vertices.append(vertices[-1]*omega)
    increments=[vertices[(j+1)%6]-vertices[j] for j in range(6)]
    midpoints=[(vertices[j]+vertices[(j+1)%6])/2 for j in range(6)]
    values=[Q(delta)/d for d in increments]
    local_residuals=[(midpoints[j]-vertices[j])*values[j]+(midpoints[(j-1)%6]-vertices[j])*values[(j-1)%6] for j in range(6)]
    assert all(x==0 for x in local_residuals)
    assert all(x.norm2()==1 for x in values)
    assert all((values[(j+1)%6]-values[j]).norm2()==1 for j in range(6))
    assert all((midpoints[(j+1)%6]-midpoints[j]).norm2()==F(3,4)*delta*delta for j in range(6))
    circulation=sum((d*x for d,x in zip(increments,values)),Q())
    assert circulation==Q(6*delta)
    # Third incident edges have value zero; vertices outside the face have no supported edge.
    # Therefore these six exact residuals exhaust the nontrivial equations.
    return {"delta":str(delta),"nonzero_midpoints":6,"maximum_local_residual_squared":"0","norm_squared":"1","adjacent_jump_squared":"1","adjacent_distance_squared":str(F(3,4)*delta*delta),"face_circulation":circulation.encode()}

def main():
    start=time.perf_counter()
    deltas=[F(1,2**j) for j in range(1,13)]
    rows=[verify(delta) for delta in deltas]
    incidence=[[int(v==j)-int(v==(j+1)%6) for j in range(6)] for v in range(6)]
    rank=rank_rational(incidence)
    assert rank==5
    metrics={"command":"python -X utf8 verify_cycle_modes.py","arithmetic":"exact fractions in Q(i*sqrt(3))","mesh_cases":len(rows),"nontrivial_vertex_equations_checked":6*len(rows),"all_local_residuals_exactly_zero":True,"one_hexagon_rank":rank,"one_hexagon_nullity":6-rank,"boundary_value_difference":"0","jump_at_every_mesh":"1","rows":rows,"elapsed_seconds":time.perf_counter()-start,"scope":"Verifies this explicit cycle mode and finite incidence rank; independent mathematical review remains required; does not verify the actual SAW observable or P0003."}
    (ROOT/"cycle_metrics.json").write_text(json.dumps(metrics,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in metrics.items() if k!="rows"}))

if __name__=="__main__": main()
