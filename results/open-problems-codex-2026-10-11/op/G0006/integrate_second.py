from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write('''

## Approach B: an exact split-and-merge stationarity identity

Proposition 10. For a finite vertex set F, let K_F(eta) be the number of occupied connected components in its induced graph. For a healthy x in F, let a_x be the number of distinct occupied components of F containing a neighbor of x inside F. For an occupied x in F, let s_x be the number of distinct components of eta restricted to F with x deleted that contain a neighbor of x. Let N_x be the number of occupied neighbors of x in the FULL lattice, including those outside F. Then any stationary contact-process law satisfies

    sum_{x in F} E[lambda*(1-eta_x)*N_x*(1-a_x)
                      + eta_x*(s_x-1)] = 0.

Proof. A birth at x merges its a_x neighboring components and the new vertex into a single component, so its change to K_F is 1-a_x. A death at x removes the old component containing x and replaces it by exactly s_x components. Indeed each surviving component of the old component contains a neighbor of x: follow an old occupied path from a vertex of that component to x, stopping at the vertex before x. All components not containing x are unchanged. Thus the death change is s_x-1, including the isolated case s_x=0. The generator changes K_F only at the finitely many sites x in F, with birth rate lambda*(1-eta_x)*N_x and death rate eta_x. K_F is a bounded cylinder function and its generator is bounded. Stationarity sets its expected generator to zero, proving the formula. QED.

This confirms the dynamic route's obstacle precisely: a_x and s_x are connectivity and articulation quantities, not functions of density or adjacent pair probabilities. Dividing by |F| and sending F to the full lattice requires controlling components that connect around the finite box boundary. No sign inequality on these split-and-merge terms has been proved that would exclude an infinite occupied component near lambda_c. The identity is valid but does not close the gap.
''')
# Main attempt remains self-contained about the final outcome and points to full proofs.
p=Path('ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write('''

## 8. User-requested second attempt, 2026-10-11

A further serious attempt is fully recorded in SECOND_ATTEMPT.md. Two new routes were identified: finite stationary boxes with infected boundaries and buffered annulus crossings; and whole-cluster split-and-merge stationarity. The first was pursued through a complete reduction and small-case checks.

New proved results: Theorem 6 gives a finite stationary crossing certificate in every dimension; Lemma 7 supplies a quantitative buffered comparison at a fixed supercritical rate in d=2; Theorem 8 proves that lambda_c<lambda_p on Z^2 is equivalent to the existence of L with b_L(lambda_c)<3^(-25), using van den Berg's verified sharpness and temporal-convergence theorems. Lemma 9 proves the criterion eventually passes below 1/(2d), with an explicit certificate at d=2, lambda=1/8, L=25. A restricted three-site immigration chain proves the buffered L=1 certificate fails throughout the survival regime in d=2. Proposition 10 gives an exact finite-cluster split-and-merge stationarity identity for the other route.

These are reductions and special cases, not a proof of the requested strict inequality. Larger buffered boxes were explored using exact-CTMC numerical simulations, but no critical-rate certificate was proved. The remaining gap is now concretely the existence of a sufficiently small stationary buffered crossing probability at lambda_c (equivalent to the target in d=2), or an alternative upper estimate above lambda_c. The final verdict remains PARTIAL.
''')
p=Path('LITERATURE.md')
with p.open('a',encoding='utf8') as f:f.write('''

## Second attempt, 2026-10-11: gap-focused brain requests and verified inputs

Ran the read-only math store with the gap's key words and authors:

- `contact process near critical spatial connectivity decoupling Bezuidenhout Grimmett`
- `Liggett Schonmann Stacey domination finite dependent percolation contact process sharpness van den Berg`
- `Liggett Schonmann Stacey` (full output saved in brain_lss.txt)

Also invoked the read-only memory recall query `contact process near critical spatial mixing density correlation length mistakes`. No recalled result was accepted as a theorem proving the missing connectivity bound. The math-store outputs were mostly off topic; the BK/disjoint-occurrence hints cannot be applied to ordinary simultaneous occupation events. No LSS theorem was used or quoted: the block criterion was proved directly.

Re-examined the already downloaded van den Berg paper, arXiv:0907.2843v2, rather than running a new status search. Exact inputs (subscripts and ligatures normalized):

Theorem 1.1, PDF p. 4:

> Let λ be such that ν̄λ(|C| = ∞) = 0. Then, for every λ′ < λ there exist C1,C2 > 0 such that for all n ≥ 1, ν̄λ′(|C| ≥ n) ≤ C1 exp(−C2 n).

Theorem 2.1, PDF p. 5:

> For all λ > λc there exist C3,C4 > 0 such that for all t > 0 and all Λ finite in Z², dTV(μt;Λ, ν̄λ;Λ) ≤ |Λ| C3 exp(−C4 t).

The second quotation renders the PDF's finite-set symbol as words. These statements are used only to prove necessity of a finite certificate UNDER AN ASSUMED STRICT GAP. They are not a literature solution of the gap. Full reference: J. van den Berg, Annals of Applied Probability 21(1) (2011), 374–395, DOI 10.1214/10-AAP702.
''')
print('Saved split/merge proof, updated main attempt and literature record.')
