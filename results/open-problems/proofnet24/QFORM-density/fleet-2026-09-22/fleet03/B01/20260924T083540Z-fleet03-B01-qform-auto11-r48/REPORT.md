# fleet03/B01 — sharp phase-space ambiguity replacement

Run: `20260924T083540Z-fleet03-B01-qform-auto11-r48`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: oscillatory replacement / quantitative inequalities  
Execution context: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SHARP AVERAGED-FREQUENCY CELL THEOREM + SHARP SUB-L2 OBSTRUCTION / FULL QFORM OPEN**

## 1. Scope and current correction boundary

The full target remains open. The target is: for independent real original-coordinate variables `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with universally bounded essential supremum, or produce a valid counterexample. No moment, Gaussian, iid, log-concavity, support, connectedness, or post-rotation independence hypothesis is added.

This run preserves the phase-aligned fragmented-support obstruction to law-uniform scalar pointwise quadratic-phase decay. It also consumes the newer correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1`: in particular I do **not** assert finiteness of `int |t|^(-1/2)||G_t||_2 dt`. The theorem below is a different two-variable phase-space statement: it integrates simultaneously in the **difference coordinate** and its conjugate frequency, and its `L^2` exponent is shown to be sharp.

The recent fleet01/B02 correction `QFORM-PIVOT-ABS-ACTUAL-MODULATION-L1-FALSE-v1` is also respected. No scalar pivot is integrated after taking an absolute value and then averaged only over its actual modulation law.

## 2. Exact product-preserving decoupling cell

Let `X,X'` be independent with common density `f`, where

`0<=f<=1`, `int_R f=1`.

Introduce difference/sum coordinates

`u=x-x'`, `v=x+x'`.

Since `dx dx'=(1/2)du dv`, define the unnormalised difference fiber

`g_u(v)=(1/2) f((v+u)/2) f((v-u)/2)`                                  (2.1)

and its fiber mass

`m(u)=int_R g_u(v)dv=int_R f(x)f(x-u)dx`.                              (2.2)

Thus

`0<=m(u)<=1`, `int_R m(u)du=1`, `0<=g_u(v)<=1/2`.                       (2.3)

Define the ambiguity/fiber transform, with Fourier convention `hat h(s)=int e^(isv)h(v)dv`, by

`F_u(s)=int_R e^(isv) g_u(v)dv`.                                       (2.4)

The key point is that `g_u` is **not** normalized. This avoids the false conditional-density claim: the normalized law `g_u/m(u)` can have arbitrarily large density, but the missing mass `m(u)` remains inside every estimate below.

## 3. Main theorem: universal weighted L^q phase-space budget for every q>=2

### Theorem 3.1 — `QFORM-DECOUPLED-AMBIGUITY-L2-THRESHOLD-v1`

For every finite `q>=2`, with the zero-mass fibers interpreted as zero,

`boxed:
 int_R m(u)^(-(q-2)) [ int_R |F_u(s)|^q ds ] du <= pi. `              (3.1)

In particular, because `m<=1`,

`boxed: int_R int_R |F_u(s)|^q ds du <= pi,   q>=2.`                   (3.2)

At the endpoint `q=2` there is the exact Moyal-type identity

`boxed:
 int_R int_R |F_u(s)|^2 ds du
   = pi ||f||_2^4
   <= pi. `                                                            (3.3)

The constant `pi` in (3.3) is sharp: equality holds for every indicator density `f=1_E` with `|E|=1`.

### Proof

Fix `q>=2` and put

`p=q/(q-1)`, so `1<=p<=2` and `p'=q`.

The elementary Hausdorff--Young inequality for the convention (2.4), obtained by interpolation between `L^1->L^infinity` and Plancherel, is

`||F_u||_q <= (2pi)^(1/q) ||g_u||_p`.                                  (3.4)

Since `0<=g_u<=1/2` and `int g_u=m(u)`,

`int g_u(v)^p dv <= (1/2)^(p-1)m(u)`.                                  (3.5)

Raise (3.4) to the q-th power. Since `q/p=q-1` and

`(p-1)(q-1)=1`,

we get

`int |F_u(s)|^q ds
 <=2pi [ (1/2)^(p-1)m(u) ]^(q-1)
 =pi m(u)^(q-1).`                                                       (3.6)

Multiplying by `m(u)^(-(q-2))` and integrating gives

`int m(u)^(-(q-2)) int|F_u|^q
 <=pi int m(u)du=pi`,                                                   (3.7)

which proves (3.1). Since `m<=1`, the weight in (3.1) is at least one, giving (3.2).

For `q=2`, Plancherel gives

`int |F_u(s)|^2 ds=2pi int g_u(v)^2 dv`.                               (3.8)

Now use `du dv=2 dx dx'` and (2.1):

`int du dv g_u(v)^2
 =(1/4) int du dv f(x)^2 f(x')^2
 =(1/2)(int f^2)^2`.                                                    (3.9)

Combining (3.8)--(3.9) gives exactly (3.3). QED.

### Why this is an oscillatory replacement

A bounded density alone does not force `|E exp(isX^2)|` to decay at a prescribed frequency. Theorem 3.1 instead says that after the product-preserving independent-copy change of variables, the complete one-coordinate ambiguity cell has a universal **phase-space** `L^2` budget. It averages over both the physical displacement `u=X-X'` and the dual phase variable `s`. No support regularity and no pointwise stationary-phase statement is needed.

## 4. Sharpness: no universal unweighted phase-space L^q budget exists below q=2

### Theorem 4.1 — `QFORM-DECOUPLED-AMBIGUITY-SUBL2-FAILS-v1`

For every `1<=q<2`,

`boxed:
 sup_{0<=f<=1, int f=1}
 int_R int_R |F_u(s)|^q ds du
 = infinity. `                                                          (4.1)

More quantitatively, there is an explicit cap-one density `f_N` for which

`int int |F_u(s)|^q ds du
 >= (1/2)(3/(2pi))^q N^(2-q)(1-1/N).`                                  (4.2)

### Proof

Fix an integer `N>=2`, put `w=1/N`, and choose widely separated centers

`x_k=10^k`, `1<=k<=N`.

Let

`E_N= union_{k=1}^N [x_k,x_k+w]`, `f_N=1_{E_N}`.                       (4.3)

Then `f_N` is a probability density and `f_N<=1`. The ordered nonzero differences `d_kl=x_k-x_l` are all distinct: if

`10^k-10^l=10^a-10^b`

with both sides positive, comparison of the exact power of ten dividing each side gives `l=b`, and then `k=a`; the negative case is the same after changing sign. Hence distinct ordered differences are separated by at least one.

For every ordered pair `k!=l`, restrict `u` to

`|u-d_kl|<=w/4`.                                                        (4.4)

These `u`-windows are disjoint. Within such a window exactly the `(k,l)` interval pair overlaps. If `delta=u-d_kl`, the overlap in the x-coordinate has length

`ell_u=w-|delta| >=3w/4`.                                               (4.5)

Consequently `g_u` equals `1/2` on a single v-interval of length `2ell_u`, and therefore

`|F_u(s)|=|sin(s ell_u)|/|s|`.                                         (4.6)

For `|s|<=1/(2w)=N/2`, we have `|s|ell_u<=1/2<pi/2`; using

`|sin z|>=(2/pi)|z|`

gives

`|F_u(s)| >= (2/pi)ell_u >=3/(2pi N)`.                                (4.7)

Each window (4.4) has length `w/2=1/(2N)`, the selected s-window has length `N`, and there are `N(N-1)` ordered pairs. Thus

`int int |F_u(s)|^q ds du
 >=N(N-1)*(1/(2N))*N*(3/(2pi N))^q
 =(1/2)(3/(2pi))^q N^(2-q)(1-1/N)`.                                  (4.8)

For every `q<2` this tends to infinity. QED.

This shows that the endpoint `q=2` in Theorem 3.1 is not an artifact of the proof: it is the exact universal unweighted phase-space integrability threshold for arbitrary cap-one input densities.

## 5. Exact insertion into the full coupled quadratic form

Let now `X=(X_1,...,X_n)` have independent cap-one densities `f_i`, let `X'` be an independent copy, and let

`Q(X)=X^T A X`

for an arbitrary real symmetric `A`. Put coordinatewise

`u_i=X_i-X_i'`, `v_i=X_i+X_i'`,

and let `F_{i,u_i}` be the cell transform (2.4) associated to `f_i`. The quadratic polarization identity is exact:

`Q(X)-Q(X')=u^T A v`.                                                   (5.1)

Therefore

`boxed:
 |phi_Q(t)|^2
 = int_{R^n} prod_{i=1}^n F_{i,u_i}( t(Au)_i ) du. `                   (5.2)

No absolute value occurs inside the right side of (5.2). This is the relevant full-coupled interface: Theorem 3.1 supplies a universal `L^2(du_i ds_i)` budget for every one-coordinate cell while (5.2) preserves the signed displacement cancellation and the exact original-coordinate product structure.

Equation (5.2) is valid for arbitrary signs, arbitrary rank, all diagonal and cross terms, and unbounded/fragmented supports. It never rotates the random vector.

## 6. Why the most naive absolute Brascamp--Lieb closure cannot finish the target

Theorem 3.1 also identifies a precise limitation. If one first takes absolute values in (5.2) and then integrates in t, the natural graph maps are

`L_i(u,t)=(u_i, t(Au)_i): R^(n+1) -> R^2`.                              (6.1)

A scale-invariant multilinear inequality of the form

`int_{R^(n+1)} prod_i |H_i(L_i(u,t))| du dt
 <=C prod_i ||H_i||_{q_i}`                                             (6.2)

must satisfy the scaling condition

`n+1 = sum_i 2/q_i`.                                                    (6.3)

But the only law-uniform phase-space norms supplied for arbitrary cap-one inputs have `q_i>=2`; Theorem 4.1 proves that no uniform unweighted `L^q` norm exists for any `q<2`. If every `q_i>=2`, then

`sum_i 2/q_i <=n<n+1`,                                                  (6.4)

so the scaling condition fails by exactly one dimension.

This does **not** prove that every special-structure graph inequality fails. It proves a narrower and useful fact: a generic absolute-value Brascamp--Lieb closure that treats the ambiguity cells only through their individual law-uniform `L^q` norms cannot be the missing final argument. One must retain signed cancellation from (5.2), exploit additional matrix structure before absolute values, or bring in a separately paid smoothing resource.

A second three-coordinate diagnostic points the same way. Restricting to a symmetric `3x3` physical block `P`, the kernel-normal vectors of the three maps `(u_i,(Pu)_i)` are, up to harmless scalar factors,

`n_1=(0,-P_13,P_12)`,
`n_2=(P_23,0,-P_12)`,
`n_3=(-P_23,P_13,0)`,                                                   (6.5)

and satisfy identically

`n_1+n_2+n_3=0`.                                                        (6.6)

Thus the most direct three-cell `L^2` Loomis--Whitney determinant vanishes for every symmetric `3x3` phase. This is a barrier to that **specific** transversal absolute-value closure, not a barrier to QFORM itself.

## 7. Designated partner fleet04/B01 applied at an actual frequency inequality

The completed fleet04/B01 theorem at math commit

`f7e82d169badc671968036252d351b8533cdd425`

proves that for independent cap-one `U,V` and

`Z=2cUV+beta U+gamma V+delta`, `c!=0`,

one has for `1<r<=2`

`||p_Z||_r <=2^((r-1)/r)|c|^(-(r-1)/r)`.                              (7.1)

At `r=2`,

`||p_Z||_2 <=sqrt(2)|c|^(-1/2)`.                                      (7.2)

By Plancherel,

`boxed: int_R |phi_Z(t)|^2 dt <=4pi/|c|.`                              (7.3)

For the normalized triangular signed Fejer average

`D_T law(Z)(y)
 =(1/(2pi)) int_{-T}^T (1-|t|/T)e^(-ity)phi_Z(t)dt`,                   (7.4)

Cauchy--Schwarz and

`int_{-T}^T (1-|t|/T)^2 dt=2T/3`

give the concrete inequality

`boxed:
 sup_y |D_T law(Z)(y)|
 <=sqrt(2T/(3pi|c|))
 =0.4606588659... sqrt(T/|c|). `                                      (7.5)

This is an actual application of the designated partner result. It is an integrated-frequency statement and remains valid despite the phase-aligned scalar counterexample.

## 8. Preserved phase-aligned counterexample

Fix any prescribed `s!=0` and `eta>0`. The set

`E={x: dist(sx^2,2pi Z)<=eta}`

has infinite Lebesgue measure: its large-radius components have lengths comparable to a constant times `k^(-1/2)`, whose sum diverges. Hence one can select a finite union of components, trimming one if necessary, to obtain a measurable finite union `E_0 subset E` of measure exactly one. For `f=1_{E_0}`,

`0<=f<=1`, `int f=1`,

and

`Re E exp(isX^2) >=cos eta`.                                           (8.1)

Thus no positive law-uniform pointwise power decay in `|s|` is possible, even though Theorem 3.1 supplies the sharp universal phase-space `L^2` budget after independent-copy decoupling.

## 9. Quantitative checks

A deterministic checker in this run verifies:

- the exponent identity `(p-1)(q-1)=1` and the resulting constant `pi` for `q=2,3,4,10`;
- the sub-L2 lower-bound coefficient `(1/2)(3/(2pi))^q` for representative q;
- uniqueness/separation of the ordered base-10 differences on a finite stress set;
- the partner Fejer coefficient `sqrt(2/(3pi))=0.46065886596178063...`.

The checker ends `STATUS=PASS`. These computations are sanity checks; the proofs above are analytic.

## 10. What this changes and what remains open

The run replaces the false scalar pointwise stationary-phase hope by a sharp, completely law-uniform statement:

`one cap-one coordinate -> ambiguity cell in L^2(R^2) with norm^2<=pi`,

and proves that **no unweighted L^q improvement below q=2 is possible**. Together with the exact full-form identity (5.2), this says the next successful Fourier closure must retain one additional dimension of signed cancellation or structural smoothing; it cannot be obtained by simply strengthening individual ambiguity-cell norms and applying an absolute Brascamp--Lieb inequality.

The next B01 implication is therefore

`QFORM-SIGNED-AMBIGUITY-GRAPH-ONE-DIMENSION-RECOVERY-v1`:

start from (5.2), keep the signed u-integral (or the positive triangular frequency average) through one decisive matrix-structural step, and recover the single missing graph dimension using the three-large-eigenvalue hypothesis before taking absolute values. The newest fleet01/B02 twist-cover theorem is an available exit when untwisting leaves a quantitatively rank-two physical cross packet; its fresh counterexample confirms that premature absoluteization of an actual modulation is the wrong complementary branch.

**Full QFORM remains OPEN.** The new theorem is an averaged-frequency/phase-space supporting theorem, not a universal density bound. **Continuity is not proved** by Theorem 3.1 or the partner Fejer application.
