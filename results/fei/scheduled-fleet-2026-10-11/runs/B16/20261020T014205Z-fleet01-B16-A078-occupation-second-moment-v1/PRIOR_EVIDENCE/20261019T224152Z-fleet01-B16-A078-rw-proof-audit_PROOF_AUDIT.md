# B16 / A078 — independent algebraic audit of the corrected random-walk tail proof

**Run:** `20261019T224152Z-fleet01-B16-A078-rw-proof-audit`  
**Primary packet:** A078 — coding and padding  
**Stable gap:** `G-A078-BOOLEAN-CODING-PADDING`  
**Status:** B16 self-audit only; not an independent end-to-end review and not adoption.  
**Scope:** universal GU only.

## Frozen target and candidate

The target is a single absolute pair `a >= 0`, `0 <= b < 1` for which `G(f) <= a I(f) + b U(f)` holds for every genuine Boolean sign on every finite uniform cube. The candidate is the median-threshold triangular bijection

\[
\phi_n(t)_j=t_j\oplus\mathbf1\{|t_{j+1:n}|>\lfloor(n-j)/2\rfloor\},\quad j<n,
\qquad \phi_n(t)_n=t_n,
\]

and `F_n(x,y)=(-1)^{phi_n^{-1}(x) dot y}`. The prior corrected random-walk proof claims `G_y(F_n) >= n+n^2/C`, `C=34,406,400`, for `n>=131072`; the newer single-atom proof instead gives `G_y >= n+n^(3/2)/16000`. The audit below checks the former proof's constant chain independently. The triangular code is existing input; no novelty claim is made for the code.

## Independent reconstruction of the critical chain

For each selected `ell`, put `m=n-ell` and `Z_s=2K_s-s`, where `K_s` is the number of ones in the length-`s` suffix after deleting coordinate `ell`. As `s` runs from `m` to `n-2`, `Z_s` is a simple symmetric walk with `L=ell-2` increments. A zero at any even `s` is a derivative hit, because the threshold equation is `K_s=floor((s+1)/2)`; hence the event `B={Z_s=0 for some s in [m,n-2]}` is sufficient to ensure `D_ell(T)\{ell}` is nonempty.

The starting window `0 <= Z_m <= sqrt(m)/4` has probability at least `1/128`. This follows by counting at least `sqrt(m)/16` nonnegative central atoms and using the adjacent-binomial-ratio product: each atom in that window is at least half the mode mass, and the mode mass is at least `1/(2 sqrt(m))`. The product estimate is valid in both parities: for even `m=2r`, the ratio at displacement `d` is `prod_{i=1}^d(1-(2i-1)/(r+i))` and the sum of losses is at most `d^2/r <= 1/32`; for odd `m=2r+1`, it is `prod_{i=1}^d(1-2i/(r+1+i))` and the loss sum is at most `d(d+1)/(r+1)<1/32`.

For the independent increments, `S_L` has `E S_L^2=L` and `E S_L^4=3L^2-2L<=3L^2`. Paley–Zygmund applied to `S_L^2` yields `P(S_L^2>=L/2)>=1/12`; symmetry gives `P(S_L<=-sqrt(L/2))>=1/24`. In the chosen interval `ell in [ceil(n/3), floor(n/2)]`, `L=ell-2 >= m/3` for `n>=18`, and `sqrt(L/2)>=sqrt(m/6)>sqrt(m)/4`. Thus the independent intersection forces the walk to go from nonnegative to negative, and so to hit zero. Therefore `P(B)>=1/(128*24)=1/3072`.

Let `A={s/3<=K_s<=2s/3 for all s=m,...,n-2}`. Binomial Chernoff and a union bound give `P(A^c)<42 exp(-m/20)`, which is below `1/6144` for `m>=1024`. Hence `P(A intersect B)>=1/6144` without an independence assumption between `A` and `B`.

For a base `T` in `A`, an upper extension changes each missing suffix bit independently with probability `1/2`. At length `s`, the probability of hitting the central layer is bounded by `2^{-N_s D_2(r_s/N_s || 1/2)}`, where `N_s=s-K_s(T)`. The two-sided band gives `N_s>=s/3`, and the relation between `r_s` and `K_s` gives `r_s/N_s<=1/4+3/(4s)<=1/3` for `s>=9`. Since `D_2(1/3||1/2)>1/15`, this is at most `2^{-s/45}` and hence `2^{-s/50}`. Summing over suffix lengths gives `q_ell(T)<=C50 2^{-m/50}`, `C50=(1-2^{-1/50})^{-1}<128`; because `log2 C50<7<=m/100`, `q_ell(T)<=2^{-m/100}`.

For bases with `x_ell in S` and `S dot D_ell(T)=0`, the base matching sign is positive. Any extension with `D_ell(T')={ell}` has negative sign, so cannot match; therefore the matching fraction `R_{y_ell}(S,T)<=q_ell(T)`. On `A intersect B`, the rest of `D_ell(T)` is nonempty, and exactly one quarter of uniform `S` satisfy both conditions. This produces an event of probability at least `1/24576` on which `-log2 R>=m/100`. Disjointly, `x_ell notin S` has probability `1/2` and exact `R=1/2`. Using the exact flat-spectrum restriction identity `Delta_i U=1/2+E[-log2 R]`, this yields

\[
\Delta_{y_\ell}U\ge 1+\frac{m}{2,457,600}.
\]

There are at least `n/7` selected indices and each has `m>=n/2`; summing gives `G_y(F_n)>=n+n^2/34,406,400` for `n>=131072`. The arithmetic chain is internally consistent in this audit.

## GU implication and distinction from FEI

The exact spectrum has `H(F_n)=2n` and `I(F_n)=U(F_n)=n`. Thus the candidate, if the analytic proof is accepted, has `G/I -> infinity` while `U/I=1` and `H/I=2`; it would refute universal GU, not FEI. For each fixed `a>=0`, `0<=b<1`, the random-walk bound permits

\[
N(a,b)=\max\{131072,\lfloor C(a+b+2)\rfloor+1\},\qquad C=34,406,400,
\]

and gives `(G-aI-bU)/I > 3`. For the frozen pair `(4,3/4)`, `N=232,243,201` and the residual exceeds `3+1/C`.

The one-way reduction was checked algebraically from the recorded source theorem `H<=2(I-Var)+2U`: assuming GU, put `c=a/(1-b)`, use weighted pigeonhole to choose a coordinate with `Delta_i U <= (a+b U/I) Inf_i`, apply induction to both restrictions, and write `u=U/I`, `x=Inf_i/I`. Then `u-c <= b x (u-c)`, so `u<=c`, and `H<=(2+2a/(1-b))I`. This implication is not used to infer the GU obstruction.

## Audit conclusion and limitations

No new fatal algebraic error was found in the corrected random-walk proof's constant chain during this self-audit. That is **not** an independent end-to-end review: the proof still requires the assigned independent reconstructions of the triangular derivative identity, the central-band/hitting intersection, and the matching-fraction estimate with the terminal extension retained. The fixed-time central-atom proof is a useful alternate mechanism. Its normalized excess `sqrt(n)/16000` is larger than `n/C` at the minimum tested dimension `n=131072`, but the random-walk excess `n/C` dominates once `n>(C/16000)^2≈4.624 million`. For all-parameter witnesses with large `a+b`, the random-walk route gives a dimension linear in `a+b`, while the atom route uses a dimension quadratic in `a+b`; retain both, but use the random-walk route for the asymptotic all-parameter witness absent a newly found defect. No full FEI claim is made.

## Persistence

Local artifacts and checksums are generated and verified. The standing source/write hold remains binding; no remote canonical write, Brain mirror, alternate route, shared-index update, or schedule change was attempted. Remote persistence and independent review remain unconfirmed.