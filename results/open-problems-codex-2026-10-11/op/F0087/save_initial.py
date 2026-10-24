import pathlib
P=pathlib.Path('.')
(P/'ATTEMPT.md').write_text('''# F0087 — attempt, 2026-10-11

## Exact setting and scope
Kenyon's height h uses reference flow 1/4 (Section 2.2, PDF p.16), so the usual integer domino height is H=4h, up to sign and an additive constant. Fix the translation-invariant zero-slope infinite-volume uniform square-grid dimer Gibbs measure and pin h at one face. This is an explicit special case of the source, which does not specify domain, pinning, topology or renormalization.

## Literature obstacle recorded immediately
Dubédat, arXiv:1110.2808, current PDF title *Dimers and families of Cauchy-Riemann operators I*, Theorem 24 (PDF p.77) gives paired-charge separated-point correlations for s in (-1/2,1/2). His introduction (p.3) explicitly says this partially answers Kenyon's Open problem 1. Proposition 23 (p.75) states the absolute-value two-point asymptotic for 0<s<1/2. Thus no SOLVED_IN_LITERATURE verdict is justified by this paper.

## Result now being proved
For a piecewise constant embedding U_epsilon(x)=exp(i alpha h(f_epsilon(x))) of this infinite-volume height field, and alpha not congruent to 0 or pi modulo 2pi, U_epsilon tends to zero after testing against any compactly supported smooth function, in mean square. A quantitative O(epsilon^(2s^2)) bound on the squared norm follows from Proposition 23, where s is the representative of alpha/(2pi) modulo integers in (-1/2,1/2). This is an unrenormalized distributional limit, not a construction of the nontrivial renormalized field. Full proof and checks to follow below.
''',encoding='utf8')
