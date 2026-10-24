"""Build exact proposals from the two discovered integer seed tables."""
from exact_core import *
from pathlib import Path
import json, math
ROOT = Path(__file__).resolve().parent
cube = [0,1,0,1,0,0,1,2,1,0,0,0,0,0,1,1,2,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,2,1,2,0,1,0,0,0,2,0,0,0,0,1,0,0,1,2,0,0,1,0,0,0,0]
tip = [0,0,1,1,6,0,0,1,6,0,1,0,1,0,0,6,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,6,0,0,0,1,0,0,0,0,0,6,0,0,0,0,0,0,6,0,0,0,0,0,1,0,0,0,6,1,1,0,0,0,0,7,0,7,0,0,1,0,0,0,1,1,0,0]
old = json.loads((ROOT.parent/'C004/exact_certificate.json').read_text())
columns = old['flows']['pivot_column_indices']
rows = old['flows']['pivot_row_indices']
C = contrast_coefficients(); Rn = right_inverse_numerators(); flows,labels=exchange_flows()
M = [[flows[j][i] for j in columns] for i in rows]
def seed_record(num,den,point):
    w = [F(a,den) for a in num]; b=at(C,point)
    assert matvec(D,w)==b and min(w)>=0 and sum(w)==1
    defect = [a-v/F(12600) for a,v in zip(w,matvec(Rn,b))]
    theta = solve(M,[defect[i] for i in rows])
    assert [sum(flows[j][i]*t for j,t in zip(columns,theta)) for i in range(90)]==defect
    td=math.lcm(*[a.denominator for a in theta]);tn=[int(a*td) for a in theta]
    return {'point':point,'denominator':den,'numerators':num,
            'flow_correction_denominator':td,'flow_correction_numerators':tn}
assert all((a*72).denominator==1 for row in C for a in row)
record={'ground_set':list(E),'sets':SETS,'diamonds':AB,
        'contrast_denominator':72,'contrast_coefficient_numerators':[[int(a*72) for a in row] for row in C],
        'coefficient_order':['constant','x','y','z'],
        'cube':seed_record(cube,36,[1,1,1]),'tip':seed_record(tip,72,[0,0,2]),
        'symmetries':{'x_flip_permutation':SIGMA,'y_flip':'interchange A and B','z_flip_permutation':TAU},
        'flow_basis_columns':columns,'flow_basis_rows':rows,
        'flow_basis_labels':[labels[j] for j in columns]}
(ROOT/'certificate.json').write_text(json.dumps(record,indent=2)+'\n')
for key in ['cube','tip']:
    r=record[key]
    print(key,'correction denominator',r['flow_correction_denominator'])
    print('numerators',r['flow_correction_numerators'])
print('certificate written')
