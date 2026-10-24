# Repair/counterexample checks — 20260925T015002Z-account02-B11-five-line-audit-r12

C01 PASS: use an angular chart with one null ray removed; same Jacobian.
C02 PASS: Jensen |E F|^2<=E|F|^2 is exactly the missing averaging step.
C03 PASS: q=v is two affine lines for an indefinite nondegenerate quadratic form, hence null under a joint density.
C04 PASS: A=I_5 falsifies the unqualified crossing summary and validates need for no-pivot qualification.
C05 PASS: replace 'has a singularity' by 'admits an upper envelope'.
C06 PASS editorial only.
C07 UNCHECKED as literature status.
L222 PASS: 'factors ... are at most one' means factor values <=1; beta_i=0 => w_i=0, so arbitrary many such factors may be dropped.

B11 exact adversarial family: B=epsilon diag(I_p,-I_q), C=sqrt(epsilon)I, D=diag(I_p,-I_q) gives S=0 and exact spectral loss p+q at threshold 1. Naive B^dagger extension fails for B=0,C=I,D=0.
