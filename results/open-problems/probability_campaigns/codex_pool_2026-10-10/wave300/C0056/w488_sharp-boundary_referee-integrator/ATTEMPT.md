# C0056 boundary audit (w488, 2026-10-10)

The recorded target has two parts: nonzero absolutely continuous spectrum for weak-disorder Anderson on Z^3, and GOE local statistics for finite-volume restrictions. The site law and exact bulk interval are not fixed by the intake wording. The September 2026 OpenAI preprint claims the spectral part for iid uniform disorder; its correctness and independent review remain unknown.

## Independently checked peer route

I checked w487's four initial derivations step by step. The diagonal example disproves a tempting annealed-first-moment bridge but is not the target operator. The Poisson Lp criterion is valid for p>1; at p<=1 the integrated bound is automatic even for a Dirac mass. The exact second-moment formula is correct. For the actual hopping operator, the Schur-complement computation correctly shows that site averaging alone gives a p=1 bound while this particular p>1 route needs a uniform negative moment of the imaginary deleted-site bath width. The six neighbor Green functions are dependent through loops; no product estimate follows from iid site variables alone. The unresolved load-bearing step for this route is a uniform p>1 integrated bound at eta down to zero plus positive spectral mass. Other routes need not use this criterion.

I also checked w487's S1.487.5 free-operator counterexample. Fourier change of variables proves all free infinite-volume spectral measures are a.c.; on odd periodic tori k and -k pair every momentum in an interior energy window and force at least half the finite-volume gaps to be zero. Verdict FIX only because 'nonempty interval' must read 'nondegenerate interval' to ensure its eigenvalue count diverges. This counterexample is at lambda=0 and does not decide fixed positive disorder.

## New general atomic boundary lemma (S1.488.1)

Let mu be a finite positive Borel measure, I an open interval, p>1, and t0 in I an atom of mass m>0. Define F_eta(E)=integral eta/((t-E)^2+eta^2) dmu(t). Then for any deterministic eta_n down to zero,

    liminf_n eta_n^(p-1) integral_I F_eta_n(E)^p dE >= c_p m^p,
    c_p = integral_R (1+u^2)^(-p) du > 0.

Proof: positivity gives F_eta(E)>=m eta/((t0-E)^2+eta^2). Raise to p and integrate. With u=(E-t0)/eta, the right-hand side is m^p eta^(1-p) integral_{(I-t0)/eta}(1+u^2)^(-p)du. Since t0 is interior, the expanding interval tends to R; monotone convergence along decreasing eta (or dominated convergence) gives c_p. The result is sharp for mu=m delta_t0 when I=R, and asymptotically sharp for bounded I containing t0. For random mu with positive probability of an atom in I, the nonnegative random liminf is positive on that event; Fatou implies liminf_n eta_n^(p-1) E integral_I F_eta_n^p >0, so an eta-uniform expected p moment is impossible. This is a boundary lemma for a proposed spectral-measure criterion, not a statement about the Anderson parent problem. Independent review requested from w491; until then it is an author proof only.

## Hardest remaining C0056 step

Neither w487's valid conditional estimates nor the new atomic lemma proves the negative bath-width estimate needed for a.c. spectrum of the positive-hopping iid operator. The later public preprint may claim this via another method, but an abstract and source hash are not a proof verdict. GOE statistics are an additional part of the intake target and are not claimed by that abstract.
