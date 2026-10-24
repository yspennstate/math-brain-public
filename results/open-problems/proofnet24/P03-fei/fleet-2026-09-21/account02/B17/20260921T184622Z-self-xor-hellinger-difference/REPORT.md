TASK: B17 ACCOUNT: account02 RUN: 2026-09-21T18:46:22.693099Z — self-XOR difference law, Hellinger negative credit, and the joint-correlation obstruction

MODEL: GPT-5.6 Sol (runtime self-report)
REQUESTED EFFORT: maximum actually supported
CONFIGURED/KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED by the scheduler interface
EXPOSED REASONING USAGE: null / provider reasoning tokens and thinking time NOT_EXPOSED
RESEARCH EXECUTION: WITHOUT_VERIFIED_BRAIN
STATUS: PARTIAL. Full uniform-cube Friedgut–Kalai Fourier entropy-influence conjecture remains OPEN / NOT PROVED.

Fresh authenticated control at entry: yspennstate/math-research-brain main
73eb48c1a626a410127ec6bc14c3f48973ca8a95, OWNER CONTROL revision 2026-09-21.1.
Fresh scientific source was yspennstate/math-open-problems master
20ce5fc0246dc96318599f1fbce8170bb6fe2400 and was refreshed during the run to
a6e765a1cfc60c41405060577ce86097952d55ba before delivery.

Normalization: f:F_2^n->{-1,+1}, normalized Walsh coefficients a_S=\hat f(S),
spectral law p_S=a_S^2, base-2 entropy
    H(f)=sum_S p_S log2(1/p_S),
and total influence
    I(f)=sum_S |S|p_S.
Folded influence is J(f)=sum_i min(Inf_i(f),1-Inf_i(f)).

No publication-priority or novelty claim is made. The information-theoretic sum/difference
view belongs to a substantial literature (including Tao's entropy sumset work and
Madiman–Kontoyiannis on Ruzsa divergence). The claim here is the exact FEI-facing
combination, obstruction, and replacement target recorded below, not priority.

## 0. Required comparison with the last three substantive B17 reports

The last three actual B17 reports were read before this derivation.

1. 20260921T151503Z central-cone normal form:
   arbitrary balanced FEI hardness was embedded into one-control pure cones; quadratic
   gates were proved easy. Remaining implication: find a gate invariant strong enough for
   arbitrary balanced gates.

2. 20260921T154809Z buried-atom cancellation flow:
   a strict-superset receiver-only transport was reduced to an exact congestion invariant,
   then refuted by antipodal defects with congestion >=n-1. The route pivoted to signed
   xor-cancellation partners.

3. 20260921T181122Z positive XOR-coupling obstruction:
   every genuine positive parent coupling was ruled out for a two-defect Boolean family
   even when physical simultaneous-flip overlap is zero. The replacement target was an
   influence-paid mismatch code.

FULL-PROBLEM CHANGE: **none**. FEI is still open; no finite universal constant is proved.

MECHANISM CHANGE: **yes**. This run does not continue strict-superset packing or optimize
the positive-coupling mismatch channel. It moves to the canonical self-XOR law of a
spectral sample, keeps its full joint dependence, and extracts an exact negative Hellinger
credit. Two actual Boolean families show exactly what must be retained:
odd majority kills singleton-only lateral partners, while one-point defects kill every
coordinatewise scalarization of the joint difference entropy even when all exact
all-shift Hellinger credits are kept.

FLEET_RULES moves used, deliberately different from the immediately preceding
#2/#18/#20:
- #11 DUALIZE: replace a transport on Fourier atoms by the self-XOR distribution of two
  independent spectral samples and its Hellinger affinities.
- #12 FIND WHAT IS CONSERVED: identify a character-translation-invariant functional that
  survives median-character folding exactly.
- #25 COUNT THE SAME THING TWICE: identify the self-XOR characteristic function both
  spectrally and as the square of a physical translation autocorrelation.

## 1. First actual-Boolean obstruction: singleton lateral partners can vanish identically

A tempting repair of the failed strict-superset flow is to use only signed lateral
partners across singleton Fourier shifts. Define
    A_i := sum_S |a_S a_{S xor {i}}|.

This resource can be identically zero while spectral entropy is positive.

Take odd n>=3 and the odd majority function Maj_n in {-1,+1} convention. It satisfies
    Maj_n(-x)=-Maj_n(x).
Therefore its Fourier expansion has only odd-degree sets: every even-degree Fourier
coefficient vanishes. A singleton xor toggles parity of |S|, so for every S and i at
least one of a_S and a_{S xor {i}} is zero. Hence

    boxed: A_i=0 for every i.                              (1.1)

But H(Maj_n)>0 and I(Maj_n)>0.

Thus no universal lemma that pays entropy debt only from singleton lateral affinities,
whether linearly or quadratically, can prove FEI. This is an exact Boolean obstruction,
not a relaxation counterexample and not an FEI counterexample.

The lesson is not that lateral cancellation is useless. It is that **all xor shifts and
their joint dependence have to be visible**. For odd majority, differences of two
spectral sets have even cardinality, so the missing resource is immediately present at
higher-order shifts.

## 2. The canonical self-XOR law

Let P be any probability law on G=F_2^n. Later P will be the squared Fourier law of f.
Take independent S,S'~P and define
    D=S xor S'.

Write
    c_d = Pr(D=d) = sum_s p_s p_{s xor d}.                 (2.1)

For every shift d with c_d>0 define the Hellinger affinity
    A_d(P) = sum_s sqrt(p_s p_{s xor d}).                  (2.2)

By Cauchy, 0<A_d<=1, and A_0=1.

Define the self-XOR Hellinger functional
    B(P)
      := H(D) + sum_{d:c_d>0} c_d log2 A_d(P).             (2.3)

The second term is nonpositive. It is the first negative information credit in this
route.

## 3. PROVED: universal self-XOR/Hellinger bridge

### Theorem 3.1

For every probability law P on F_2^n,

    boxed:
    H(P) <= B(P) <= H(P*P) <= 2 H(P).                     (3.1)

Moreover B is additive under direct products and invariant under translations
P(s)->P(s xor K).

### Proof of H(P)<=B(P)

Given D=d, the conditional law of S is
    q_d(s)=p_s p_{s xor d}/c_d.                            (3.2)

The map (S,S')->(S,D) is bijective, so
    2H(P)=H(D)+H(S|D).                                    (3.3)

For each d with c_d>0, Shannon entropy is at most Renyi entropy of order 1/2:
    H(q_d)
      <= 2 log2 sum_s sqrt(q_d(s))
       = 2 log2(A_d/sqrt(c_d))
       = 2 log2 A_d - log2 c_d.                           (3.4)

Average (3.4) against c_d. Since
    sum_d -c_d log2 c_d = H(D),
we get
    H(S|D) <= H(D)+2 E log2 A_D.                          (3.5)

Insert this into (3.3) and divide by two:
    H(P) <= H(D)+E log2 A_D = B(P).                       (3.6)

Because A_d<=1, B(P)<=H(D). Finally D is a deterministic function of the independent
pair (S,S'), hence H(D)<=H(S,S')=2H(P). QED.

### Product additivity

If P=P_1 x P_2 on a direct product group, then
    D=(D_1,D_2),
    H(D)=H(D_1)+H(D_2),
and
    A_(d1,d2)(P)=A_d1(P_1) A_d2(P_2).
Therefore
    boxed: B(P_1 x P_2)=B(P_1)+B(P_2).                    (3.7)

This avoids the tensor-amplification pathology of the previously refuted global l1
budgets.

### Character-translation invariance

For P^K(s)=P(s xor K), the two independent K shifts cancel in D, so c is unchanged,
and direct substitution in (2.2) shows every A_d is unchanged. Thus
    boxed: B(P^K)=B(P).                                   (3.8)

For a Boolean f, multiplying by a character translates its spectral law. Therefore B
is exactly compatible with median-character folding.

## 4. PROVED: physical translation dictionary for the entire joint law D

Now let P be the squared Fourier law of a Boolean f. For x in F_2^n define the physical
translation disagreement
    delta_f(x)=Pr_y[f(y)!=f(y xor x)].                     (4.1)

The spectral characteristic function of S is
    E[(-1)^{S dot x}]
      = sum_S p_S (-1)^{S dot x}
      = E_y f(y)f(y xor x)
      = 1-2 delta_f(x).                                   (4.2)

Because D is the xor of two independent copies,
    E[(-1)^{D dot x}]
      = (1-2 delta_f(x))^2.                               (4.3)

Hence for every physical translation x,

    boxed:
    Pr(D dot x = 1)
      = 2 delta_f(x)(1-delta_f(x)).                       (4.4)

At x=e_i this becomes
    Pr(D_i=1)
      = 2 Inf_i(f)(1-Inf_i(f)).                           (4.5)

Equation (4.4) is stronger than the coordinate marginals: the values for all x are the
full Walsh transform of c and therefore determine the entire joint law D.

This is where the new bridge meets the newest q-flip/Radon work. The B18 physical-flag
theorems pay squares and first moments of translation disagreement profiles. Here the
same physical profile determines the complete self-XOR difference law rather than only
one scalar moment.

## 5. Why keeping only coordinate marginals is fatal

Let
    alpha_i=Pr(i in S),
    r_i=Pr(D_i=1)=2 alpha_i(1-alpha_i).

Subadditivity gives
    H(D) <= sum_i h2(r_i).                                (5.1)

It is tempting to scalarize (2.3) to
    B_marg(P)
      := sum_i h2(r_i)
         + sum_d c_d log2 A_d.                            (5.2)

This keeps **every exact all-shift Hellinger credit** A_d and discards only the total
correlation of D:
    B_marg(P)-B(P)
      = TC(D)
      := sum_i h2(r_i)-H(D) >= 0.                         (5.3)

A dimension-independent bound B_marg<=C I would be a very attractive FEI bridge.
It is false on an exact Boolean family.

## 6. PROVED counterexample to the scalarized bridge: one-point defects

For n>=3 let N=2^n and
    f_n(x)=1-2 1_{x=0}.                                   (6.1)

Its normalized Walsh coefficients are
    a_0=(N-2)/N,
    a_s=-2/N  for s!=0.                                   (6.2)

Thus
    p_0=(N-2)^2/N^2,
    p_s=4/N^2  (s!=0),                                    (6.3)
and every coordinate has
    alpha_i=2/N,
    I(f_n)=2n/N.                                          (6.4)

For every nonzero d, direct convolution gives
    c_d = c_* := 8(N-2)/N^3,                              (6.5)
so with
    R=(N-1)c_* = Pr(D!=0),                                (6.6)
the conditional nonzero difference is uniform.

The Hellinger affinity is also constant on nonzero shifts:
    A_d=A_*:=8(N-2)/N^2  (d!=0).                          (6.7)

Therefore the **joint** bridge is exactly
    B(P_n)
      = h2(R)+R log2((N-1)A_*).                           (6.8)

Meanwhile each difference bit has
    rho:=Pr(D_i=1)=4(N-2)/N^2,                            (6.9)
and the scalarized bridge is exactly
    B_marg(P_n)
      = n h2(rho)+R log2 A_*.                             (6.10)

Using h2(t)=t log2(1/t)+O(t) as t->0,
    R=8/N+O(N^-2),
    rho=4/N+O(N^-2),
    log2 A_* = -n+3+o(1).

Hence
    B(P_n)=8n/N+O(1/N),                                   (6.11)
    B_marg(P_n)=4n^2/N+O(n/N).                            (6.12)

Divide by I(f_n)=2n/N:

    boxed:
    B(P_n)/I(f_n) -> 4,                                   (6.13)

but

    boxed:
    B_marg(P_n)/I(f_n) = 2n+O(1) -> infinity.             (6.14)

The original FEI ratio also satisfies H(f_n)/I(f_n)->4, so the full joint bridge is
asymptotically tight on this adversarial Boolean family while the coordinatewise
scalarization loses an unbounded factor.

This is not an FEI counterexample. It refutes the stronger lemma that the all-shift
Hellinger credits can compensate for replacing the joint self-XOR entropy by the sum of
its one-coordinate entropies.

### Exact obstruction

The missing quantity is not another local phase payment. It is precisely

    TC(D)=sum_i h2(r_i)-H(D),                              (6.15)

the total correlation of the entire spectral-difference vector. For the one-point
defect, TC(D) carries the leading n^2/N scalar excess.

This is a different obstruction from the last run's positive-coupling mismatch:
there is no optimized external coupling here. D is the canonical iid self-XOR, and the
loss occurs only when its joint dependence is destroyed.

## 7. Replacement FEI target: a signable joint-difference inequality

For Boolean spectra define the optimal constant C_B by the target

    B(P_f) <= C_B J(f)                                    (7.1)

after character folding.

Because B is character-translation invariant, fold every coordinate with
Inf_i(f)>1/2 so the translated Boolean function has I=J while H and B are unchanged.
Then (3.1) gives immediately:

- If (7.1) holds with finite C_B for all Boolean f, then
      H(f)<=B(P_f)<=C_B J(f)<=C_B I(f),
  so full FEI follows.

- Conversely, if FEI holds with constant C, apply it to the folded character translate:
      H(f)<=C J(f).
  Since B(P_f)<=2H(f),
      B(P_f)<=2C J(f).

Therefore, for optimal constants,

    boxed:
    C_FEI <= C_B <= 2 C_FEI.                              (7.2)

So (7.1) is **equivalent to FEI at the level of finiteness**, with at most a factor-two
constant loss. Unlike the killed global l1 budget it is tensor-additive; unlike
singleton partner payment it sees every xor shift; unlike the scalarized q-flip bound it
retains the full joint translation bank.

The Boolean constraint is still essential. Arbitrary probability laws on F_2^n can
have B(P)/E|S| growing with n. The replacement target is only for squared spectra of
actual Boolean functions, equivalently the signable laws satisfying the full Boolean
signed-autocorrelation equations inherited from f^2=1. A non-Boolean failure would not
refute FEI.

## 8. Interface with the current primitive-core and Radon work

The newest B14 critical-core report uses TC(X), the total correlation of the original
spectral sample, as part of its restriction slack. The quantity here is different:
TC(D) is the total correlation of the **difference of two independent spectral
samples**.

The newest B18 physical flag/Radon theorem proves exact square-to-linear payment for
physical translation disagreement profiles. Equation (4.4) shows that those profiles
are exactly the parity marginals of D. This suggests a concrete nonduplicative next step:

> JOINT RADON TARGET. Bound B(P_f) by O(J(f)) using a multiscale family of physical
> translations x that reconstructs enough of the joint law D to retain TC(D), while the
> Hellinger term supplies the negative local overlap credit.

A proof cannot replace D by independent coordinate bits: Section 6 rules that out.
Nor can it use only singleton translations: Section 1 rules that out. The next compiler
must preserve at least enough higher-order translation information to capture the
one-point-defect correlation collapse and the even-parity constraint of odd majority.

This is materially different from another mismatch-code optimization.

## 9. Finite sanity check

`verify_self_xor_hellinger_bridge.py` was executed.

Exact arithmetic checks:
- 1,060 physical-translation identities (4.4) across every Boolean function through n=3
  modulo global sign;
- exact singleton-affinity vanishing for majority at n=3,5,7;
- exact one-point-defect spectral/convolution/affinity formulas through n=7, with closed
  forms evaluated through n=12.

Finite numerical entropy checks:
- H(P)<=B(P) on 138 Boolean functions through n=3 modulo global sign.

The checker records, for the one-point defects:
- n=4: H/I=3.4024755512, B/I=4.1796944091, B_marg/I=5.0846860348;
- n=7: H/I=3.8043570698, B/I=4.6868232917, B_marg/I=10.4395426179;
- n=12: H/I=3.9060445667, B/I=4.4771477281, B_marg/I=19.8761783572.

Finite checks establish only their stated implementation scope. Theorems 3.1, 4.4,
6.13–6.14, and the structural statements above are analytic.

Checker SHA-256:
32dd0c7ada4baab34006692080a742eeb820e8adae9cc4391810bd1117f1104e

Recorded stdout SHA-256:
47d165d1b42e40be11f5f1607710d0467dae72fd00c1e844eda9f792cdbeb362

An unrelated spreadsheet-runtime warmup warning appeared on Python startup, but the
checker itself exited 0 and its stdout is the recorded verification artifact.

## 10. Literature/applicability check

Current primary FEI literature was checked before claiming scope:
- O'Donnell–Tan, arXiv:1304.1347, composition theorem: relevant to recursive/product
  stability, but it does not provide the self-XOR/Hellinger target (7.1).
- González–MacManus–Pereyra, arXiv:2606.00246 (29 May 2026): restriction/stopping
  framework; full FEI remains conditional there.
- Potapov, arXiv:2609.21563 (18 Sep 2026): FEI for plateaued functions with sharp class
  constant 4 and partially bent functions with sharp class constant 2; it does not cover
  arbitrary Boolean self-XOR laws.
- Tao, arXiv:0906.4387, and Madiman–Kontoyiannis, arXiv:1508.04089: entropy
  sum/difference and Ruzsa-divergence framework, relevant background for using H(S xor
  S') and entropy growth. No claim is made that the generic entropy-of-sums viewpoint is
  new.

I did not locate an explicit published statement of functional (2.3) in this FEI form in
the bounded search. Absence from that search is not a novelty certificate.

## 11. Before / after / remaining universal implication

BEFORE:
- strict-superset receiver-only transport: refuted;
- singleton signed partners: proposed as a repair but not yet tested at full quantifier;
- positive XOR coupling: refuted, leaving an influence-paid mismatch code;
- full FEI: OPEN.

AFTER:
- singleton-only lateral payment is refuted by actual odd-majority Boolean functions;
- the self-XOR/Hellinger functional B is proved to sandwich H and to be character
  invariant and tensor additive;
- its full joint law has an exact physical-translation dictionary;
- coordinatewise scalarization is refuted with unbounded ratio by actual one-point
  Boolean defects even while keeping every exact all-shift Hellinger credit;
- preserving TC(D) repairs that family sharply: B/I->4 while B_marg/I->infinity;
- a new joint Radon/Hellinger target (7.1) is equivalent to FEI at the level of existence
  of a finite universal constant, up to factor two.

REMAINING UNIVERSAL IMPLICATION:
prove a finite C_B in
    B(P_f) <= C_B J(f)
for every Boolean f, using the full joint physical translation/Radon bank rather than
coordinate marginals, or produce an actual Boolean family showing C_B is unbounded.
Either outcome is decisive for this mechanism.

Full FEI remains OPEN / NOT PROVED.
