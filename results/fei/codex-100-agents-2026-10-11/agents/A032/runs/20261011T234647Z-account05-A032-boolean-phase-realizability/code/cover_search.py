import json, time, argparse
from collections import defaultdict,Counter
from decimal import Decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def prime_factors(n):
    result=Counter();p=2
    while p*p<=n:
        while n%p==0:result[p]+=1;n//=p
        p+=1
    if n>1:result[n]+=1
    return result

def search(m,seconds):
    started=time.monotonic();N=1<<m;full=(1<<N)-1
    slices=json.loads((ROOT/'out'/f'slices_m{m}.json').read_text())['records']
    bysupport=defaultdict(list);byfirst=defaultdict(list)
    for i,row in enumerate(slices):
        row['entropy']=Decimal(row['entropy_numerator_decimal'])
        row['log_signature']=Counter({2:2*m*sum(v*c for v,c in row['histogram'])})
        for v,c in row['histogram']:
            for p,e in prime_factors(v).items():row['log_signature'][p]-=v*c*e
        bysupport[row['support']].append(i)
        for x in range(N):
            if row['support']>>x&1:byfirst[x].append(i)
    covers=calls=0;best=None;signatures={}
    def accept(chosen):
        nonlocal covers,best
        covers+=1
        masses=sorted([slices[i]['size'] for i in chosen]+[0]*(4-len(chosen)),reverse=True)
        influence=sum(slices[i]['influence_numerator'] for i in chosen)+N*(masses[1]+masses[2]+2*masses[3])
        signature=Counter()
        for i in chosen:signature.update(slices[i]['log_signature'])
        signature=tuple(sorted((p,v) for p,v in signature.items() if v))
        key=(signature,influence)
        if key not in signatures:signatures[key]={'chosen':chosen.copy(),'count':0,'mass_sizes':masses}
        signatures[key]['count']+=1
        entropy=sum(slices[i]['entropy'] for i in chosen)
        ratio=entropy/Decimal(influence) if influence else Decimal(0)
        if best is None or ratio>best['ratio']:
            best={'ratio':ratio,'chosen':chosen.copy(),'signature':signature,'influence_numerator':influence,'mass_sizes':masses}
    def visit(covered,chosen):
        nonlocal calls
        calls+=1
        if calls%1000==0 and time.monotonic()-started>seconds:raise RuntimeError('FROZEN_RUNTIME_LIMIT')
        if covered==full:accept(chosen);return
        remain=full^covered
        if len(chosen)==3:
            for i in bysupport.get(remain,[]):accept(chosen+[i])
            return
        x=(remain&-remain).bit_length()-1
        for i in byfirst[x]:
            mask=slices[i]['support']
            if not mask&covered:visit(covered|mask,chosen+[i])
    visit(0,[])
    configurations=[]
    for (signature,influence),row in sorted(signatures.items()):
        configurations.append({'log_signature':signature,'influence_numerator':influence,**row})
    best['ratio_decimal']=str(best.pop('ratio'))
    best['slices']=[{k:v for k,v in slices[i].items() if k not in ('entropy','log_signature')} for i in best['chosen']]
    output={'status':'COMPLETE','m':m,'covers_mod_slice_sign_and_address_permutation':covers,'recursive_calls':calls,'objective_signatures':configurations,'best':best,'seconds':time.monotonic()-started}
    (ROOT/'out'/f'covers_m{m}.json').write_text(json.dumps(output,indent=2))
    print(json.dumps({k:v for k,v in output.items() if k!='objective_signatures'}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--m',type=int,nargs='+',required=True);p.add_argument('--seconds',type=int,default=180);args=p.parse_args()
    for m in args.m:assert m in (1,2,3,4);search(m,args.seconds)
