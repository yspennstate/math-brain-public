"""Render the saved, independently audited numerical results."""
import json,math,csv
from pathlib import Path
U=['0','1/4','1/2','3/4','7/8','1']
def load(p):return json.loads(Path(p).read_text())
def f(x):return 'undefined' if x is None else f'{x:.12f}'
def main():
    c=[load(f'census{n}.json') for n in range(1,6)];a=load('census_audit.json');rows=load('families.json');lp=load('induction_lp.json');lpa=load('induction_audit.json')
    lines=['# FEIB12 results','',
    'All numerical tables below are CHECKED within the stated finite scopes. Logs and functionals use bits; I is dimensionless. Ratios are bits per unit influence. Undefined ratios are excluded from extrema. Bit x of a hexadecimal truth table is 1 precisely when f(x)=-1, with x encoded by its input-bit mask. NPN moves preserve every reported spectral quantity. Constants have zero functionals and undefined ratios.','',
    'PROVED results and full arguments are in PROOFS.md. OPEN: a universal Phi(1/2)<=CI theorem, the requested dimension-independent monotone/LTF class bounds, and a universal unrestricted recursion potential. The finite searches do not settle these questions.','',
    '## Exhaustive census through five variables','',
    'CHECKED: census.c / census1.json through census5.json. The generator scans output-sign representatives in increasing truth-table order, marking complete orbits under coordinate permutations, coordinate negations and output negation. Every unmarked table becomes a representative. The bitmap at n=5 occupies 268,435,456 bytes; the final scan covered 4,294,967,296 truth tables. audit.py re-evaluated every representative independently in NumPy, reconstructed the complete four-variable orbit partition independently in Python, and recomputed each displayed extremal truth table by exact rational character sums and 80-decimal-digit logarithms. The maxima are numerical census claims, not interval-certified rankings.','',
    '| n | NPN classes | Truth tables covered |','|---:|---:|---:|']
    for r in c:lines.append(f"| {r['n']} | {r['classes']:,} | {r['boolean_functions']:,} |")
    lines+=['','CHECKED sup Phi(u)/I, from the census JSON files:','', '| n | '+ ' | '.join('u='+u for u in U)+' | Extremal representative |','|---:|'+':---|'*7]
    for r in c:lines.append('| '+str(r['n'])+' | '+' | '.join(f(z['value']) for z in r['suprema'][:6])+' | '+r['suprema'][0]['tt']+' |')
    lines+=['','CHECKED: for each n every displayed u has the same unique NPN extremal class listed above, as checked in census_audit.json. In n=1 the only nonconstant NPN class is a dictator, and all six values are zero. For n>=2 these Phi/I extremizers are AND_n up to NPN. Padding a function with unused variables leaves all its ratios unchanged.','',
    '| n | sup (Phi(1/2)-A)/I | Truth table | sup (Phi(1/2)-A)/(I-V) | Truth table |','|---:|---:|:---|---:|:---|']
    for r in c:
        x,y=r['suprema'][6:8];lines.append(f"| {r['n']} | {f(x['value'])} | {x['tt']} | {f(y['value'])} | {y['tt'] or 'undefined'} |")
    lines+=['',
    'CHECKED: over the union n<=5, the half-noise cancellation cost is 0.821862628209331 bits per influence, at n=5, tt=0x00010117. The maximum over I-V is 1.66014999711538, attained by AND_2 and its padded equivalents. exact_extrema.json stores long exact-character-sum evaluations; census_audit.json lists every tied NPN representative within the stated numerical tolerance. I-V=0 cases are constants and signed dictators, where the numerator is also zero.','',
    '## Structured families and random draws','',
    'CHECKED: families.py / families.json and families.csv. These are finite tested maxima, not suprema over an unbounded family. There are '+str(len(rows))+' saved rows. Every row has all six Phi/I values, I, V, both cancellation ratios, and either its full hexadecimal truth table or an exact compact symmetric description. extremal_truth_tables.json collects the maximizing row for every column in this table. Large majority truth tables have exponentially many bits and are specified by their exact weight-threshold vector instead of materialized. The exhaustive-census extremal truth tables above are all materialized.','',
    '| Family | Rows | n range | '+' | '.join('u='+u for u in U)+' |','|:---|---:|:---|'+':---|'*6]
    extrema={}
    for fam in sorted(set(r['family'] for r in rows)):
        rs=[r for r in rows if r['family']==fam];ok=[r for r in rs if r['I']>0];chosen=[max(ok,key=lambda r:r['phi_over_I'][j]) for j in range(6)];extrema[fam]={'Phi_over_I':chosen}
        lines.append('| '+fam+' | '+str(len(rs))+' | '+str(min(r['n'] for r in rs))+'–'+str(max(r['n'] for r in rs))+' | '+' | '.join(f(r['phi_over_I'][j]) for j,r in enumerate(chosen))+' |')
    lines+=['','| Family | max half-noise cost / I | Witness | max half-noise cost / (I-V) | Witness |','|:---|---:|:---|---:|:---|']
    for fam in sorted(extrema):
        rs=[r for r in rows if r['family']==fam and r['I']>0];x=max(rs,key=lambda r:r['cost_over_I']);y=max((r for r in rs if r['cost_over_excess'] is not None),key=lambda r:r['cost_over_excess'])
        extrema[fam]['cost_over_I']=x;extrema[fam]['cost_over_excess']=y
        lines.append(f"| {fam} | {f(x['cost_over_I'])} | {x['name']} | {f(y['cost_over_excess'])} | {y['name']} |")
    lines+=['',
    'CHECKED family definitions: AND_n includes every n=1..16 and n=24,32,64,128,256. Majority includes odd n=1..15 and n=17,33,65,129,257,513; the large evaluations use a closed spectral formula, independently compared to dense transforms in overlapping dimensions. Tribes uses (width,tribes)=(1,2),(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4). PM(K33) is the monotone graph property that a selected edge set in K_{3,3} contains a perfect matching. Address functions have k=1,2,3 address bits and 2^k data bits. Read-once formulas use AND/OR/NOT with six seeded random trees at each n=4,6,8,12,16. Their exact trees, including leaf negations, are saved. Random means 24 mixed unbiased/biased draws at each n=6,8,12,16; constants can occur and are excluded from ratios. The 32 LTFs have positive integer weights, eight draws at each of the same dimensions, with three threshold quantiles. All weights, thresholds and seeds are in the source/data.','',
    '## The four proposed routes','',
    'CHECKED / PROVED: the raw median inequality is false even for a unique median. unique_median_counterexample.json gives n=4, tt=0xaaa9, S mask 1, q=(9,3,3,1)/16, median 0, and F(1/2)/up=91/128. PROOFS.md proves the corrected quantile inequality and the atom-plus-conditional-mean bound, each tested before proof on all four-variable functions and the six-variable sample.','',
    '| Majority n | I | true half-noise cost / I | old Jensen / I | atom bound / I | quantile bound / I | median level / I | H_nu(S given U) / I |','|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in rows:
        if r['family']=='majority' and r['n']>=17:
            lines.append('| '+str(r['n'])+' | '+' | '.join(f(r[k]) for k in ['I','cost_over_I','mean_Jensen_over_I','atom_bound_over_I','quantile_bound_over_I','median_level_over_I','conditional_entropy_over_I'])+' |')
    lines+=['',
    'CHECKED: these rows show the mean and median costs growing while the atom/quantile costs stay much smaller. PROVED: the atom bound is at most B and at most the old Jensen bound, so the supplied symmetric B theorem gives an O(I) majority bound without its old mean defect. OPEN: a new universal O(I) bound for this expression.','',
    'CHECKED: reverse hypercontractivity for |g| at u=1/2 passed the actual derivative checks, but the weighted noisy sign ratio remains the unresolved term. The largest weighted log-ratio / I was '+f(load('check_all4.json')['noisy_cancellation_sup_over_I']['value'])+' over all4 and '+f(load('check_sample6.json')['noisy_cancellation_sup_over_I']['value'])+' in the 12,000-draw six-variable sample; these are finite maxima, not universal constants. PROVED: the exact u-derivative formula is in PROOFS.md; its numerical finite-difference check is in check_*.json.','',
    'PROVED: H_nu(S|U)<=CI is equivalent up to constants to FEI; it has not removed the missing inequality. CHECKED: its ratio is already greater than 2 on majority_33 and reaches '+f(max(r.get('conditional_entropy_over_I') or 0 for r in rows))+' in the saved family table. The n<=5 census alone, whose largest ratio is '+f(c[-1]['suprema'][8]['value'])+', would miss this.','',
    '## Classes','',
    '| Class | Verdict | Explicit result |','|:---|:---|:---|',
    '| Monotone / unate | PROVED partial; OPEN uniform target | Singleton Gamma terms vanish; higher alpha(S)<=min_{i in S} Inf_i. Higher Gamma terms need not vanish. |',
    '| Symmetric | PROVED, inherited from FEIB02 | B<=3.459354 I; Gamma<=1.6 I; hence every noise cancellation cost is <=3.459354 I. |',
    '| Linear threshold | PROVED partial; OPEN uniform target | Same unate first-level statement; majority_5 disproves higher-level sign purity. |',
    '| Read-once AND/OR/NOT | PROVED | Gamma=b^2 log(1/|b|)<=I/(2 ln 2). This is not a B/Phi theorem. |',
    '| All nonempty derivatives have one sign | PROVED | Same exact bias formula and Gamma bound; if the empty derivative is included, only constants qualify. |',
    '| Degree d | PROVED with d-dependent C | H, B, Phi(u)<=[2(d-1)+1/ln 2]I; Gamma<=[d-1+1/(2 ln 2)]I. Degree 0 and 1 are handled separately. |','',
    'PROVED correction to FLOW.md section 3b: a read-once formula need not have Gamma=0. AND_2 has Gamma=1/4 bit, entirely at S=empty. FEIB04 already recorded this correction. The symmetric coefficient in the brief was an intermediate value; the final FEIB02 proof sharpens it to 3.459354.','',
    'CHECKED: classes_all4.json covers all 65,536 four-variable functions, including 168 increasing monotone functions and 1,146 functions whose nonempty derivatives all have one sign. classes_sample6.json adds 3,000 mixed draws. The class identities, degree granularity and entropy bound had no violations. families_audit.json independently reconstructs every read-once tree and checks signs on all derivatives up to n=8, plus 16 sampled nonempty derivatives per larger tree.','',
    '## Induction LP and its failure beyond fitting','',
    'CHECKED: induction_lp.py / induction_lp.json and induction_constraints.npz. The roots are 222 NPN representatives. Every remaining coordinate at every E/D descendant is constrained: '+str(lp['unique_nodes'])+' unique dyadic nodes and '+str(lp['constraints'])+' local inequalities. The feature definitions and root prices are in PROOFS.md. The objective minimizes c plus the priced bias feature; the request for a largest upper-bound coefficient has no finite optimum.','',
    '| Potential family | Fitted resulting coefficient | c |','|:---|---:|---:|']
    for r in lp['results']:lines.append(f"| {r['label']} | {f(r['objective'])} | {f(r['c'])} |")
    lines+=['','CHECKED: the best signed fit uses G coefficients '+', '.join(f(x) for x in lp['results'][3]['G_coefficients'])+' in the first five feature order. Adding a nonnegative priced bias feature did not improve the optimum. The weaker root-only LP is '+f(load('root_only_lp.json')['objective'])+'; it is not an induction certificate. induction_audit.json independently replays primal residuals, numerical dual constraints/objectives, the explicit J formula, and the influence recursion.','',
    '| Held-out n | Potential family | Violating rows | Largest local violation, bits |','|---:|:---|---:|---:|']
    for r in lpa['held_out']:lines.append(f"| {r['n']} | {r['label']} | {r['violating_rows']} | {f(r['max_violation'])} |")
    lines+=['',
    'CHECKED: each held-out dimension uses 128 independently seeded mixed Boolean roots and all their descendants. Explicit real truth-vector witnesses, the split coordinate, J and derivative mass are saved in induction_audit.json. All six fitted rules fail; none is promoted to a theorem in higher dimensions.','',
    'PROVED: no fixed nonnegative combination of the five root-zero features can satisfy the coordinate-independent local induction inequality on all Boolean E/D descendants with any finite c. AND_n forces all four logarithmic-feature coefficients to vanish; a bounded dyadic linear-plus-parity descendant then has J/||D||_2^2=log_2(N+1), defeating the remaining L1-deficit feature. The full proof and the exact Boolean embedding are in PROOFS.md. This obstruction does not rule out signed features, child slacks, special coordinate orders, or other potentials.','',
    '## Audit and provenance','',
    'CHECKED: every census representative agrees across C and NumPy; the largest reported disagreement is '+format(max(r['max_census_disagreement'] for r in a),'.3e')+' (the exact scientific value is stored in census_audit.json). Explicit derivative noise energies agree exactly in check_*.json. Conditional entropies are calculated both from joint conditional probabilities and by the independent B+KL formula. Centered finite differences test the noise derivative. No theorem is inferred from sampling. The final audit collects all tolerances and resource measurements in final_audit.json.','',
    'CHECKED: source files NOTES.md and FLOW.md were read from ~/fei_solve_agent; the symmetric theorem is from ../FEIB02/PROOFS.md and REPORT.md. Brain recall helped identify the pre-existing read-once-potential warnings and the distinction between finite fitting and a certificate. The math recall command returned “math store not found.” No shared brain, mesh, fleet board or checklist was written; LEARNINGS.md is a local handoff for the launching session.']
    Path('RESULTS.md').write_text('\n'.join(lines)+'\n');Path('extremal_truth_tables.json').write_text(json.dumps(extrema,indent=2,allow_nan=False))
if __name__=='__main__':main()
