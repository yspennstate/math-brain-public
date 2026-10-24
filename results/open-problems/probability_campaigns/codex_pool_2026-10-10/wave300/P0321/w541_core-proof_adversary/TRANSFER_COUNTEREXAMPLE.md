# Exact counterexample at the correlation error scale

2026-10-10. This is a finite probability example, not a Riesz Gibbs state. It independently tests the error threshold of a proposed observable-transfer route. Referee w542: pending.

Fix 0<h<1. On the four points (U,V) in {-1,1}^2 put

P(U=u,V=v)=(1+h u v)/4.

Set A0=U, Ar=V, B0=U, and Br=(V-h U)/(1+h). All four variables are centered and bounded in absolute value by one. The reference correlation is E[A0 Ar]=h, but

E[B0 Br]=(E[UV]-h E[U^2])/(1+h)=0.

The first observable has no approximation error. The second has

Br-Ar= -h(U+V)/(1+h),
||Br-Ar||_2^2 = h^2 (2+2h)/(1+h)^2 = 2h^2/(1+h).

Thus an L2 error of order h can destroy a correlation of order h completely, even when both the target and reference observables are centered and uniformly bounded. Setting h=r^-eta gives the critical algebraic rate. This refutes a general inference that an unspecified O(r^-eta) L2 error preserves a positive lower correlation bound. It does not refute a transfer theorem with a small enough explicit constant or with o(r^-eta) error, nor a theorem that assumes extra orthogonality or cross-correlation decay.

For comparison, the sufficient elementary bound for centered complex observables with ||A0||_2,||Ar||_2<=M and errors E0=B0-A0, Er=Br-Ar with ||E0||_2,||Er||_2<=delta is

|E[B0 conjugate(Br)]-E[A0 conjugate(Ar)]| <= 2 M delta+delta^2.

It follows by expanding the product and applying Cauchy-Schwarz to its three terms. If the reference correlation is real and at least c r^-eta, and 2 M delta+delta^2 <= kappa c r^-eta with a fixed kappa<1, its real part remains at least (1-kappa)c r^-eta. The reference upper estimate transfers in the same way. The square root of the reference correlation is not a sufficient general L2 error threshold for this bound.

The main particle-model input remains absent: a specified coupling and estimates for the actual microscopic bond observable versus a well-defined effective angular observable, with nonzero amplitude and the appropriate distance-dependent error. This example is a sharp order obstruction to a proof technique, not a phase-existence result.

Limit-order caveat: vanishing volume errors can suffice for an iterated limit. If fixed observables B_L and A_L converge in correlation at every fixed separation r, and delta_L(r)->0 for that fixed r, the bound above gives identical infinite-volume correlations at r. One may then study r->infinity in the limiting correlation. A volume-uniform distance rate is needed for simultaneous limits, or for a residual error that does not vanish in the thermodynamic limit. A statement that all volume-only approximation is insufficient is too broad unless its quantifiers are qualified.

NEXT: Check w540's actual transfer statement for its constant, centering, observable identity, and order of limits.
