# Independent review: arbitrary full-rank input, finite boundary grid

**Disposition:** The theorem and proof in `BOUNDARY_GRID.md` pass this audit under the stated model: fixed `k,d,N_0`, full-row-rank `X`, independent original-coordinate symmetric stable initialization, standard simultaneous two-layer GD, and the ReLU derivative convention `1{v_j>0}`. The conclusion is only the finite boundary-grid vector (and its deterministic-grid held `J_1` path). I found no substantive missing estimate. The prior joint initialization theorem is a genuine dependency; the extension of its ray coefficients to a fixed nonorthogonal `X` uses rank, not orthogonality. This is an internal mathematical review, not a claim of external certification or novelty.

## Exact scaling and finite-step localization

With `a=m^(1/alpha)`, `L=(log m)^(1/alpha)`, the physical step `gamma/L` applied to the `L^2`-accelerated loss indeed produces the parameter increment `gamma/a` in (1). For one row, let `Y=(W,U)`. The update matrix is `I+(gamma/a) [[0,(X^T D(v)r)^T],[X^T D(v)r,0]]`; its increment has operator norm at most `(gamma/a)||X||||r||`. Thus the claimed bound for `S_m,n` holds for every gate pattern, including a step that crosses or reactivates a gate.

The output-increment estimate (8) can be checked directly. Writing `h_n=(XU_n)_+`, the exact split is

`L(f_(n+1)-f_n)=a^(-1)sum_i W_i,n(h_i,n+1-h_i,n)
                     +(gamma/a^2)sum_i (r_n^T h_i,n)h_i,n+1`.

The first norm is at most `gamma||G||||r_n|| a^(-2)sum_i W_i,n^2`. Replacing `h_i,n+1` by `h_i,n` in the second costs at most

`gamma^2 a^(-3)||G||||X||||r_n||^2 sum_i |W_i,n|||U_i,n||`.

The remaining part is bounded by `gamma||X||^2||r_n||S_m,n`. This proves (8), with constants depending only on `X`. On `||r_0||<=R, S_m,0<=B`, induction over **fixed** `N_0` then gives `S_m,n<=2B`, `||r_n||<=R+1`, and `max_n||r_n-r_0||=O(1/L)` for all sufficiently large `m`. The induction needs no contraction of the residual and is not circular: each step's energy and output estimates use only already bounded values. Since `r_0` and `S_m,0` are tight, localization can be removed.

The row displacement is `O(R_i,0/a)` over finitely many steps. Cauchy-Schwarz therefore gives both frozen-square estimates (10): `a^(-2)sum_i|W_i,n^2-W_i,0^2|=O_P(1/a)` and `||C_m,n-C_m,0||=O_P(1/a)`. This includes rows with hidden coordinates of order `a`; no per-row boundedness is assumed.

## Initialization and threshold continuity

For a general fixed `X`, the ReLU ray remainder bounds quoted in the theorem remain valid with constants depending on `X`. The original-coordinate rays `q_ell^+-q_ell^-=Xe_ell` span `R^k`, so the asserted nondegenerate `F` and positive-definite `C` follow from the prior signed-ray limits. The marked `W` endpoint process is independent of `F` in that joint initialization limit. Orthogonality of the input rows is used in the older continuous-time dynamics, but not in this initialization argument.

The limiting endpoint map is discontinuous only where a component of some `v_n` is zero. For fixed `z,r`, and any prescribed finite mask history, `v_n=Xu+gamma z G sum_(j<n)D_j r`. Every such zero is an affine hyperplane in `u` because each row of `X` is nonzero. The stable mark vector has a density. A finite union over histories and coordinates has zero mark probability; independence of `F` and `N` allows the same conditioning with random `r=y-F`. For each finite retained collection of Poisson atoms, all gates have positive threshold margins simultaneously through `N_0`. The finite-width endpoint recursion (11), together with `W_i,n/a->z` and `r_n->r`, then converges by induction even when gates turn off and later reactivate. Countability extends the zero-threshold statement to every fixed integer step almost surely.

## Small marks, output, and topology

For `|z|<=1`, the bound `||z[(v_n)_+-(Xu)_+]||<=n gamma z^2||G||||r||` makes the output Poisson sum absolutely convergent; the kernel sum is bounded by `||G||sum z^2`. Since `alpha<2`, their small-`|z|` tails vanish in probability as `epsilon^(2-alpha)`. There are only finitely many atoms with `|z|>epsilon`; their large-`|z|` and large-`||u||` tails are removed by occurrence probabilities, without invoking an invalid second moment of large stable jumps.

At finite width, initial small-`|W|` square mass has `limsup_m E[a^(-2)sum_i W_i,0^2 1{|W_i,0|<=epsilon a}]=O(epsilon^(2-alpha))`. Equation (10) transfers this bound uniformly over the finite grid to current `W_i,n^2`. It bounds both the omitted first-layer kernel and the omitted first term of (15), the latter by an additional factor `gamma||G||||r_n||`. The second term of (15) equals `gamma C_m,n r_n+o_P(1)=gamma Cr+o_P(1)` jointly on localization. Retained atoms give the displayed Poisson increment. Summing the finite increments telescopes exactly to `P_n`, and the same cutoff applied to (2) gives `K_n`.

`K_n` is a pre-step tangent Gram and is PSD because `D(v_n)G D(v_n)` is PSD. It must not be used as an exact secant for the Euler output increment: crossing a ReLU face makes that secant generally nonsymmetric and potentially non-PSD. For example, take `G=[[1,0.9],[0.9,1]]`, initially `D=I`, and a step in which only gate 1 crosses after one tenth of the straight segment. The first-layer secant factor is `diag(0.1,1)G`; its symmetric part has determinant `0.1-(0.9*1.1/2)^2<0`. Such a step is attainable by choosing an initially small positive first preactivation and an update direction with negative first component. The proof correctly relies on the absolute finite-step bounds above, so it needs neither residual sign preservation nor monotone gates. The naive Euler identity `P_(n+1)-P_n=gamma K_n r` is not valid at a crossing step, even in the scalar critical-step problem; (15) supplies the correct area-like increment.

All held paths have the same finite deterministic jump set `gamma,2gamma,...` on a fixed boundary horizon. Joint convergence of the finite vector of heights gives uniform convergence under a coupling and hence product `J_1` convergence. The proof does not support a growing number of steps or a macroscopic-time limit, and the theorem properly declines both claims.

## Scope clarification

The no-absorption convention is essential for arbitrary `X`. If `G_12!=0`, a coordinate with `v_1<0` can move through the update driven by an active second gate and later become positive. An explicitly *absorbing* projected gate would need an additional history mask and would not obey (4)–(5). The current theorem states the standard nonabsorbing convention correctly.

One editorial improvement: make the words “jointly with the initial primitives” in (6) literal by displaying `(f_0,C_m,0,N_m,(H_m,n,L(f_n-f_0))_(n<=N_0))` and its limiting counterpart, with the specified point-process topology for `N_m`. Equation (7) and the proof already establish this stronger joint formulation; it does not change the theorem's substance.
