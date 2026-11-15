"""Independent exact audit, best-witness aggregation, and report generation.
No numerical optimization here. Every saved winner is recomputed by killed solves.
"""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import json,time,resource
from datetime import datetime
from zoneinfo import ZoneInfo
from fractions import Fraction as Q
from pathlib import Path
from q1_core import exact,lump,serialize
from q2_search import correction,fork,log
from q2_families import k5,clone,formula

start=time.monotonic();best={};checked=0;runmeta=[]
task_clock=datetime.fromtimestamp(Path('LOG.md').stat().st_birthtime,ZoneInfo('Asia/Tbilisi')).strftime('%d %B %Y, %H:%M:%S %z')
def audit(w,bs,i,j,source,expected=None):
    global checked
    w=[[Q(v) for v in row] for row in w];n=len(w)
    x=exact(w);z=exact(lump(w,bs));assert correction(x['F'],bs)==z['F']
    assert len(bs)==n-2 and i!=j and [i] in bs and [j] in bs
    p=bs.index([i]);q=bs.index([j]);T=x['t'];Fh=z['F'][p][q]
    ti=max(x['F'][i]);tj=max(x['F'][j]);ratio=Fh/T;excess=(Fh-ti-tj)/T
    if expected:
        for key,value in expected.items():
            if key in ('T','Fhat','ti','tj','ratio','excess'):
                assert Q(value)==dict(T=T,Fhat=Fh,ti=ti,tj=tj,ratio=ratio,excess=excess)[key],(source,key)
    assert ratio<=3,('COUNTEREXAMPLE',source)
    shape='triple' if any(len(b)==3 for b in bs) else 'pairs'
    for objective,value in (('ratio',ratio),('excess',excess)):
        key=f'{n}_{shape}_{objective}'
        if key not in best or value>Q(best[key]['value']):
            best[key]=serialize(dict(value=value,w=w,partition=bs,i=i,j=j,T=T,Fij=x['F'][i][j],Fhat=Fh,ti=ti,tj=tj,ratio=ratio,excess=excess,source=source))
    checked+=1

M=Q(10**12)
for n in (6,7,8):
    # Both shapes have exact near-sharp baselines. Keep a,b (or a,y) singleton.
    w=clone(k5(M),3,2);w=clone(w,0,n-4)
    bs=[[2,3,4]]+[[i] for i in range(n) if i not in (2,3,4)]
    x=exact(w);z=exact(lump(w,bs));assert (x['t'],z['t'])==formula(0,M)
    audit(w,bs,0,1,f'R2_M10pow12_padded_to_{n}')
    w=clone(fork(1,M),0,n-5);bs=[[1,3],[2,4]]+[[i] for i in range(n) if i not in (1,2,3,4)]
    x=exact(w);z=exact(lump(w,bs));assert (x['t'],z['t'])==formula(1,M)
    assert max(x['F'][5])==x['t']-(M**3+M+1)/M**3
    audit(w,bs,0,5,f'R3_M10pow12_padded_to_{n}')
    with open(f'k7_search_{n}_results.json') as f:zz=json.load(f)
    runmeta.append(dict(n=n,evaluations=zz['evaluations'],seconds=zz['seconds'],peak_rss=zz['peak_rss']))
    for key,v in zz['best'].items():audit(v['w'],v['partition'],v['i'],v['j'],f'k7_search_{n}:{key}',v)
with open('k7_probe_results.json') as f:zz=json.load(f)
for key,v in zz.items():
    if key.startswith(('ratio_','excess_')):audit(v['w'],v['partition'],v['i'],v['j'],'k7_probe:'+key,v)
with open('k7_prequotient_results.json') as f:pre=json.load(f)
for key,v in pre['best'].items():audit(v['w'],v['partition'],v['i'],v['j'],'k7_prequotient:'+key,v)

# Independently check both adversarial orthogonal-minimum obstructions.
min_obstructions=[]
for name in ('k7_min_search_results.json','k7_min_search_above2_results.json'):
    with open(name) as f:v=json.load(f)
    w=[[Q(a) for a in row] for row in v['w']];bs=v['partition'];i=v['i'];j=v['j']
    audit(w,bs,i,j,name,v)
    x=exact(w);z=exact(lump(w,bs));F=x['F'];ti=list(map(max,F));pi=x['pi'];T=x['t'];n=len(w)
    dif=[(a,b[0]) for b in bs for a in b[1:]]
    V=[[F[k][a]-F[k][b] for a,b in dif] for k in range(n)]
    S=[[V[a][k]-V[b][k] for k in range(2)] for a,b in dif]
    from q1_core import solve
    qs={a:[sum(s*t for s,t in zip(row,solve(S,[-u for u in V[a]]))) for row in V] for a in (i,j)}
    c=qs[i][j];values=[]
    assert qs[i][i]*qs[j][j]-c*c>0
    for ii,jj in ((i,j),(j,i)):
        lam=c/qs[ii][ii];gamma=[a-lam*b for a,b in zip(qs[jj],qs[ii])]
        m=[min(lam*(ti[ii]-F[ii][a]),ti[jj]-F[jj][a]-gamma[a]) for a in range(n)]
        value=-(1+1/lam)*sum(p*a for p,a in zip(pi,m))/T
        values.append(value)
    assert min(values)==Q(v['value']) and min(values)>1
    min_obstructions.append(serialize(dict(file=name,value=min(values),orientation_values=values,ratio=Q(v['Fhat'])/T,T=T,Fhat=v['Fhat'],w=w,partition=bs,i=i,j=j,evaluations=v['evaluations'],seconds=v['seconds'],peak_rss=v['peak_rss'])))

out=serialize(dict(best=best,independent_witness_audits=checked,adversarial_runs=runmeta,prequotient_metadata={k:pre[k] for k in ('networks','partitions','seconds','peak_rss')},minimum_obstructions=min_obstructions))
with open('k7_final_results.json','w') as f:json.dump(out,f,indent=2)
print('INDEPENDENT EXACT AUDIT PASSED',checked,'witnesses')
for key in sorted(best):print(key,float(Q(best[key]['value'])),best[key]['value'])
for v in min_obstructions:print('MINIMUM BOUND REJECTED',v['file'],'error',float(Q(v['value'])),'actual ratio',float(Q(v['ratio'])))
log(f'Final independent hitting-solve audit passed for {checked} exact witnesses, including all search incumbents, near-sharp baselines, and both orthogonal-minimum obstructions. All tested singleton ratios <=3. {time.monotonic()-start:.3f}s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes. No universal upper bound has been proved.')

lines=['Result: partial','',r'The question remains unresolved: this run proves neither $K(7)=3$ nor a counterexample. The established bounds remain $3\le K(7)\le4$. In particular, no finite search below is a universal inequality.','',
'The work isolates failures of all three proposed shortcuts and gives exact adversarial evidence for the remaining inequality. The new proved statement is that the diagonal projection cost at an untouched singleton cannot be bounded by any constant multiple of $T$, or of $t_i+T$. This holds for both rank-two shapes.','',
'## 1. Notation and what remains open','',
r'Use the definitions and identities in K5P_REPORT.md and K6P_REPORT.md. In particular, $T=\max_{i,j}F_{ij}$, $\phi_i=t_i-F_{i\cdot}$, $\mathcal E(\phi_i,z)=W(z_i-E_\pi z)$, and $\mathcal E(\phi_i,\phi_j)=-WF_{ij}$. Let $P$ be energy projection onto block-constant functions and $Q=I-P$, with representatives centered to have stationary mean zero. Write $q_i=Q\phi_i$. Then',
'',r'$$\widehat F_{ij}=F_{ij}+\mathcal E(q_i,q_j)/W,\qquad a_i=\mathcal E(q_i,q_i)/W=\widehat F_{ii}-F_{ii}.$$',
'',r'The previous proofs give an upper bound $T$ on entries incident to the triple and $2T$ on entries incident to either of two merged pairs. Proportional boundary vectors give $\widehat F_{ij}\le t_i+t_j$. The missing case is still two untouched singletons with independent boundary vectors. None of the arguments here bounds every such entry by $3T$.','',
'## 2. A proved obstruction to diagonal bounds','',
r'Take the four-state family $(a,b,u,v)$ with $w_{au}=w_{bu}=1$, $w_{uv}=t^2$, $w_{aa}=w_{bb}=t-1$, $w_{vv}=t^6$, and all other conductances zero except symmetry, for integers $t\ge2$. Put',
'',r'$$W=t^6+2t^2+2t+2,\quad S=t^2+2t+2,\quad N=t^7+t^6+2t^5+2t^4+2t^3+t^2+4t+2.$$',
'',r'K5P proves $T=t_a=t_b=N/W$. For the merge $\{u,v\}$, its equilibrium potential has $h_a=h_b=h_u=1$, $h_v=0$, effective resistance $R=t^{-2}$, and stationary mean $p=S/W$. Therefore',
'',r'$$a_a=WR(1-p)^2=\frac{(W-S)^2}{t^2W}=\frac{t^2(t^4+1)^2}{W},\qquad \frac{a_a}{T}=\frac{t^2(t^4+1)^2}{N}\sim t^3.$$',
'',r'Thus $a_a/T$ and $a_a/(t_a+T)$ are unbounded. At $t=10$ the first ratio is exactly $5001000050/5611071>891$. The bound $a_i\le-F_{ii}$ is valid, since $\widehat F_{ii}\le0$, but supplies no bound in terms of $T$.','',
r'To obtain the triple shape, split $v$ into two equal clones and merge $\{u,v_1,v_2\}$. To obtain two disjoint pairs, split both $u$ and $v$ into two equal clones, and merge $\{u_1,v_1\}$ and $\{u_2,v_2\}$. A clone-to-unsplit weight is half the original weight and a clone-to-clone weight, including its loop, is one quarter. These are respectively five- and six-state examples with $a,b$ untouched. Their quotients are the four-state quotient, or its equal-root clone. In both constructions $F_{aa}$ and $\widehat F_{aa}$ stay unchanged, as does $T$.','',
r'Here is a check that cloning does not create a larger original maximum. Splitting a state $c$ adds only the possible off-diagonal value $F_{cc}+1/\pi_c$, while entries from distinct original states stay fixed. Write $C=S/t^2$, $M=t+C$, and $\mu=(2t^2+S^2/t^2)/W$. For $u$, this extra value is $2C-\mu-2W/[t^2(t^2+2)]\le2C-\mu\le M-\mu=T$, since $C\le t$ for $t\ge3$; at $t=2$ it is $-3/2-\mu\le9/2-\mu=T$. For $v$, the extra value is $-\mu+W/(t^6+t^2)\le M-\mu$, since $W/(t^6+t^2)<2<M$. The quotient clones only its root: its extra value is $-2t^2/W+W/(t^6+2t^2+2)\le 2t-2t^2/W=\widehat T$. This verifies the asserted maxima.','',
r'These examples pad to any $n\ge5$ for a triple, or $n\ge6$ for two pairs, by splitting $a$ into singleton clones. The new original off-diagonal value is $2M-\mu-W(1-1/t+1/t^2)\le T$, since $M\le(9/4)t$ and $W(1-1/t+1/t^2)\ge(3/4)t^6\ge(9/4)t$. In the quotient the new off-diagonal value is $2t-2t^2/W-W(1-1/t)\le\widehat T$. The diagonal shifts by the same amount in both chains, since the mass of the untouched state is preserved, so $a_a$ is unchanged. Thus the obstruction holds specifically on seven states as well.','',
r'The exact family checks at $t=2,10,1000$, with conductances, times, and projection costs, are in k7_leads_results.json. The asymptotic formulas above, rather than those tests, establish unboundedness.','',
'## 3. Why the other shortcuts do not close the gap','',
r'Cauchy--Schwarz gives $\widehat F_{ij}\le F_{ij}+\sqrt{a_i a_j}$. The exact witness `cauchy_schwarz_bound_exceeds_3T` in k7_leads_results.json satisfies $\mathcal E(q_i,q_j)>0$ and $a_i a_j>(3T-F_{ij})^2$, with $3T-F_{ij}>0$. Thus this upper bound exceeds $3T$, although the actual quotient entry is below $3T$. It cannot serve as a universal factor-3 certificate.','',
r'The sequential row-maxima budget also fails. Start with the four-state family at $t=10$, add states $x,y$ each attached only to $v$ by conductance $10^{-6}$, and merge $\{u,v\}$ first and $\{x,y\}$ second. Both $a,b$ remain singleton. Exact hitting solves give',
'',r'$$t_a^{(1)}+t_b^{(1)}=\frac{10002120000039}{250055500001}>\frac{229169325000879}{6251387500025}=t_a+t_b+T.$$',
'',r'This rejects bounding the sum of intermediate row maxima by the desired budget. It does not reject the proposed final-entry inequality. The full conductance matrix and final entry are in `intermediate_row_sum_exceeds_proposed_budget`.','',
'## 4. Exact orthogonal-minimum refinement, and its gap','',
r'For a pair with $c=\mathcal E(q_i,q_j)/W>0$, let $\lambda=c/a_i>0$ and $\gamma=q_j-\lambda q_i$. Then $\mathcal E(\gamma,q_i)=0$, $E_\pi\gamma=0$, and $\gamma(i)=\mathcal E(\phi_i,\gamma)/W=0$. Set',
'',r'$$g=\lambda\phi_i,\quad k=\phi_j-\gamma,\quad m=\min(g,k).$$',
'',r'Here $Qg=Qk=\lambda q_i$. Consequently $g-k$ and $m-k$ are block constant. It follows that $\mathcal E(\gamma,m)=\mathcal E(\gamma,k)=0$, because $Qk=\lambda q_i$. Dirichlet minimization and the disjoint-support argument therefore give',
'',r'$$\lambda^2Wa_i\le\mathcal E(m,m)\le\mathcal E(g,m)+\mathcal E(k,m)-\mathcal E(g,k).$$',
'',r'For the upper inequality, $g-m$ and $k-m$ are nonnegative and have disjoint supports, regardless of the sign of $m$, so their cross-energy is nonpositive. The source identities, orthogonality, and $\gamma(i)=0$ give',
'',r'$$\mathcal E(g,m)=\lambda W(m_i-\bar m),\quad \mathcal E(k,m)=W(m_j-\bar m),\quad \mathcal E(g,k)=-\lambda WF_{ij},$$',
'',r'where $\bar m=E_\pi m$. Also $m_i\le t_j-F_{ij}$ and $m_j\le\lambda(t_i-F_{ij})$. Dividing by $\lambda W$ proves the exact inequality',
'',r'$$\boxed{\widehat F_{ij}\le t_i+t_j-(1+1/\lambda)E_\pi m.}$$',
'',r'This does not prove factor 3. The function $k$ can be negative; an exact example is saved as `removing_orthogonal_boundary_part_loses_nonnegativity`. More decisively, the tempting sufficient bound $-(1+1/\lambda)E_\pi m\le T$ fails even if the better of the two orientations $(i,j)$ and $(j,i)$ is chosen. The initial finite scan did not find this failure; the adversarial test did. This is why the scan is not evidence of a theorem.','']
for v in min_obstructions:
    lines.append(f"For `{v['file']}`, the smaller of the two normalized error terms is {float(Q(v['value'])):.12g}, while the actual entry ratio is {float(Q(v['ratio'])):.12g}. Both error terms exceed 1 exactly; the explicit rational values, chain, and partition are in that file and independently audited in k7_final_results.json.")
    lines.append('')
lines += [r'The second test explicitly restricts to $\widehat F_{ij}\ge2T$. Thus restricting to entries above $2T$ does not repair this sufficient bound. No bound on the actual entry follows from the large error term.','',
r'Gap: a different estimate exploiting the rank-two structure is still needed. Neither this refinement, the diagonal estimates, nor the sequential row bounds establishes $\widehat F_{ij}\le t_i+t_j+T$. The claimed constant 2 for a triple remains a conjecture.','',
'## 5. Exact best values and the search evidence','',
'The following table reports the largest values among the new searches, the fork prequotient scans, and explicitly audited baselines at parameter $10^{12}$. Every entry is an exact rational in k7_final_results.json; decimal values are only for readability. All pairs in the table are untouched singletons.','',
'| States | Shape | Best $\widehat F_{ij}/T$ | Best $(\widehat F_{ij}-t_i-t_j)/T$ |',
'|---:|---|---:|---:|']
for n in (6,7,8):
    for shape in ('pairs','triple'):
        r=best[f'{n}_{shape}_ratio'];e=best[f'{n}_{shape}_excess']
        lines.append(f"| {n} | {shape} | {float(Q(r['value'])):.15g} | {float(Q(e['value'])):.15g} |")
lines += ['',r'The ratio winners for two pairs are the exact $R_3$ family in K6P_REPORT.md, equation (12), at $M=10^{12}$; the triple ratio winners are $R_2$ in its equation (11), with the padding described below. In particular the two-pair ratio approaches 3, and the triple ratio approaches 2. These are lower bounds only.','',
r'For completeness, the following list gives every best value exactly. A record identifies the conductances, partition, pair, $T,t_i,t_j$, and quotient entry in k7_final_results.json.','']
for key in sorted(best):
    lines.append(f"- `{key}`: `{best[key]['value']}` (source `{best[key]['source']}`).")
lines += ['',r'The ratio baseline for two pairs is the six-state fork $N=1$, cloned at the untouched $a$ to reach seven or eight states, keeping each clone singleton. Its maximizing pair is $a,y_0$. Writing $U=M^3+M+1$, the original row maxima are $t_a=T_3$ and $t_{y_0}=T_3-U/M^3$. This gives the exact baseline excess $R_3-2+U/(M^3T_3)$, independently checked by hitting solves. The triple baseline splits the four-state family root $v$ into two equal clones, merges $\{u,v_1,v_2\}$, and then splits $a$ into $n-4$ equal singleton clones. It retains the original and quotient times. All conductances and the maximum checks are saved.','',
'The main optimizer used exact rational objectives on every proposal, including rejected proposals. It separately maximized the entry ratio and the excess for each shape at each size, starting from both the fork and the independent-vector obstacle witness. Conductances include powers of ten, multiplicative heavy-tailed perturbations, zero edges, extra edges, and loops. Proposal acceptance uses floating-point probabilities; all objective comparisons and saved values use Fraction.','',
'| Run | Exact objective evaluations | Seconds | Peak RSS, bytes |','|---|---:|---:|---:|']
for v in runmeta:lines.append(f"| n={v['n']} | {v['evaluations']} | {v['seconds']:.3f} | {v['peak_rss']} |")
lines += ['',f"The main runs total {sum(v['evaluations'] for v in runmeta):,} exact objectives. The separate prequotient scan checked {pre['networks']:,} chains and {pre['partitions']:,} rank-two partitions in {pre['seconds']:.3f} seconds. It starts with larger fork combs (eight or ten states), prequotients them to six, seven, or eight states, and then scans every rank-two partition. This tests a different family of adversarial starts; it found no counterexample.",'',
f'The independent final audit recomputed {checked} saved witnesses with target-by-target killed hitting systems, compared every quotient matrix against the low-rank update, verified all saved objective values, checked the baseline formulas, and confirmed the two failures of the orthogonal-minimum sufficient bound. The conditional energy argument was separately audited in k7_minimum.py, including its Dirichlet, source, and disjoint-support steps. None of these checks establishes the missing universal bound.','',
'## 6. Programs and outputs','',
'| Program | Output and data | Purpose |','|---|---|---|',
'| k7_probe.py | k7_probe_output.txt; k7_probe_results.json | Initial exact all-partition probes |',
'| k7_search.py | k7_search_6_output.txt, k7_search_7_output.txt, k7_search_8_output.txt; matching results JSON | Exact singleton ratio and excess optimization |',
'| k7_leads.py | k7_leads_output.txt; k7_leads_results.json | Diagonal family and shortcut obstructions |',
'| k7_minimum.py | k7_minimum_output.txt; k7_minimum_results.json | Exact audit of the orthogonal-minimum inequality |',
'| k7_min_search.py | k7_min_search_output.txt and k7_min_search_above2_output.txt; matching results JSON | Adversarial rejection of the sufficient mean bound |',
'| k7_prequotient.py | k7_prequotient_output.txt; k7_prequotient_results.json | Larger-fork prequotient scans |',
'| k7_summary.py | k7_summary_output.txt | Readable intermediate summaries |',
'| k7_finalize.py | k7_finalize_output.txt; k7_final_results.json; REPORT.md | Independent exact recomputation and report |',
'| k7_check_report.py | k7_check_report_output.txt | Final report and artifact checks |','',
'The reused libraries are q1_core.py, q2_search.py, and q2_families.py. No old search results were overwritten. All new findings were appended to LOG.md when obtained. Programs were saved before execution. Each task computation used one numerical-library thread; at most two computations overlapped. All measured runs were below five minutes and far below 1 GB. Python bytecode writes were disabled. No web, other agents, git pushes, visible windows, or writes outside this directory were used. External brain/checklist/mesh tools were not invoked because they write outside the authorized directory.','',
'Reproduce each program separately, for example:','',
'```sh','env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 k7_search.py 7 160 > k7_search_7_output.txt 2>&1','```','',
'Use n=6 and n=8 for the other main runs. Run k7_min_search.py without arguments for the unrestricted error search, and with argument 2 for the restricted one. Run k7_finalize.py after the searches and k7_check_report.py last. Searches append to LOG.md; reruns can change their time-limited incumbents.','',
f'Task: “settle K(7)” — {task_clock} (first local work recorded; exact receipt time unavailable).','']
Path('REPORT.md').write_text('\n'.join(lines))
assert Path('REPORT.md').read_text().splitlines()[0]=='Result: partial'
