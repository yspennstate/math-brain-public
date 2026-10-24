# Paid conversion between output and coherently appended root witnesses

All entropies are in bits. Let f be Boolean on a finite independent interior product cube, and let T be
any finite deterministic physical singleton stopping tree, querying each
coordinate at most once on a path. Pi is its full recorded transcript. Put

    R = I_phys(f) - E I_phys(f_leaf) = sum_v w_v Inf^phys_{i_v}(f_v).

Use A037's function-specific coherent lift: S0 has root Fourier-square law;
at a node with current remaining spectral set S_v, query i and retain
T=S_v\{i}. With q_T=sum of the two parent Fourier-square masses, choose
physical outcome b with kernel P(X_i=b)*childhat_b(T)^2/q_T, and discard i from the
current spectral set. Zero-q states are unreachable. Product Parseval gives actual physical
branches and exactly the actual child spectra. The kernel depends on S0 only
through T and the history, so

    I(S0;Pi) = J_T := sum_v w_v J_v.

Append arbitrary finite root variables (W,A) with ONE fixed conditional law
P(W,A|S0), and then propagate only via this lift, without reference resets.
Consequently (W,A) -> S0 -> Pi is a Markov chain and

    j_Z:=I(W,A;Pi) <= J_T.

For complete trees Y=f(X) is measurable from Pi. For partial trees attach Y
at the leaf with the actual conditional output law of f_leaf; its joint law
with Pi is the physical one. Set o=I(Y;Pi). Branch independence gives

    o=sum_v w_v I(X_i;Y|v) <= sum_v w_v h2(p_i)Inf^phys_i(f_v) <= R.

Indeed at each actual physical history the unqueried bits are independent,
I(X_i;Y|v)<=I(X_i;Y,X_-i|v)=H(Y|X_-i,v), and a pivotal two-point fiber has
output entropy h2(p_i) while a nonpivotal one has zero. This strengthens
the root-I bound to physically REMOVED influence and retains terminal output
entropy exactly: o=H(Y)-E H(Y|Pi).

The conditioning conversion is exactly

    Gamma_Z := H(Pi|Y)-H(Pi|W,A) = j_Z-o.

Its positive part has the joint accounting identity

    o/2 + [Gamma_Z]_+/2 = max(o,j_Z)/2 <= 2R/ln(2),
    sharpened to R/ln(2) for uniform physical inputs.

This uses the paid product-law channel bound J_T<=4R/ln(2), or the uniform bound J_T<=2R/ln(2), with no second copy of
R assigned to Gamma_Z. It covers S0 itself as Z and any coherently appended
finite witness/side-information pair. The bound does NOT apply to a witness
reoptimized independently at descendants, or to arbitrary additional
side information not appended conditionally at the root. Those change the
Markov chain and require channel/reset accounting.

In particular, if the declared output-bank estimate of A050 is used in its
exact form

    A_tax <= o/2 + H(Pi|Y)/2,

then conditioning on Z=(W,A) yields

    A_tax <= H(Pi|Z)/2 + j_Z/2
          <= H(Pi|Z)/2 + 2R/ln(2),
    with R/ln(2) under uniform inputs.

This is an entropy-bank CONVERSION, not a free supply of H(Pi|Z)/2 by an
actual reference. The latter conditional history entropy still has to be
included in a normalized code/reference or canceled by compatible posterior
credit. A050's output-information account and conversion correction are
already combined; adding their separate influence upper bounds would
unnecessarily reuse or enlarge the physical budget.

## Self-contained product-law channel bound

In one residual fiber write q=(1-p)G^2+pH^2. The elementary inequality
ln u<=u-1 bounds its natural-unit mixture information by
((1-p)G^4+pH^4-q^2)/q=p(1-p)(G^2-H^2)^2/q.
For magnitudes a=|G|,b=|H|, weighted Cauchy-Schwarz gives
(a+b)^2<=q/[p(1-p)]. Hence that expression is at most (a-b)^2,
and at most (G-H)^2. Zero-q fibers vanish. Sum and apply Parseval:
J_v<=4 Inf^phys_i(f_v)/ln(2). This is not asserted sharp; it suffices
for a dimension/bias-independent conversion with removed physical influence.

## Sharper uniform scalar proof

For nonnegative a,b, in natural units

    (a^2 ln(a^2/q)+b^2 ln(b^2/q))/2 <= (a-b)^2/2,
    q=(a^2+b^2)/2.

Scale b to 1, put t=a/b>=1, and define twice the difference as

    F(t)=(t^2+1)ln((t^2+1)/2)-2t^2 ln(t)+(t-1)^2.

F(1)=0. F'(t)>=0 is equivalent to ln(2t^2/(t^2+1))<=1-1/t;
the difference on the right has derivative (t-1)^2/[t^2(t^2+1)]>=0 and
vanishes at 1. Symmetry F(t)=t^2 F(1/t) handles t<1; endpoints follow by
continuity. This proves the scalar bound. Apply it to the two actual child
Fourier amplitudes' magnitudes, sum the residual labels, and use
(|G|-|H|)^2<=(G-H)^2 and Parseval. Then

    J_v <= (1/(2 ln2)) sum_T (G_T-H_T)^2
         = (2/ln2) Inf_i(f_v).

Multiply by the node probabilities and sum to prove the paid tree-channel
bound above. The proof is reconstructed here; it is an already-known input,
not a newly closed FEI claim.

## Residual after EXACT bank conversion

Define M_T=sum_v w_v M_v and Dbar_T=sum_v w_v[1/2-(J_v-M_v)] at uniform
physical biases. A050's exact ledger is

    Hhat(f)=E Hhat(f_leaf)+2M_T+H(Pi|Y)/2+o/2-Dbar_T.

For Z=S0 replace the two output terms by H(Pi|S0)/2+J_T/2 exactly. This
does not eliminate M_T, Dbar_T, or the terminal entropy. Since H(Pi) is
the expected number of fair queries and H(Pi|S0)=H(Pi)-J_T, the net identity
reduces to the original erasure/channel telescope. In particular the
conditional history bank cannot be dropped merely because its conversion
cost is influence-paid. For arbitrary coherently appended Z the same
replacement uses j_Z/2 exactly, but H(Pi|Z) is generally larger.

## Rare-output boundary: a half-I conversion allowance is insufficient

Let f_r=1-2*1_{x=(1,...,1)} on r fair bits. Its essential short-circuit tree
queries the first zero or all r ones. Write delta=2^-r, I=2r delta,
v_s=4*2^-s*(1-2^-s) for s residual bits. At the node with s residual bits,
the inactive child is constant, and the active child's nonempty spectral
mass is v_s. Therefore exactly

    J_s=h2(v_s/2)-h2(v_s)/2,
    J_T=sum_{s=0}^{r-1} 2^{-(r-s-1)} J_s,
    o=H(Y)=h2(delta), Gamma_{S0}=J_T-h2(delta).

As s grows, J_s=v_s/2+O(v_s^2)=2*2^-s+O(4^-s), using the cancellation
in h2(v/2)-h2(v)/2. Summation gives J_T=4r delta+O(delta).
Also h2(delta)=r delta+delta/ln2+O(delta^2). Consequently

    Gamma_{S0}/(2I) -> 3/4,
    (o+[Gamma_{S0}]_+)/(2I) -> 1.

Thus the proposed stronger conversion-only bound Gamma_+/2<=I/2 is false
on an actual uniform Boolean family. A finite exact certificate is supplied
for a frozen r in 1..16 when the checker finds the first positive sign.
This is a counterexample to that new conditioning-cost allowance, not to
the existing A050 half-output-bank theorem, its output payment, or FEI.
The point-defect J_T and influence asymptotics are also explicit A048 inputs;
this stage's new consequence is their side-bank conversion scale.

## Why arbitrary additional side information is excluded

Use the same r-bit fair point defect but stop after the first essential query.
Let A_future be that query's physical outcome, so A_future=Pi. Its removed
influence is R=2delta. The output information released is
o=h2(delta)-h2(2delta)/2=delta+O(delta^2). Consequently

    H(Pi|Y)-H(Pi|A_future)=1-o -> 1,
    [H(Pi|Y)-H(Pi|A_future)]/(2R) -> infinity.

The query remains essential for every r. Thus allowing future/history-derived
side information without the root-append/Markov condition destroys every
finite influence bound on conversion. A_future can be represented by a root
conditional law only if it is drawn afresh independently of subsequent
branches given S0; identifying that independent draw with the actual future
outcome is a different reveal channel. This control does not refute the
compatible theorem or any registered claim; it pins exactly why the
conditioning hypothesis cannot be dropped.

## Honest first unsupported line

H(Pi|W,A)/2 is funded once by the SAME normalized whole-set/witness reference,
with required side information, and the remaining signed M/terminal cost is
paid by exclusive physical influence. The Markov-compatible conversion
theorem does not prove that. The product-law conversion has the larger
explicit constant 2/ln(2). No arbitrary reference-reset version,
optimal conversion constant, or universal erasure payment is asserted.
