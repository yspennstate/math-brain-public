TASK: B17 ACCOUNT: fleet02 RUN: 2026-09-21T19:47:32.193014Z — odd-majority depth-bank counterexample and harmonic-Riesz mixed curvature

MODEL: GPT-5.6 Sol (runtime self-report)
REQUESTED EFFORT: maximum actually supported
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED by the scheduler interface
EXPOSED REASONING USAGE: null / provider reasoning tokens and thinking time NOT_EXPOSED
EXECUTION: WITHOUT_VERIFIED_BRAIN
STATUS: PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy-influence conjecture remains OPEN / NOT PROVED.

Fresh authenticated control at entry:
yspennstate/math-research-brain main
570a765d71a26461e94221a75508c992a8bc72ab,
The live owner order was FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z,
with fleet02/B17 assigned the exact Boolean adversary for interface B
(quantitative joint-derivative stability).

Fresh scientific master at entry:
yspennstate/math-open-problems
f19e92d5facf03f83458aebaad175100f5f322c5,
refreshed before the derivation to
568b3f75eaa51b9049bb776ef799d25eb71fb7aa.

Normalization: f:{-1,+1}^n->{-1,+1}; p_S=\hat f(S)^2; base-2
H(f)=sum_S p_S log2(1/p_S), I(f)=sum_S |S|p_S.  After a median-character
gauge the folded quantity J becomes ordinary influence.  No novelty or
publication-priority claim is made.

# 0. Required comparison with the last three substantive B17 reports

The last three completed own B17 mechanisms were read from the current source
lineage.

1. 20260921T154809Z buried-atom cancellation flow: strict-superset
   receiver-only transport was refuted by antipodal defects; replacement was
   signed xor-cancellation.
2. 20260921T181122Z positive XOR-coupling obstruction: positive parent
   couplings were refuted by a two-defect Boolean family; replacement was an
   influence-paid mismatch code.
3. 20260921T184622Z self-XOR/Hellinger difference: singleton lateral partners
   were refuted by odd majority and coordinatewise scalarization by one-point
   defects; replacement retained the full self-XOR joint law and a negative
   Hellinger credit.

FULL-PROBLEM CHANGE: none. No dimension-independent FEI constant is proved.

MECHANISM CHANGE: yes. This run leaves the self-XOR transport route and
consumes the newer fleet04/B18 joint-derivative result.  It first shows that
the B18 ordinary derivative-depth/positive-defect bank itself cannot be
globally paid by J, even on odd majority.  It then changes category from
Boolean derivative rows D_i f to a curl-free family of harmonic Riesz rows
D_i L^{-1/2} f.  Their entire mixed-curvature mass is exactly I-tau, i.e. one
influence charge rather than a second spectral moment.

# 1. Named external result consumed: fleet04/B18

The current fleet04/B18 report
`20260921T191147Z-mixed-curvature-global-rigidity` proves, after median
character folding, that for the Boolean derivative rows

    g_i = D_i f,
    j_i = ||g_i||_2^2,
    d_i = sum_{k!=i} ||D_k g_i||_2^2,

the normalized depth defect is

    delta_i = d_i/j_i - (1/2) log2(1/j_i) >= 0.

It also proves exact mixed-curvature conservation and converts arbitrary
overlap of robust near-subcube rows to the global receiver

    sum_i d_i.

The report explicitly leaves open the missing arrow from this depth bank to
O(J); it does not claim sum_i d_i=O(J).

The present run attacks precisely that arrow rather than re-proving the local
B18 stability theorem.

# 2. PROVED: odd majority destroys every all-row ordinary-depth payment

Let n=2m+1, m>=1, and let

    f = Maj_{2m+1}.

All coordinate influences are equal to

    j = C(2m,m)/4^m <= 1/2,

so the median-character gauge is already centered and

    J(f)=I(f)=(2m+1)j.

Fix a coordinate i.  The derivative row g_i=D_i f is, up to an overall sign,
the indicator of the middle Hamming layer E in the remaining 2m variables:

    E={y: |y|=m}.

Thus ||g_i||_2^2=mu(E)=j.

For every residual coordinate k!=i, E and E+e_k are disjoint: flipping one
coordinate takes weight m to m-1 or m+1.  Hence

    Pr[1_E(y) != 1_E(y+e_k)] = 2j.

Because D_k=(u(y)-u(y+e_k))/2,

    ||D_k g_i||_2^2 = j/2.

There are 2m residual coordinates, therefore

    boxed: d_i = m j,
    boxed: d_i/j_i = m.                                  (2.1)

Consequently the fleet04/B18 positive depth defect is exactly

    boxed:
    delta_i = m - (1/2) log2(1/j).                        (2.2)

By symmetry,

    boxed:
    (sum_i d_i)/J(f) = m,                                 (2.3)

and

    boxed:
    (sum_i j_i delta_i)/J(f)
      = m - (1/2) log2(1/j).                              (2.4)

The elementary central-binomial estimate

    j=C(2m,m)/4^m >= 1/(2 sqrt(m))

gives

    (sum_i j_i delta_i)/J(f)
      >= m - 1/2 - (1/4)log2 m -> infinity.               (2.5)

Therefore:

THEOREM B17-MAJORITY-DEPTH-NOGO.
There is no universal finite constant C such that either

    sum_i d_i <= C J(f)

or

    sum_i j_i delta_i <= C J(f)

holds for every Boolean f after median-character folding.

This is a counterexample to those stronger global payment lemmas, not a
counterexample to FEI.  It uses the genuine Boolean odd-majority family.  The
majority family itself is reused from the existing project literature; the new
point here is its exact evaluation against fleet04/B18's global depth and
depth-defect banks.

# 3. Different bridge: harmonic Riesz derivative rows

The failure in Section 2 is a multiplicity failure.  Ordinary mixed depth
charges a spectral atom of size K once for every ordered pair of active
coordinates, producing K(K-1).

Let L be the Walsh number operator,

    \widehat{Lh}(S)=|S| \hat h(S),

and set the empty coefficient of L^{-1/2}h to zero.  Define the harmonic Riesz
row on the quotient cube excluding i by

    u_i := D_i L^{-1/2} f.

Its Fourier coefficients are exactly

    \hat u_i(T)
      = \hat f(T union {i}) / sqrt(|T|+1).                (3.1)

Put

    r_i = ||u_i||_2^2
        = sum_{S contains i} p_S/|S|,                    (3.2)

and for i!=k

    e_{ik}=||D_k u_i||_2^2
          =sum_{S contains i,k} p_S/|S|.                 (3.3)

Let K=|S| for S drawn from the spectral law and

    tau=Pr(K>0)=1-p_empty.

### Theorem B17-HARMONIC-RIESZ-CURVATURE

For every Boolean f (indeed for every real f with unit L2 norm),

    boxed: sum_i r_i = tau,                               (3.4)

    boxed: D_k u_i = D_i u_k for i!=k,                    (3.5)

and hence

    boxed: e_{ik}=e_{ki}.                                 (3.6)

Most importantly,

    boxed:
    sum_i sum_{k!=i} e_{ik} = I(f)-tau <= I(f).           (3.7)

Proof.
Equations (3.1)--(3.3) are Parseval.  For a fixed nonempty spectral set S of
size K, its contribution to sum_i r_i is

    K * p_S/K = p_S,

which proves (3.4).  For fixed i,k, both D_k u_i and D_i u_k have, after the
natural quotient identification, Fourier coefficient

    \hat f(T union {i,k}) / sqrt(|T|+2),

so (3.5) and (3.6) hold.  Finally a spectral atom S of size K contributes

    K(K-1) * p_S/K = (K-1)p_S

to the ordered mixed-curvature sum.  Summing gives E[(K-1)1_{K>0}]=I-tau.
QED.

This retains the exact integrability/curl-free feature that made fleet04's
mixed-derivative theorem possible, but removes the fatal extra factor K.  On
odd majority, ordinary mixed depth is mJ while the new entire harmonic
mixed-curvature bank is exactly I-1<J.

# 4. The harmonic rows are exactly the B13 marked spectral laws

Condition on a nonempty spectral sample S and choose M uniformly from S. Then

    r_i=Pr(M=i,K>0),

and, conditioned on M=i, the law of S is

    Q_i(S)=p_S/(|S|r_i),  S contains i.                   (4.1)

Thus Q_i is exactly the normalized squared Fourier law of u_i.  If

    kappa_i=E_{Q_i}(|S|-1),

then

    r_i kappa_i
      =sum_{S contains i} (|S|-1)p_S/|S|,

and (3.7) is the B13 one-charge identity

    sum_i r_i kappa_i=I-tau.                              (4.2)

This identifies a concrete common object behind the two previously separate
interfaces: B13's harmonic marker and B18's mixed derivative curvature.

There is also an exact representation of B13's remaining layer-incidence debt

    R_inc
      = tau[H(S|K,K>0)-H(M|K,K>0)].

For fixed K, because M is uniform in S,

    H(S,M|K)=H(S|K)+log2 K
            =H(M|K)+H(S|M,K).

Therefore

    boxed:
    R_inc
      = sum_i r_i H_{Q_i}(S|K)
        - E[1_{K>0} log2 K].                              (4.3)

So the unpaid entropy is precisely the within-level spectral entropy of the
harmonic Riesz rows, with an exact log-fiber credit.

# 5. Replacement universal bridge: a vector harmonic-Riesz entropy inequality

B13 already proves the universal reduction

    H(f)
      <= C0 I(f) + R_inc(f),                              (5.1)

where

    C0 = 3 + (2+e^{-1})/ln 2
       = 6.416127927200970....

Sections 3--4 suggest replacing row-by-row Boolean depth stability by a joint
curl-free Riesz-field statement.

A sufficient universal target is:

(HR_C) There is a dimension-independent finite C_R such that, after the
median-character gauge, every Boolean source f satisfies

    boxed:
    R_inc(f)
      <= C_R sum_{i!=k} ||D_k D_i L^{-1/2} f||_2^2
      = C_R (I(f)-tau).                                   (5.2)

If (HR_C) holds, (5.1) immediately gives

    H(f) <= (C0+C_R) J(f) <= (C0+C_R) I(original f),

and hence proves full FEI.

This is deliberately NOT claimed proved here.  It is a materially different
bridge from fleet04/B18's rowwise near-subcube stability:

- the objects u_i are real harmonic Riesz transforms, not {0,+/-1} Boolean
  derivative rows, so the B12/B18 Boolean support-isoperimetric stability
  theorem cannot simply be imported;
- in exchange, the complete mixed-curvature matrix is exactly O(I), not a
  second spectral moment;
- the rows remain curl-free and arise from one common Boolean potential, so
  treating them as arbitrary real functions would throw away essential source
  admissibility.

The precise next mathematical task is therefore a **vector**, source-admissible
entropy/Bellman theorem for the gradient field D L^{-1/2}f, not an independent
stability theorem for each row.

# 6. Adversarial sanity checks

`verify_harmonic_riesz_curvature.py` was executed with integer Walsh
transforms and `fractions.Fraction`.

Exact pass/fail scope:

- every Boolean function through n<=4: 65,812 functions total;
- exact identities sum_i r_i=tau, e_ik=e_ki,
  sum_{i!=k}e_ik=I-tau, and ordinary depth
  sum=E[K(K-1)];
- odd majorities n=3,5,7,9,11,13, including the exact formula
  sum_i d_i=((n-1)/2)J;
- the rational inequality 4m(C(2m,m)/4^m)^2>=1 for 1<=m<=1000.

For majority n=13 the ordinary bank/J is exactly 6 and the weighted B18
depth-defect/J is about 4.9258745, while the entire harmonic bank/J is about
0.6590077.

As a falsification diagnostic only, not a theorem, the candidate ratio
R_inc/(I-tau) was also computed.  Its largest value among all n<=4 Boolean
functions was about 0.2002281.  It remained O(1) on the tested odd-majority
family through n=13 and on one-point defects through n=20 (about 1.38559 at
n=20).  These finite/family checks do not establish (5.2).

Checker SHA-256:
623a19620dd659a91f293e24910da2c7664e64d529c05af2505d22e5c2638c84

Recorded stdout SHA-256:
d16a9f2586bc9935d9dadcd8937fc7204a8b018a238247003c3ddac57d2e1036

# 7. Literature applicability check

A fresh primary-literature search found no universal FEI resolution.  The
September 18, 2026 Potapov paper proves FEI for plateaued functions (sharp
constant 4 there), not for arbitrary Boolean functions.  The May 2026
Gonzalez--MacManus--Pereyra work develops a restriction/stopping framework and
additional classes, again not a universal theorem.

For the new mechanism, Domelevo--Ivanisvili--Petermichl--Volberg
(arXiv:2606.20289, June 18, 2026) proves dimension-free L^p bounds for the
vector of Riesz transforms associated with the Walsh number operator on the
Hamming cube for p>=2 via a Bellman/two-point method.  This is technically
relevant to u_i=D_i L^{-1/2}f, but their theorem is an L^p norm estimate, not
the spectral within-level entropy inequality (5.2).  No implication to FEI is
claimed.

O'Donnell--Tan's composition theorem and Hod's lower-bound constructions
remain compatible background; nothing here supersedes them.

# 8. Before / after / remaining universal gap

BEFORE this run (fleet04/B18 interface B):
robust derivative-row restriction costs could be aggregated without an
incidence assumption, but the receiver was sum_i d_i, a second factorial
spectral moment with no O(J) payment.

AFTER:
- the exact Boolean odd-majority family proves that neither sum_i d_i nor even
  sum_i j_i delta_i can be O(J);
- harmonicizing the derivative before measuring curvature preserves exact
  mixed-derivative commutation while changing the global receiver from
  E[K(K-1)] to the exact one-charge bank I-tau;
- B13's layer-incidence residual is identified exactly as within-level
  spectral entropy of these same harmonic Riesz rows minus the log-fiber
  credit.

REMAINING UNIVERSAL IMPLICATION:
prove or refute (5.2) under the full source-admissible constraints
u_i=D_i L^{-1/2}f with f Boolean.  If false, the counterexample must be an
actual Boolean function and the next replacement must retain the curl-free
joint field rather than fall back to arbitrary real-row relaxations.

Full FEI remains OPEN / NOT PROVED.
