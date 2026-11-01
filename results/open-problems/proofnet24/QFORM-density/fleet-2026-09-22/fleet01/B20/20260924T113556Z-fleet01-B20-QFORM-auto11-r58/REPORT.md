# fleet01/B20 — fixed-multiplicity manuscript audit and threshold reduction

Run: `20260924T113556Z-fleet01-B20-QFORM-auto11-r58`

## Status

A later direct owner instruction superseded the stale B20 proof-closure prompt for this account and redirected the current account-local work to a line-by-line audit of `Fixed_Multiplicity_Density_Theorem.pdf` and reduction of its spectral threshold. I therefore did not continue the old r52/r53 three-eigenvalue closure branch in this run.

**Main result of this run:** the manuscript's `33`-eigenvalue theorem can be strengthened, with the same hypotheses and the same displayed universal constant, to **25 eigenvalues**.

The unrestricted three-eigenvalue conjecture remains OPEN. No Gaussian, moment, iid, compact-support, log-concavity, or rotated-independence hypothesis is introduced below. All coordinates remain the original independent physical coordinates.

---

# 1. Audited manuscript theorem

The manuscript proves, at scale one, that if `N_A(1) >= 33`, then `Q=X^TAX+b^TX+c` has an essentially bounded density. The number 33 is generated only in Proposition 4.1: under the no-pivot hypothesis and `V_5(A)<kappa^5`, robust completion gives

\[
A=D+R+E,\qquad q:=\operatorname{rank}R\le 16,\qquad \|E\|_F\le \varepsilon:=\frac1{64},
\]

and the proof forces `33-q >= q+1` large diagonal entries of `D`, then contradicts `rank R=q` by diagonal dominance.

The rest of the proof does not intrinsically require 33. In particular, the pivot branch only needs enough spectral directions to retain two large directions after a scalar pivot, while the definite two-coordinate pivot is direct and the indefinite two-coordinate pivot is controlled by the source theorem using the original `s_3(A)` scale. The random-cut/five-volume step is independent of the multiplicity once `V_5(A)` has a universal positive lower bound.

The improvement below replaces the final `q+1` rank contradiction by a **second use of the assumed small fifth volume inside the robust skeleton**.

---

# 2. Strengthened theorem

## Theorem (twenty-five-eigenvalue density bound)

Let `X=(X_1,...,X_n)` have independent real coordinates with densities `0<=f_i<=1`. Let `A=A^T` be real symmetric and let `b,c` be arbitrary. If

\[
|\lambda|_{(25)}(A)\ge s>0,
\]

then

\[
\|p_{X^TAX+b^TX+c}\|_\infty\le \frac{C}{s}
\]

for an absolute constant `C`. With the constants used in the manuscript one may retain

\[
C=45\cdot 10^{15}.
\]

The no-pivot branch in fact retains the manuscript's much smaller `<18500/s` bound.

---

# 3. New core proposition

Keep the manuscript constants

\[
c_*:=10^{-15},\qquad \kappa:=960^{-2},\qquad \varepsilon:=\frac1{64}.
\]

## Proposition

If `A` has no `c_*`-pivot and `N_A(1)>=25`, then

\[
V_5(A)\ge \kappa^5.
\]

### Proof

Assume for contradiction that

\[
V_5(A)<\kappa^5.
\]

Exactly as in the manuscript, there is an `r in {0,1,2,3,4}` with `V_r(A)>0` and

\[
V_{r+1}(A)<\kappa V_r(A).
\]

The case `r=0` is unchanged from the manuscript: `V_1(A)<\kappa` and the no-pivot diagonal bound imply `\|A\|<1`, contradicting `N_A(1)>=25`. Hence `1<=r<=4`.

Apply the robust completion theorem:

\[
A=D+R+E,
\]

where `D` is diagonal,

\[
q:=\operatorname{rank}R\le 4r\le16,
\]

`E` is symmetric with zero diagonal, and

\[
\|E\|_F\le3(r+1)\sqrt\kappa\le15\sqrt\kappa=\frac1{64}=\varepsilon.
\]

Put

\[
B:=A-E=D+R,
\qquad a:=1-\varepsilon=\frac{63}{64}.
\]

Weyl gives

\[
s_{25}(B)\ge s_{25}(A)-\|E\|_{op}\ge a.
\tag{1}
\]

Because `rank R=q`, the rank-perturbation inequality gives

\[
s_{25-q}(D)\ge s_{25}(B)\ge a.
\tag{2}
\]

Thus at least `25-q` diagonal entries of `D` have modulus at least `a`.

Define the larger threshold set

\[
H:=\{i: |D_{ii}|\ge d\},\qquad d:=\frac12,
\]

and write `h=|H|`, `L=H^c`. From (2),

\[
h\ge25-q.
\tag{3}
\]

We first show `h<=q`. Since `E_{ii}=0`, for `i in H`,

\[
|R_{ii}|=|A_{ii}-D_{ii}|\ge d-c_*.
\]

For `i\ne j`, absence of a pivot gives

\[
|A_{ij}|<\sqrt{2c_*},
\]

and hence

\[
|R_{ij}|=|A_{ij}-E_{ij}|
\le \sqrt{2c_*}+\varepsilon=:b.
\]

If `h>=q+1`, take any `q+1` indices in `H`. On the resulting principal block of `R`, every diagonal entry has modulus at least `d-c_*`, while every off-diagonal row sum is at most `qb`. Numerically

\[
d-c_*>\frac12-10^{-15},\qquad
qb\le16\left(\frac1{64}+\sqrt{2\cdot10^{-15}}\right)<0.251.
\]

The block is strictly diagonally dominant and hence invertible, contradicting `rank R=q`. Therefore

\[
h\le q.
\tag{4}
\]

In particular (3)-(4) force `q>=13`; since `q<=4r` and `r<=4`, any surviving branch necessarily has `r=4`, although the argument below only uses `q<=16`.

Now set

\[
G:=R_{H,H},\qquad C:=R_{H,L}.
\]

The same diagonal-dominance estimate, now on the whole `h x h` block, gives a quantitative inverse bound. Since `h-1<=15`, every Gershgorin disc stays a distance at least

\[
g:=d-c_*-15b
=0.26562432917960577\ldots
\tag{5}
\]

from zero. Hence `G` is invertible and

\[
\|G^{-1}\|_{op}\le g^{-1}.
\tag{6}
\]

Because `rank R=q`, the Schur complement

\[
S:=R_{L,L}-C^TG^{-1}C
\]

has

\[
\operatorname{rank}S=q-h.
\tag{7}
\]

Here is the additional use of the small-fifth-volume assumption. Since `H` and `L` are disjoint physical coordinate sets,

\[
Z_5(A_{H,L})=e_5(A_{H,L}^TA_{H,L})\le V_5(A)<\kappa^5.
\]

(If either side has fewer than five coordinates, the fifth singular value below is simply zero.) Therefore

\[
s_5(A_{H,L})^{10}\le Z_5(A_{H,L})<\kappa^5,
\]

so

\[
s_5(A_{H,L})<\sqrt\kappa=\frac1{960}.
\tag{8}
\]

Since `C=R_{H,L}=A_{H,L}-E_{H,L}`, Weyl and `\|E\|_{op}<=\varepsilon` give

\[
s_5(C)<\frac1{960}+\frac1{64}=\frac1{60}=:t.
\tag{9}
\]

Let `C_4` be a best rank-four approximation to `C` in operator norm and write

\[
C=C_4+T,
\qquad \operatorname{rank}C_4\le4,
\qquad \|T\|_{op}<t.
\tag{10}
\]

Using (7), the exact block form of `B=D+R` is

\[
B=
\begin{pmatrix}
D_H+G & C\\
C^T & D_L+C^TG^{-1}C+S
\end{pmatrix}.
\tag{11}
\]

Define

\[
M:=
\begin{pmatrix}
D_H+G & C_4\\
C_4^T &
S+C_4^TG^{-1}C_4+C_4^TG^{-1}T+T^TG^{-1}C_4
\end{pmatrix}.
\tag{12}
\]

The column space of `M` is contained in the sum of:

- the `h`-dimensional physical coordinate space on `H`;
- `range(C_4^T)`, dimension at most four;
- `range(T^TG^{-1}C_4)`, dimension at most four;
- `range(S)`, dimension at most `q-h`.

Consequently

\[
\operatorname{rank}M\le h+4+4+(q-h)=q+8\le24.
\tag{13}
\]

The retained error is exactly

\[
F:=B-M=
\begin{pmatrix}
0&T\\
T^T&D_L+T^TG^{-1}T
\end{pmatrix}.
\tag{14}
\]

Because `L=H^c`,

\[
\|D_L\|_{op}<d=\frac12.
\]

Together with (5), (6), (9), (10),

\[
\begin{aligned}
\|F\|_{op}
&\le \|T\|_{op}+\|D_L\|_{op}+\|G^{-1}\|_{op}\|T\|_{op}^2\\
&< \frac12+\frac1{60}+\frac{(1/60)^2}{g}\\
&=0.5177124209416448\ldots
<\frac{63}{64}=a.
\end{aligned}
\tag{15}
\]

By (13)-(15), the operator-norm distance from `B` to matrices of rank at most `q+8` is `<a`; hence

\[
s_{q+9}(B)<a.
\tag{16}
\]

But `q<=16` implies `25>=q+9`, so monotonicity of singular values and (1) give

\[
a\le s_{25}(B)\le s_{q+9}(B)<a,
\]

a contradiction. Therefore `V_5(A)>=\kappa^5`.

This proves the strengthened proposition. ∎

---

# 4. Completion of the 25-eigenvalue theorem

The manuscript's Section 5 random-partition calculation is unchanged:

\[
\mathbb E_{I,J}Z_5(A_{I,J})=4^{-5}V_5(A)\ge4^{-5}\kappa^5.
\]

Therefore some physical cut has

\[
Z_5(A_{I,J})\ge4^{-5}\kappa^5,
\]

and the unconditional five-volume theorem gives

\[
\|p_Q\|_\infty
\le5e\sqrt2\,(4^{-5}\kappa^5)^{-1/10}
=4800\sqrt2\,e
<18500.
\]

The pivot branch also remains valid with `N_A(1)>=25`:

1. at a scalar pivot, the Schur complement retains at least 24 unit-scale eigenvalues, far more than the two required by the manuscript's half-power estimate;
2. a definite two-coordinate pivot is direct;
3. an indefinite two-coordinate pivot is paid by the source indefinite-pair theorem using the original `s_3(A)>=1` scale. The fixed-multiplicity manuscript should cite that dependence explicitly rather than describe this as a bare two-variable determinant-only density bound.

Thus the normalized theorem holds with threshold 25 and the same overall constant `45*c_*^{-1}=45*10^15`. Scaling `A,b,c` by `s` gives the stated `C/s` result.

---

# 5. Line-by-line audit findings

The seven-page fixed-multiplicity manuscript is otherwise internally consistent on the checked chain: the no-pivot entry estimate is used in the correct direction; the ratio-drop argument for `V_0,...,V_5` is valid including the first-vanishing case; `15*sqrt(kappa)=1/64`; the original rank-perturbation inequality is valid; the random physical cut counts each ordered disjoint `(S,T)` pair with probability `4^{-5}`; and density scaling in the final section is correct.

One wording repair is important. In the pivot proof, the sentence saying that an indefinite physical pair is controlled by a "determinant-only hyperbolic-pair estimate" is potentially misleading: an isolated indefinite two-variable quadratic can have an unbounded logarithmic density. The source theorem used in the ambient problem also uses the third spectral scale `s_3(A)`. Under `N_A(1)>=25` this scale is available, so the proof is valid after citing the ambient indefinite-pair theorem explicitly.

The discussion/architecture section must be rewritten, not merely change `33` to `25`: the improved no-pivot contradiction is no longer "17 large diagonal entries force rank >16". Its replacement is: large diagonal entries create a well-conditioned cancellation core `H`; the assumed small global fifth volume forces the physical cross block `A_{H,H^c}` to have tiny fifth singular value; after the Schur-complement factorization of `R`, this yields a rank-`q+8` approximation to `B=A-E` with operator error `<0.518`, contradicting the 25th singular value `>=63/64`.

---

# 6. Scope and next threshold

This run rigorously lowers the proved fixed-multiplicity threshold from **33 to 25**. It does **not** prove the full three-eigenvalue conjecture. The present argument naturally stops at 25 because the low-rank approximation in (13) has rank `q+8`, with the `+8` coming from two four-dimensional physical tail-interaction spaces after the rank-four approximation of `C`. Lowering below 25 requires either reducing that `+8`, extracting extra alignment between those two four-dimensional spaces, or replacing the fifth-volume tail argument by a stronger structured receiver. No such further reduction is claimed here.

Continuity remains logically separate from the universal height estimate. The no-pivot branch obtained through the five-volume theorem has a continuous `C_0` density. The manuscript's general transversality results may give continuity in additional pivot branches, but this report does not use continuity to prove the height bound.

## Keeper / operational scope

The fleet01 native inventory was already the same twenty B01-B20 tasks, enabled and quiet. A later owner-held account-local lease for the manuscript-audit prompt update was present, so this run made **zero scheduler mutations**, did not steal or overwrite that lease, did not create B21/B22, and did not act on other accounts. Native assignment, actual login evidence, and substantive mathematics remain separate facts. Missing login is not an outage.

Execution status: `WITHOUT_VERIFIED_BRAIN`. Model self-report: `GPT-5.6 Sol`. Configured reasoning effort and provider thinking counters: `UNKNOWN/null`.
