"""Exact, standalone closure and Collatz certificates for the 3/5-chord matrix."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,hashlib
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parent))
from certify_bounds import sqrt_bounds,log_bounds,cosh_bounds,sinh_bounds,floor_decimal,exact

ROOT=Path(__file__).resolve().parents[1]

def canon(word):
    names={};out=[]
    for axis,sign in word:
        if axis not in names:names[axis]=len(names)
        out.append((names[axis],sign))
    return tuple(out)

def displacement_norm(word):
    sums=[0]*6
    for axis,sign in word:sums[axis]+=sign
    return sum(abs(value) for value in sums)

def expected_transitions(state,index):
    history,coverage=state
    used_axes={axis for axis,sign in history}
    r=len(used_axes)
    assert used_axes==set(range(r)) and len(history)==4 and len(coverage)==4
    out=[]
    for axis in range(r+1):
        for sign in (-1,1):
            new=(axis,sign)
            if new==(history[-1][0],-history[-1][1]):continue
            if displacement_norm(history[-3:]+(new,))==0:continue
            new_full=history+(new,)
            marks=[]
            # Independent description: add incidence vectors for new 3- and 5-chords.
            for length in (3,5):
                if displacement_norm(new_full[-length:])==1:marks.append(length)
            all_counts=list(coverage)+[0]
            for length in marks:
                for position in range(5-length,5):all_counts[position]+=1
            target=(canon(new_full[-4:]),tuple(all_counts[-4:]))
            assert target in index,'Graph is not closed under a legitimate transition.'
            out.append((index[target],sign,r if axis==r else 0,all_counts[0]))
    return out

def check_graph(graph):
    states=[(tuple(tuple(a) for a in history),tuple(c)) for history,c in graph['states']]
    assert len(states)==len(set(states))==1778
    index={state:i for i,state in enumerate(states)}
    for state,stored in zip(states,graph['rows'],strict=True):
        assert sorted(expected_transitions(state,index))==sorted(tuple(a) for a in stored)
    initial=[]
    def extend(word):
        if len(word)==4:
            counts=[0]*4
            for end in (3,4):
                if displacement_norm(word[end-3:end])==1:
                    for i in range(end-3,end):counts[i]+=1
            initial.append(index[(word,tuple(counts))]);return
        r=len({a for a,b in word})
        for axis in range(r+1):
            for sign in (-1,1):
                new=(axis,sign)
                if word and new==(word[-1][0],-word[-1][1]):continue
                if len(word)==3 and displacement_norm(word+(new,))==0:continue
                extend(canon(word+(new,)))
    extend(())
    assert sorted(initial)==sorted(graph['initial_indices'])
    return states

def main():
    graph_file=ROOT/'scripts/chord5_graph.json'
    graph=json.loads(graph_file.read_text(encoding='utf-8'))
    states=check_graph(graph)
    params_file=ROOT/'scripts/chord5_certificate_parameters.json'
    params=json.loads(params_file.read_text(encoding='utf-8'))['rows']
    old=json.loads((ROOT/'logs/exact_certificates.json').read_text(encoding='utf-8'))['rows']
    old_by_d={r['d']:Q(int(r['hairpin_lower']['n']),int(r['hairpin_lower']['d'])) for r in old}
    # Reverify the primary baseline bound; do not trust old float or baseline labels.
    al=Q(119967864025,10**11);au=Q(119967864026,10**11)
    clo,chi=cosh_bounds(al);slo,shi=sinh_bounds(al);assert al*shi-clo<0
    clo,chi=cosh_bounds(au);slo,shi=sinh_bounds(au);assert au*slo-chi>0
    coefficient_upper=Q(331371710,10**9)
    assert 4*coefficient_upper**2>au**2-1
    results=[]
    lines=['d\tchord5_lower_floor\tgain_over_CEG_percent_floor\tMv_over_v_floor']
    for p in params:
        d=p['d'];z=Q(p['z_n'],p['z_d']);s=Q(p['s_n'],p['s_d'])
        assert d>=5 and s>0 and z>1
        vec=[Q(a,p['v_d']) for a in p['v_n']]
        assert len(vec)==len(states) and min(vec)>0
        rho=Q(0)
        for i,row in enumerate(graph['rows']):
            total=Q(0)
            for j,sign,newaxis,coverage in row:
                mult=1 if newaxis==0 else d-newaxis
                assert mult>0
                total+=mult*z**sign*vec[j]/(s+1+coverage)
            ratio=total/vec[i]
            assert ratio<1,(d,i,'Mv<v failed')
            rho=max(rho,ratio)
        sqlo,sqhi=sqrt_bounds(d)
        loglo,loghi=log_bounds(z)
        lower=sqlo*loglo/s
        ceg_upper=coefficient_upper/sqlo
        assert lower>ceg_upper
        assert lower>old_by_d[d],(d,'does not improve previous certified lower bound')
        gain=lower/ceg_upper-1
        result=dict(d=d,lower=exact(lower),rho=exact(rho),CEG_upper=exact(ceg_upper),relative_gain_lower=exact(gain),previous_lower=exact(old_by_d[d]),status='exact arithmetic certificate; mathematical proof awaits independent audit')
        results.append(result)
        # Save each dimension immediately; restarting never loses completed certificates.
        (ROOT/'logs'/('chord5_certificate_d'+str(d)+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        line='\t'.join([str(d),floor_decimal(lower),floor_decimal(100*gain,6),floor_decimal(rho)])
        lines.append(line);print(line,flush=True)
    (ROOT/'logs/chord5_exact_certificates.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),arithmetic='Fraction only; independently checked full finite transition graph and all 30226 strict vector inequalities',graph_sha256=hashlib.sha256(graph_file.read_bytes()).hexdigest(),parameters_sha256=hashlib.sha256(params_file.read_bytes()).hexdigest(),state_count=len(states),transition_count=sum(map(len,graph['rows'])),rows=results),indent=2)+'\n',encoding='utf-8')
    (ROOT/'logs/chord5_certified_bounds.tsv').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('PASS: 1778-state graph closure; 17 exact positive-vector certificates; every bound beats CEG and the three-edge certificate.',flush=True)

if __name__=='__main__':main()
