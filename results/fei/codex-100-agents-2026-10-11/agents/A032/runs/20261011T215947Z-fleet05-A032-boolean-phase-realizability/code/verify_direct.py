import json, math
from pathlib import Path
from itertools import product
ROOT=Path(__file__).resolve().parents[1]

def transform(values):
    N=len(values)
    return [sum(values[s]*(1 if (s&x).bit_count()%2==0 else -1) for s in range(N)) for x in range(N)]

checked=0
for n in range(5):
    N=1<<n
    summary=json.loads((ROOT/'out'/f'summary_n{n}.json').read_text())
    keys=set()
    for line in (ROOT/'out'/f'catalogue_n{n}.jsonl').read_text().splitlines():
        row=json.loads(line); mask=row['truth_mask_with_first_value_positive']
        truth=[1]+[-1 if mask>>(i-1)&1 else 1 for i in range(1,N)]
        assert list(map(abs,transform(truth)))==row['magnitudes']
        keys.add(tuple(row['magnitudes'])); checked+=1
    assert len(keys)==summary['distinct_spectral_laws']
    # Independently check all pattern placement counts combinatorially.
    for row in summary['pattern_ledger']:
        multiplicities={v:row['pattern'].count(v) for v in set(row['pattern'])}
        total=math.factorial(N)
        for count in multiplicities.values(): total//=math.factorial(count)
        assert total==row['realizable_laws']+row['impossible_laws']

# Explicit coupled-phase obstruction. Every individual XOR equation has a
# partition, but there is no common phase satisfying all equations.
a=[8,8]+[4]*8+[0]*6
pair_witnesses=[]
for u in range(1,16):
    pairs=[(s,s^u,a[s]*a[s^u]) for s in range(16) if s<(s^u) and a[s] and a[s^u]]
    total=sum(v for s,t,v in pairs)
    found=None
    for bits in product((0,1),repeat=len(pairs)):
        if sum(bit*term[2] for bit,term in zip(bits,pairs))*2==total:
            found=bits;break
    assert found is not None
    pair_witnesses.append({'xor':u,'pairs':pairs,'partition_bits':found})
rejections=[]
for mask in range(512):
    signed=[a[0]]+[(-a[i] if mask>>(i-1)&1 else a[i]) for i in range(1,10)]+[0]*6
    # Direct signed convolution, distinct from the inverse-transform search.
    violations=[(u,sum(signed[s]*signed[s^u] for s in range(16))) for u in range(1,16)]
    bad=next(((u,v) for u,v in violations if v),None)
    assert bad is not None
    rejections.append({'phase_mask':mask,'nonzero_xor':bad[0],'convolution_integer':bad[1]})
certificate={'magnitudes':a,'probability_denominator':256,'individual_xor_partitions':pair_witnesses,'complete_phase_domain':'first nonzero phase+; remaining9 arbitrary signs','phase_rejections':rejections,'status':'IMPOSSIBLE'}
(ROOT/'out'/'coupled_phase_certificate.json').write_text(json.dumps(certificate,indent=2))
result={'status':'PASS','catalogue_witnesses_directly_reconstructed':checked,'coupled_phase_rejections':len(rejections),'individual_xor_equations_with_separate_valid_partitions':len(pair_witnesses),'review_status':'AUTHOR_DIFFERENT_IMPLEMENTATION; independent human/agent review pending'}
(ROOT/'out'/'direct_verification.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
