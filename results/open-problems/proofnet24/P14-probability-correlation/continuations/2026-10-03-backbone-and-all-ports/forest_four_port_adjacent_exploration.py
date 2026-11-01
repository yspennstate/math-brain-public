"""Four-plus-port adjacent proportional terminal-path exploratory search.

Tests the exact universal nonnegative boundary-row formulation, rather than
claiming a theorem from finite evidence. Float searches are followed by an
exact Fraction certificate if a negative result is found. Any boundary-row
counterexample need not be realizable by a weighted forest backbone.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from random import Random
import json


def partitions(n):
    out = []
    def visit(row):
        if len(row) == n: out.append(tuple(row)); return
        for value in range(max(row)+2): visit(row+[value])
    visit([0]); return out


def canonical(row):
    names = {}
    return tuple(names.setdefault(x, len(names)) for x in row)


def transfer_data(n, columns):
    states = partitions(n); indices = {state:i for i,state in enumerate(states)}
    transitions = []
    for state in states:
        row = []
        for subset in range(1 << n):
            selected = [i for i in range(n) if subset >> i & 1]
            labels = [state[i] for i in selected]
            if len(set(labels)) != len(labels): continue
            touched = set(labels)
            target = canonical(tuple(labels[0] if x in touched else x for x in state)) if labels else state
            weight = 1
            for i in selected: weight *= columns[i]
            row.append((indices[target],len(selected),weight))
        transitions.append(row)
    return states, transitions


def coeff_vectors(rows, columns):
    a,b,c = rows; states, transitions = transfer_data(len(columns),columns)
    one = [1]*len(states)
    def T(x, values):
        powers = [x**i for i in range(len(columns)+1)]
        return [sum(weight*powers[degree]*values[target]
                    for target,degree,weight in terms) for terms in transitions]
    A = T(a,T(b,T(c,one))); E = T(a+b,T(c,one)); G = T(a,T(b+c,one)); C = T(a+b+c,one)
    return states, (A,E,G,C)


def rayleigh(coeffs, v):
    values = [sum(x*y for x,y in zip(vector,v)) for vector in coeffs]
    A,E,G,C = values
    return E*G-A*C, values


def main():
    rng = Random(180003); report = {'status':'exploration only','cases':[]}
    for n, trials in ((4,2500),(5,600),(6,60)):
        bad = None; negative_cross = None; tested_pairs = 0; tested_mixtures = 0
        for trial in range(trials):
            rows = [10**rng.uniform(-2,2) for _ in range(3)]
            columns = [10**rng.uniform(-2,2) for _ in range(n)]
            states, coeffs = coeff_vectors(rows,columns); A,E,G,C = coeffs
            diagonal = [E[i]*G[i]-A[i]*C[i] for i in range(len(states))]
            for i,j in combinations(range(len(states)),2):
                cross = E[i]*G[j]+E[j]*G[i]-A[i]*C[j]-A[j]*C[i]
                tested_pairs += 1
                if cross < -1e-11*(abs(E[i]*G[j])+abs(E[j]*G[i])+abs(A[i]*C[j])+abs(A[j]*C[i])):
                    if negative_cross is None:
                        negative_cross = {'trial':trial,'rows':rows,'columns':columns,'partitions':[states[i],states[j]],'cross':cross,'diagonal':[diagonal[i],diagonal[j]]}
                    # A negative cross coefficient alone does not certify a
                    # negative quadratic form on nonnegative boundary rows.
                    if diagonal[i]>0 and diagonal[j]>0:
                        v = [0.0]*len(states); v[i]=1; v[j]=(diagonal[i]/diagonal[j])**.5
                        R, values = rayleigh(coeffs,v)
                        if R < -1e-9*max(abs(values[1]*values[2]),abs(values[0]*values[3])):
                            bad = {'trial':trial,'rows':rows,'columns':columns,'partitions':[states[i],states[j]],'weights':[1,v[j]],'R':R}; break
            if bad: break
            for _ in range(3):
                v = [10**rng.uniform(-3,3) if rng.random()<.25 else 0 for _ in states]
                R, values = rayleigh(coeffs,v); tested_mixtures += 1
                if R < -1e-9*max(abs(values[1]*values[2]),abs(values[0]*values[3])):
                    bad = {'trial':trial,'rows':rows,'columns':columns,'boundary_weights':v,'R':R};break
            if bad:break
        report['cases'].append({'ports':n,'trials':trial+1,'state_count':len(states),
            'tested_boundary_pairs':tested_pairs,'tested_boundary_mixtures':tested_mixtures,
            'negative_cross_coefficient':negative_cross,'negative_rayleigh_candidate':bad})
        print(n,'ports:',trial+1,'trials;', 'negative boundary R' if bad else 'no negative boundary R',flush=True)
        if bad: break
    Path(__file__).with_name('forest_four_port_adjacent_exploration_results.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__': main()
