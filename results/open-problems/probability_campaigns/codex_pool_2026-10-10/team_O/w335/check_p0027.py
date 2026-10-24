from fractions import Fraction as F
import json
import math
import pathlib
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()

def rational_rank(rows,columns):
    matrix=[[F(v) for v in row] for row in rows if any(row)]
    rank=0
    for col in range(columns):
        pivot=next((r for r in range(rank,len(matrix)) if matrix[r][col]),None)
        if pivot is None:
            continue
        matrix[rank],matrix[pivot]=matrix[pivot],matrix[rank]
        divisor=matrix[rank][col]
        matrix[rank]=[v/divisor for v in matrix[rank]]
        for r in range(rank+1,len(matrix)):
            multiple=matrix[r][col]
            if multiple:
                matrix[r]=[matrix[r][j]-multiple*matrix[rank][j] for j in range(columns)]
        rank+=1
        if rank==columns:
            break
    return rank

tensors=[]
for d in (1,2,3,4):
    triples=[(i,j,k) for i in range(d) for j in range(d) for k in range(d)]
    positions={triple:index for index,triple in enumerate(triples)}
    rows=[]
    for i,j,k in triples:
        sym=[0]*len(triples)
        sym[positions[i,j,k]]+=1
        sym[positions[j,i,k]]-=1
        skew=[0]*len(triples)
        skew[positions[i,j,k]]+=1
        skew[positions[i,k,j]]+=1
        rows.extend((sym,skew))
    rank=rational_rank(rows,len(triples))
    assert rank==d**3
    tensors.append({'dimension':d,'tensor_variables':d**3,'exact_constraint_rank':rank,'nullity':d**3-rank})
geometry=[]
for inner in (0,0.5,1,3):
    for theta in (0,math.pi/6,math.pi/2,math.pi):
        claimed=2*inner*abs(math.sin(theta/2))
        measured=math.hypot(inner-inner*math.cos(theta),inner*math.sin(theta))
        assert abs(measured-claimed)<1e-12
        geometry.append({'inner_radius':inner,'angle':theta,'minimum_displacement':claimed})
measurement={'command':'python -X utf8 check_p0027.py','exact_tensor_rank_cases':tensors,'rotation_gap_cases':geometry,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS; checks cover the algebraic and geometric steps, not stochastic-path formalization'}
(root/'p0027_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
rigid_statement='Let D be a bounded connected C^2 domain in R^d and F:D->D a C^2 diffeomorphism. If, for every initial x in D, normal reflected Brownian motion X started at x has F(X_t) with the normal reflected-Brownian law started at F(x), then F(x)=Qx+b for a fixed orthogonal Q and b. The conclusion uses smoothness, an onto map, and all starting points; it does not classify arbitrary measurable deterministic maps or convert every shy coupling to a deterministic one.'
rigid_proof=(root/'P0027_proof.md').read_text(encoding='utf-8').split('Proof. ',1)[1].split('\n\nFor an isometry',1)[0]
rigid=entry('p0027-smooth-map-rigidity','probability.stochastic-processes','smooth-deterministic-reflected-brownian-state-map-euclidean-rigidity','lemma','Smooth deterministic reflected-Brownian maps are Euclidean isometries',rigid_statement,rigid_proof,['Bounded connected C^2 domain','C^2 diffeomorphism from D onto D','Normal Brownian covariance in the interior','Reflected law preserved for every initial point'])
gap_statement='Let F(x)=Qx+b be a Euclidean isometry preserving a bounded connected smooth domain D. Suppose normal reflected Brownian motion X in D almost surely visits every nonempty interior open set infinitely often. Then Y=F(X) is a reflected-Brownian coupling, and it is shy if and only if min_{closure D}|x-F(x)|>0. A bounded convex preserving domain has a fixed centroid and therefore no shy isometry coupling. A planar annulus with inner radius R>0 and nontrivial rotation theta has separation at least 2R*|sin(theta/2)|. No claim about arbitrary nondeterministic shy couplings is made.'
gap_proof=(root/'P0027_proof.md').read_text(encoding='utf-8').split('For an isometry',1)[1].split('\n\nChecks:',1)[0]
gap=entry('p0027-isometry-gap','probability.stochastic-processes','reflected-brownian-isometry-coupling-positive-displacement-criterion','lemma','Positive displacement characterizes shy isometry couplings',gap_statement,'For an isometry'+gap_proof,['Euclidean isometry preserving D','Normal reflection','Recurrence to every nonempty interior open set','Compact domain closure'])
relations=[edge_to_problem('P0027',rigid['key'],'it does not classify arbitrary measurable deterministic maps'),edge_to_attempt('P0027',rigid['key'],'F(x)=Qx+b','If an isometry F preserves a reflected-Brownian domain','generalizes'),edge_to_problem('P0027',gap['key'],'No claim about arbitrary nondeterministic shy couplings is made'),{'from_key':gap['key'],'to_key':rigid['key'],'kind':'semantic_association','rationale':'Gap card: "it is shy if and only if min_{closure D}|x-F(x)|>0"; rigidity card: "F(x)=Qx+b for a fixed orthogonal Q and b". Together they delimit the stated smooth deterministic-map class.'}]
emit(10,'P0027',[rigid,gap],relations,'P0027_proof.md','p0027_measurement.json')
print(json.dumps(measurement),flush=True)
