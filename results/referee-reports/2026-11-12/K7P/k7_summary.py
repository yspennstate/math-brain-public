"""Readable summaries of saved exact witnesses; does not mutate prior results."""
import json
from fractions import Fraction as Q
for n in (6,7,8):
    with open(f'k7_search_{n}_results.json') as f:z=json.load(f)
    print('SEARCH',n,z.get('evaluations'),z.get('seconds'),z.get('peak_rss'))
    for k,v in z['best'].items():
        print(k,'value',float(Q(v['value'])),'n=',v['n'],'pair=',v['i'],v['j'])
with open('k7_minimum_results.json') as f:z=json.load(f)
for k,v in z['best'].items():
    print('MINIMUM',k,float(Q(v['value'])),'n',len(v['w']),'partition',v['partition'])
    for o in v['orientations']:
        print('orientation',o['i'],o['j'],'lambda',float(Q(o['lambda_'])),'error',float(Q(o['error'])),'negative',float(Q(o['negative_part_bound'])))
with open('k7_leads_results.json') as f:z=json.load(f)
for k,v in z.items():
    if k=='diagonal_family':
        for a in v:print('DIAGONAL',a['shape'],a['t'],'a/T',a['a_over_T'],float(Q(a['a_over_T'])))
    elif k=='intermediate_row_sum_exceeds_proposed_budget':
        print('ROW_SUM',v['row_sum_after_first'],'budget',v['budget'],'T',v['T'])
    elif k=='cauchy_schwarz_bound_exceeds_3T':
        print('CS', 'n',len(v['w']),'partition',v['partition'],'i,j',v['i'],v['j'],'actual',float(Q(v['Fhat'])/Q(v['T'])),'gap',v['positive_square_gap'])
    elif k=='removing_orthogonal_boundary_part_loses_nonnegativity':
        print('NEGATIVITY','min modified phi',str(min(map(Q,v['modified_phi_j']))))
