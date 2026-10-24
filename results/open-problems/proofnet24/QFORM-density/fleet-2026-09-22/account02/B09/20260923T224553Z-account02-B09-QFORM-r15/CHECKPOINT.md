# B09 r15 early checkpoint — rank-one pair square–hyperbola receiver

Status: supporting calculation; full QFORM remains open.

Let `(U,V)` have a joint probability density `rho<=M` on `R^2`; let `W` be independent of `(U,V)` with density `f_W<=S`. For

`T = U^2 + 2 V W`,

split the coarea density at `|V|=r`.

For `|V|<=r`, integrate in `U`. The two roots contribute at most `M (t-2vw)_+^{-1/2}`. For each `w!=0`,

`int_{-r}^r (t-2vw)_+^{-1/2} dv <= 2 sqrt(r/|w|)`.

The cap-one bathtub bound at exponent `1/2` gives

`E |W|^{-1/2} <= 2 sqrt(2S)`.

Hence the small-`V` contribution is at most

`4 sqrt(2) M sqrt(S r)`.

For `|V|>r`, integrate in `W`; its conditional density contribution is at most `S/(2|V|)<=S/(2r)`, and the hub density has total mass one. Thus

`||p_T||_infinity <= 4 sqrt(2) M sqrt(S r) + S/(2r)`.

Optimizing at `r^(3/2)=sqrt(S)/(4 sqrt(2) M)` gives

`||p_T||_infinity <= 3*2^(2/3) M^(2/3) S^(2/3)`.

By scaling, for `a,b!=0`,

`||p_(a U^2 + 2 b V W)||_infinity <= 3*2^(2/3) M^(2/3) S^(2/3) |a|^(-1/3)|b|^(-2/3)`.

This is a direct linear-small-ball/coarea estimate: no decoupling square root, no moments/support assumptions, and no post-rotation independence. An area-preserving linear change of the *two-dimensional hub block* preserves the joint density cap, so the lemma is adapted to an exact rank-one physical pair core plus a collinear star.

Next: splice this with the exact rank-one overlap-two minor identity and the pinned mixed-hub theorem in the transverse cross-rank-two branch.