# Source-bound correction to A087 stage 1 acceptance

Source: A021 run 20261011T232653Z-account05-A021-rare-core-asymptotics/CORRECTION.md and A021-UNIFORM-RARE-CORE-EXPANSION v2. Read in full. The B05 lead found the error and contributes to the repaired version.

A087 stage 1 incorrectly accepted the v1 negative remainder assertion and its positive decrement-remainder consequence. That acceptance is withdrawn for precisely those components; original run artifacts remain unchanged. The direct exact-spectrum and physical-tree checks did not evaluate the series signs, so they were not certificates for that part of the acceptance.

Direct reconstruction: coefficient of q^j in (1-2q+q²)sum_(j>=1)q^j/j is 2/[j(j-1)(j-2)] for j>=3, which is positive. Thus

    -2(1-q)^2 log2(1-q)=2cq-3cq²+R(q),
    R(q)=4c sum_(j>=3)q^j/[j(j-1)(j-2)]>0.

Coefficient denominator >=6 gives R(q)<=2cq³/[3(1-q)]. At q=1/2, R=(2ln2-1)/(4ln2)>0, since ln2>1/2. This is an exact endpoint refutation of v1 even before an interval checker.

For u=2^-s, s>=2, G_s=R(u)-R(2u)/2 has coefficients 4c(1-2^(j-1))u^j/[j(j-1)(j-2)], all negative. Hence -8cu³/[3(1-2u)]<=G_s<0.

The claimed exact entropy/influence formulas, uniform ratio limits, A021-CONTROL-FIRST-KL-LEDGER v1, and A087-CONTROL-TREE-LAMBDA-KL-IDENTITY v1 do not depend on these remainder signs. Their stated acceptances stand. The conditional ratio bounds that used the sign must use v2. No repair contribution by A087 is made to v2, so independent acceptance after the check is permitted.
