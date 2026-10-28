"""Record final receipts and reconcile initial/corrected validation in own draft."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'code/finalize.py'; s=p.read_text(encoding='utf-8')
s=s.replace("pilot=load(ROOT/'out/PILOT.json'); intake=load(ROOT/'out/INTAKE.json')","pilot=load(ROOT/'out/PILOT.json'); intake=load(ROOT/'out/INTAKE.json'); chain=load(ROOT/'out/CHAIN_CERTIFICATE.json')")
s=s.replace("'out/PARITY_OBSTRUCTION.json']}","'out/PARITY_OBSTRUCTION.json','out/CHAIN_FROZEN_SPEC.json','out/CHAIN_CERTIFICATE.json']}")
s=s.replace('Pilot command `python -B -X utf8 code/check.py --pilot`','Initial v1 pilot command `python -B -X utf8 code/check.py --pilot`')
s=s.replace('At this pilot dimension each child',"The corrected v2 pilot passed {pilot['assertions']:,} exact assertions in{pilot['runtime_seconds']:.3f}s on the SAME domain; the lower runtime follows outward dyadic rounding of rigorous log bounds, not a smaller test. At this pilot dimension each child")
s=s.replace('The first v1 primary failed at its LAST parity assertion',"Separate chain certificate: `python -B -X utf8 code/chain.py`,64 explicit Boolean chain lengths,2080 prefix recurrences,{chain['assertions']:,} exact assertions PASS in{chain['runtime_seconds']:.3f}s. At every retained all-zero chain step x=9/14336 and epsilon=1/561; sibling epsilon=3/787. The path spends L*log2(561/560)>L/561, unbounded in L; no full truth tables were materialized. The integer561^64*63^2>560^64*64^2 confirms that the64-step path exceeds the prior two-round path-log allowance. All-dimensional extension follows the displayed mean recurrence in DERIVATION, not this finite certificate.\n\nThe first v1 primary failed at its LAST parity assertion")
s=s.replace("'out/PARITY_OBSTRUCTION.json','out/SOURCE_MANIFEST.json'","'out/PARITY_OBSTRUCTION.json','out/CHAIN_CERTIFICATE.json','out/FAILED_FIRST_PRIMARY.json','out/SOURCE_MANIFEST.json'")
s=s.replace("'; review pending, FEI OPEN.","'; review pending, FEI OPEN.")
p.write_text(s,encoding='utf-8')
# Save the independently reconstructed controller Gram scalars as a small receipt.
(root/'out/GRAM_IDENTITY.md').write_text('Exact controller character sums: beta=3/8, C=3/512, D=3/256, E=21/512. Hence C-D^2/E=9/3584. Checked by exact Walsh arithmetic in both pilot and primary; see DERIVATION equation(3) for its uniform-in-mean lower bound.\n',encoding='utf-8')
print('Final validation and chain receipts incorporated; corrected pilot runtime reconciled.')
