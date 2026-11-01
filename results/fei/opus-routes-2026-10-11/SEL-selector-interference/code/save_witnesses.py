"""Write data/witnesses.json: exact tables and certified numbers for the SEL witnesses."""
import json
import numpy as np
from fractions import Fraction
from fei_lib import fwht_int, influence_from_W


def tab(code, n):
    return [1 - 2 * ((code >> i) & 1) for i in range(1 << n)]


out = {}
g = np.ones(16, dtype=np.int64)
g[[6, 7, 9, 11, 12, 13, 14, 15]] = -1
Wg = fwht_int(g)
out['reuse_witness_g'] = {
    'convention': 'index i: bit j of i set <=> x_j = -1; values +-1',
    'table': g.tolist(), 'walsh_times_16': Wg.tolist(),
    'H': '3', 'I': str(influence_from_W(Wg, 4)),
    'description': 'g = x2 if x2 = x3; x0 if (x2,x3) = (1,-1); x1 if (x2,x3) = (-1,1)',
    'G = g o (g o g)': {'variables': 64, 'H': '57/4', 'I': '27/8', 'H/I': '38/9', '4I': '27/2'}}
G1 = np.array(tab(2831, 4))
G2 = np.array(tab(16, 4))
out['T1sharp_boolean_witness'] = {
    'leaves_convention': 'data index i: bit j set <=> y_j = -1',
    'G1_table': G1.tolist(), 'G2_table': G2.tolist(),
    'G1_description': '-y_2 with the point y=(+1,-1,+1,-1) flipped',
    'G2_description': '1 with the point y=(+1,+1,-1,+1) flipped',
    'E[G1 G2]': str(Fraction(int(np.dot(G1, G2)), 16)),
    'cells': 'selector of r bits; A_2 = {x = (1,...,1)} (index 0), A_1 = rest',
    'excess_r9_interval': ['1.4028550034696e-5', '1.4028550034697e-5'],
    'excess_r10': '2.2432e-5', 'excess_r14': '2.4988e-6',
    'Omega_limit_scan_max': 0.0426594}
out['bent_point_flip_cost_over_delta'] = {
    str(m): v for m, v in zip(range(4, 19, 2),
                              [8.030014, 10.255970, 12.310194, 14.323621, 16.326970, 18.327806, 20.328015, 22.328068])}
out['svd_defect'] = {'kappa0_numerical': 0.756151563992684,
                     'extremal_family': 'M_t = [[t,1],[t^2(1-eta),t]], t -> 0', 'eta_star': 4.59112158874,
                     'counterexample_without_defect': [[2, -1], [-1, -1]],
                     'gap_without_defect_bits': 0.0333249268439757}
out['real_leaf_T1sharp_witness'] = {'selector': '{+-1}^2, A_1 = {(1,1)}, A_2 = rest',
                                    'G1': 'cos e - sin e * y', 'G2': 'sin e + cos e * y',
                                    'e': 0.05, 'excess_bits': 0.030707}
with open('../data/witnesses.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1)
print('written', list(out))
