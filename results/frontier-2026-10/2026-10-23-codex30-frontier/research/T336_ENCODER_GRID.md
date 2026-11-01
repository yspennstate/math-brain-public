# T336 addendum: finite-grid pretraining by quantizing the raw encoder alone

This closes the grid-comparator gap for the bounded-context, noisy-query Gaussian/RBF setting of [`agents/a28.md`](../agents/a28.md). The **learned hypothesis class varies only the raw-input ReLU encoder**. Every member uses the same, exact-real, unnormalized two-head Chebyshev attention core of [`agents/a21.md`](../agents/a21.md). Therefore no attention weight is rounded, and the grid class contains a quantitatively good comparator by rounding only the explicit encoder. The iid-task Gaussian-NLL finite-class theorem invoked at the end is [`agents/a24.md`](../agents/a24.md). This proves an existence/ERM sample bound, not an efficient training algorithm or an ordinary softmax-attention realization.

## Assumptions and the common class architecture

Fix `d,N,m≥1`, input ball radius `R>0`, RBF length scale `ell>0`, training/query observation-noise variance `s>0`, and a context-label bound `B>0`. A task has `1≤n_context≤N`, all training/query inputs in `||x||₂≤R`, and context labels satisfying `|y_i|≤B`. For the pretraining statement, draw iid **whole** tasks from the prescribed GP/design distribution conditioned on this label event (which has positive probability), then draw one noisy `m`-vector query label independently from the corresponding conditional Gaussian for each task, exactly as in `agents/a24.md`. Conditioning is determined by the observed context and leaves the conditional query law Gaussian.

Choose the feature degree `k` and dimension `p=binom(d+k,k)` below. Let `F_θ:R^d→R^p` be the fixed shape of the ReLU encoder from `agents/a28.md`, with `H` hidden layers, width `W`, and each of its `P_enc` affine scalar parameters chosen on a finite grid in `[-Q,Q]`. Pad every hidden layer with unused units so that the shape is exactly width `W`; a conservative dense parameter count is

`P_enc=dW+W+(H−1)(W²+W)+p(W+1)`.

After its affine output, apply the **fixed, unquantized** coordinate clip

`C₂(v)=−2+ReLU(v+2)−ReLU(v−2)`,

and use the shared feature map `ψ_θ(x)=(C₂(F_θ(x)_1),…,C₂(F_θ(x)_p))` at **every** active training and query token. Thus all grid encoders, including poor ones, satisfy `||ψ_θ(x)||₂≤2sqrt(p)`. Clip supplied context labels to `[-B,B]`, which changes none on the conditioned task support. Inactive training padding slots have feature and label exactly zero. If `b∈{0,1}` is their active flag, the **fixed** ReLU gate `σ(v+2b−2)−σ(−v+2b−2)` equals `bv` for any clipped feature coordinate `|v|≤2`; the same formula with `2` replaced by `B` gates a clipped label. This needs no variable-variable multiplication. In particular a zero raw input in an inactive slot must **not** simply be passed through the RBF encoder, whose constant coordinate is nonzero.

Use exactly one common Chebyshev interval and one fixed attention core for the whole grid:

`b_p=s+4Np`, `κ_p=b_p/s`, `q_p=(sqrt(κ_p)−1)/(sqrt(κ_p)+1)`.

Any grid encoder has a PSD full Gram matrix because its features are shared. Its training Gram has `λ_max≤tr G≤4Np`, so `spec(A_θ)⊆[s,b_p]`. The one-sided polynomial `P_L` and exact signed two-head recurrence of `agents/a21.md`, with coefficients calculated from `[s,b_p]`, therefore work without alteration for **every** grid member. Its relative residual obeys `e_L≤4q_p^L` and `0⪯P_L(A_θ)⪯A_θ^{−1}`. For any query list, its emitted mean/covariance are

`μ_θ=H_θᵀP_L(A_θ)y`, `Σ_θ=J_θ+sI_m−H_θᵀP_L(A_θ)H_θ`.

The Schur complement gives `sI_m⪯Σ_θ⪯J_θ+sI_m⪯(s+4pm)I_m` for every grid encoder. In particular all NLLs are finite, every emitted joint covariance is symmetric PSD above the noise floor, and **no output spectral projection is required**. Also `||H_θ||_op≤4p sqrt(Nm)` and `||P_L(A_θ)||_op≤1/s`, so

`||μ_θ||₂≤M:=4p N sqrt(m)B/s`.

The attention core (the two heads, fixed role masks, all local affine mixing, and fixed clip/gate parameters) is held exact and is not part of the learned grid. Its layer count is `L+1` attention blocks of two heads each. All its scalar weights may be arbitrary real constants determined by the public bounds; finite-class counting involves only `P_enc`.

## Explicit encoder-parameter grid perturbation

Write `T_enc=H+1` for the `H` ReLU affine layers plus final affine output. Use max norms and set

`D₀=max{R,1}`, `D_j=WQ D_{j−1}+Q` for `j=1,…,T_enc`,

`E_enc=Σ_{j=1}^{T_enc}(W D_{j−1}+1)(WQ)^{T_enc−j}`.

The unrounded target network of `agents/a28.md` has every parameter in `[-Q,Q]` and its intermediate outputs satisfy `||h_j||_∞≤D_j`: each affine row has at most `W` inputs, weights of magnitude at most `Q`, and bias at most `Q`; ReLU cannot increase the absolute bound. The same holds for any rounded network whose grid lies in `[-Q,Q]`. If corresponding parameters differ by at most `δ_w` and the layerwise max-coordinate state discrepancy is `e_j`, splitting the affine difference at the *grid* matrix gives, including the final affine output,

`e₀=0`, `e_j≤WQ e_{j−1}+δ_w(WD_{j−1}+1)`, hence `e_{T_enc}≤δ_w E_enc`.

Coordinate clipping is 1-Lipschitz. Thus rounding the target encoder changes its **clipped** feature vector by at most `sqrt(p) δ_w E_enc` uniformly over the input ball. Choose the scalar parameter grid of `K+1` evenly spaced points in `[-Q,Q]`, with `K=ceil(2Q/δ_w)` and `δ_w≤Q`. Its mesh is at most `δ_w`, each target parameter rounds within `δ_w`, and `K+1≤4Q/δ_w`; hence the finite class has cardinality bounded by

`J≤(4Q/δ_w)^{P_enc}`.

No parameter sensitivity of the attention core is needed: the rounded encoder gives an actual shared PSD feature kernel, and the same fixed solver has a guaranteed spectral interval for it.

## Explicit comparator and uniform forward KL

Let `ε>0` be the desired comparator KL tolerance. Use the functions from `agents/a28.md` with feature-norm upper bound `r=2`:

`M_N(2)=[N sqrt(m)B/s](1+4N/s)`, `V_N(2)=m(1+4N/s)²`,

`S_N(2)=4N sqrt(m)B/s`, `U_N(2)=16Nm/s`,

`C_*=[M_N(2)+S_N(2)]²/(2s)+m[V_N(2)+U_N(2)]²/(4s²)`,

`h=min{1,sqrt(ε/C_*)}`, `a=R²/ell²`,

`ν=ceil(max{1,2ea,log₂(2/h)})`, `k=ν−1`, `p=binom(d+k,k)`.

Construct the `agents/a28.md` target encoder at **encoder approximation** `ζ₀=h/16`, namely choose its square/exponential interpolation count

`n_grid=max{2,ceil(sqrt(C_{d,k,a}G/ζ₀))}`, with

`C_{d,k,a}=[Σ_{j=0}^k(da)^j/j!]^{1/2}`, `G=ad/2+a²/32+2 max(1,k)`.

This fixes `H=5+2 max(0,k−1)`, `W=2(n_grid+3)(p+d+1)`, and `Q=64[1+R^{−1}+a(d+1)+max(1,a^{k/2})]`, hence fixes `P_enc,D_j,E_enc`. Choose

`δ_w=min{Q, h/(16 sqrt(p)E_enc)}`,

and let `θ_*` be a nearest grid point to the target encoder's parameter vector. Its clipped feature map obeys

`sup_{||x||≤R}||ψ_{θ_*}(x)−φ_{≤k}(x)||₂≤ζ₀+sqrt(p)δ_wE_enc≤h/8`.

The target encoder is itself inside `[-2,2]` coordinatewise because its vector norm is at most `1+ζ₀<2`; clipping it is inactive. The **comparator**, although drawn from a globally `2sqrt(p)`-bounded class, therefore has the sharper `||ψ_{θ_*}(x)||≤1+h/8≤2`. This is why the constants `C_*` above can be selected before `p` without circularity. By the RBF feature-tail bound and the shared-feature inner-product error,

`sup_{x,z}|k_RBF(x,z)−ψ_{θ_*}(x)·ψ_{θ_*}(z)|`

`≤a^ν/ν!+2(h/8)+(h/8)²≤h/2+h/4+h²/64≤49h/64<h`.

Finally fix the **same core for all grid encoders** at

`L=max{1,ceil(log(4/h)/log(1/q_p))}`, `q_p=(sqrt(1+4Np/s)−1)/(sqrt(1+4Np/s)+1)`.

Its relative residual is at most `h` for all, including `θ_*`. The direct *forward* Gaussian-KL perturbation bound (★) of `agents/a28.md`, applied to this comparator with its actual norm at most two and solver interval `[s,s+4Np]`, now gives for every allowed task `D`

`KL(p_D || q_{θ_*}(·|D))≤C_*h²≤ε`.

There is no KL triangle step. Both true and emitted noisy-query covariance matrices are at least `sI_m` throughout the comparison. The only quantized quantities are encoder parameters; the ReLU clip, recurrence coefficients, attention heads, and output affine mixing remain fixed exact constants.

## Fully instantiated iid-task NLL/ERM bound

For the true RBF GP on this task support, the exact noisy-query law has

`||μ₀(D)||≤M₀:=N sqrt(m)B/s`, `sI_m⪯Σ₀(D)⪯V₀ I_m`, `V₀:=s+m`.

For every grid predictor, the preceding section gives the bounds `||μ_θ(D)||≤M`, `sI_m⪯Σ_θ(D)⪯V I_m`, `V:=s+4pm`. Let `R_μ=M₀+M` (distinct from the input radius `R`), choose confidence `0<δ_conf<1`, and define

`D_*=(m/2)log(2V/s)+mV₀/s+R_μ²/s`,

`v_*²=4mV₀²/s²+8V₀R_μ²/s²+D_*²/4`, `c_*=4V₀/s`,

`u=P_enc log(4Q/δ_w)+log(2/δ_conf)`.

Let `f_hat` be an exact empirical Gaussian-NLL minimizer over the **fixed** finite grid class after `T_pre` independent pretraining tasks and one independently sampled conditional query label vector for each. The conditional-task finite-class NLL theorem in `agents/a24.md`, plus the explicit grid comparator above, yields with probability at least `1−δ_conf`

`E_D KL(p_D || q_{f_hat}(·|D)) ≤ ε+2sqrt(2v_*²u/T_pre)+2c_*u/T_pre`.     (†)

An empirical `η`-minimizer adds `η`. The expectation is prior-averaged over task contexts; (†) is **not** a uniform-in-context guarantee for the learned ERM. It does not say that SGD or any efficient optimizer finds the ERM, and its NLL concentration depends on independently generated whole tasks, not repeated query draws from one shared GP realization. As `R→0`, use the constant feature map for the sole admissible input and omit the encoder grid; the same fixed-core and finite-class argument simplifies accordingly.
