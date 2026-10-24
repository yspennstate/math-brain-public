# P0309 independent route (written before reading peer proof artifacts)

Source anchor: Lewin, *Coulomb and Riesz gases: The known and the unknown*, arXiv:2202.09240v2, Sections VI and VI.B. The intake title does not define a unique theorem. I choose the mathematically defined short-range regime d=3, s>3, finite beta as a first special case. The long-range case needs a separately specified renormalized Gibbs construction.

## Proposed route

Seed periodic Gibbs limits with boundary conditions favoring a candidate lattice, and establish a positive Bragg-order observable by a block free-energy comparison. Coarse blocks must tolerate local particle displacement; the entropy of displaced particles and interfaces must be included. A Peierls-style argument would need a uniform excess free-energy lower bound for macroscopic disordered regions, followed by a thermodynamic limit and DLR verification. The choice and global optimality of the lattice is itself unresolved. No such bound is proved here.

## Exact-periodicity gap obstruction, proved special case pending independent review

Fix s>3 and integer L>=2. On the 3-torus (R/LZ)^3 use the absolutely convergent periodization v_L(z)=sum_{n in Z^3}|z+nL|^{-s} away from the origin. Let X_L contain one particle at every site of (Z/LZ)^3, so N=L^3. Let X_L(delta) move only the origin particle by delta with 0<|delta|<=1/4. The displacement destroys exact lattice periodicity, but

|H_L(X_L(delta))-H_L(X_L)| <= C_s |delta|,

where C_s=s(4/3)^(s+1) sum_{m in Z^3 minus {0}} |m|^(-s-1) < infinity and is independent of L. Indeed, only pairs involving the moved particle change. Their periodized differences are indexed by m in Z^3 minus LZ^3. The mean-value theorem bounds each by s|delta|(|m|-|delta|)^(-s-1), and |m|-|delta| >= 3|m|/4. Summing gives the stated bound. Thus an argument that claims a volume-order energy gap against *every* nonexact lattice configuration fails even in the short-range special case. This does not rule out crystalline phases or a free-energy gap for a positive density of defects.

## Hardest unresolved step

Prove a low-temperature free-energy inequality for a robust positional-order event that tolerates phonons and a dilute set of defects, while controlling all competing arrangements and the entropy of contours uniformly in volume. A harmonic phonon estimate alone assumes the crystal and does not supply this inequality.

Review boundary: w536 should independently audit the obstruction lemma. KEEP for it would remain a special-case diagnostic, not a solution to P0309.
