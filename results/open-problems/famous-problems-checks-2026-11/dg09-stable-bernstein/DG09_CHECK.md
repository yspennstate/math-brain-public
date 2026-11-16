# DG09: the stable Bernstein problem in R^7

12 Nov 2026, an agent. Row DG09 of the top-200 general list.

## Verdict

Claimed solved, not confirmed. One preprint: Hong, Li, Wang, "The stable Bernstein theorem in R^7",
arXiv 2609.15720 (14 Sep 2026, 85 pages). A complete, two-sided, stable minimal immersion of a
6-manifold into R^7 is a hyperplane; with the earlier cases (R^3: do Carmo-Peng, Fischer-Colbrie-Schoen,
Pogorelov; R^4: Chodosh-Li; R^5: Chodosh-Li-Minter-Stryker; R^6: Mazet) this would close Yau's problem,
since the Simons cone gives a stable non-flat example in R^8.

The row should come off the problems to attack and stay marked "reported solved" until the proof is
confirmed by someone other than its authors. It is long and computer-assisted, and no independent
check was found.

## What the proof is

After a point-picking reduction to bounded second fundamental form, let G be the minimal positive
Green function and J(t) the integral of |grad G|^3 over the level set {G = t}.

1. All moments int_0 J(t) t^(-sigma-1) dt with sigma < 5/2 are finite. Unit flux and the gradient
   estimate give sigma < 2; Bochner, Simons, stability, the divergence-free tensor |A|^2 g / 2 - A^2 and
   the Codazzi equations reach 2.46; stability applied to a nonlinear norm of two test functions
   reaches 2.4962 through coercive inequalities on fifteen rational parameter intervals; three more
   tensor divergence identities reach every sigma < 5/2. The algebraic inequalities of the last two
   steps are polynomial positivity statements checked in exact rational arithmetic.
2. Finite subcritical moments give finite critical energies and limits of t^(-5/2) J(t) at both ends.
   Brendle's sharp isoperimetric inequality for minimal hypersurfaces fixes the sign of the boundary
   term, and the critical spectral inequality then forces A = 0.

The authors state that AI assistance (ChatGPT 5.5, 5.6 and Astra) played a substantial role in finding
the argument and the parameters, and that Codex was used in the exposition.

Verification code: https://github.com/wgaom/stable-bernstein-R7 (commit 619b75d41555b1eafdb0db03439cdb15af82d9c5
on 12 Nov 2026). Besides the Mathematica notebook named in the paper it now holds 144 Lean files; its
README says the two algebraic estimates (R7.Paper.scalar_bound, R7.Paper.spectral_bound) are proved
with certificates checked by the Lean kernel. The Lean covers the algebra only, not the geometry. We
did not build it.

## What was checked here

Read: the introduction and proof outline, Lemma 2.1, Appendices A and B (the form of the certificates),
and Section 13 in full.

Section 13 (dg09_check.py, dg09_check.out, 8 exact symbolic checks, all pass): on a flat six-plane
G = 1/(4 w5 r^4), J(t) = 32 sqrt(w5) t^(5/2) and |{G > t}| = t^(-3/2) / (48 sqrt(w5)), so 5/2 is the
critical exponent and the paper's J_pole is right; Brendle's inequality in the form |dO| >= 6 (w5/6)^(1/6)
|O|^(5/6), with Cauchy-Schwarz and unit flux, gives (V^(-2/3))' >= 24 (w5/6)^(1/3) and V(t) <= t^(-3/2) /
(48 sqrt(w5)); a second Cauchy-Schwarz gives J(t) (-V'(t)) >= 1; together J_inf >= 32 sqrt(w5) = J_pole.
Each constant is as printed, and in the flat model every inequality of the chain is an equality, as it
must be for the argument to give rigidity.

By hand: the tensor |A|^2 g / 2 - A^2 is divergence-free on a minimal hypersurface of Euclidean space
(it is the Einstein tensor, since Ric = -A^2 by the Gauss equation).

Not checked: Sections 3 to 12 and 14 (about 70 pages), the rational certificates, the Lean build.

## Literature search

arXiv, 12 Nov 2026, three searches newest first ("stable Bernstein"; "stable minimal hypersurfaces" with
Bernstein or flat; "stable minimal" with R^7 or dimension seven). One paper uses the theorem as an
input: Z. Wang, arXiv 2609.19120 (finite index constant mean curvature hypersurfaces in space forms of
dimension at most seven). Nothing disputing it and no independent proof. Related and consistent with
the method: Cabre, Catino, Mari, Mastrolia, Roncoroni, arXiv 2604.14393 (Green-kernel gradient
estimates, R^4).

## Proposal for the list

Keep DG09 as REPORTED_SOLVED, check level "outline read, one section and its constants verified, proof
not verified", and do not spend attack effort on it. A cheap way to raise the check level: build the
Lean part of the authors' repository (read its lakefile first) and confirm the two theorems and their
axioms; that would settle the computer part, leaving the geometry of Sections 3 to 12 and 14.
