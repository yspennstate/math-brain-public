"""Integrate the separately frozen real-field guard and refresh stage metadata."""
from pathlib import Path
R=Path(__file__).resolve().parent.parent
p=R/'code/finalize.py';s=p.read_text(encoding='utf-8')
s=s.replace('244034','244039').replace('244,034','244,039')
s=s.replace('The diagnostic adds seven fixed cases and 26 assertions in 0.0013 seconds: three padded-subcube alphabet-loss certificates and the four leaf rejections.',
            'The diagnostic adds eight fixed cases and 31 assertions in 0.0013 seconds: three padded-subcube alphabet-loss certificates, the four leaf rejections, and one compressed real-field ownership guard. The guard uses 16 formal singleton coefficients and a binomial edge count, not a 16-bit truth table or an expanded Boolean search.')
s=s.replace('The non-Boolean channel bound is separated from the new final-edge Boolean ownership argument, which uses actual sign pivots.',
            'The non-Boolean channel bound is separated from the new final-edge Boolean ownership argument, which uses actual sign pivots. An exact normalized real control psi=(1/4)sum of 16 input signs is unchanged by edits at its zero middle layer and z00; its core spectral energy is 1, while the mask core influence is 6435/4096. This invalidates real-field reserve ownership even with the same sparse-fiber cap and confirms the new Boolean step.')
s=s.replace('The channel is already a general real log-Sobolev fragment; the new Boolean improvement is the owned core reserve.',
            'The channel is already a general real log-Sobolev fragment; the new Boolean improvement is the owned core reserve. The normalized real psi16 zero-middle-layer edit is unchanged, with core energy1 below mask influence6435/4096, so ownership fails outside Boolean signs even under the cap.')
s=s.replace('Total executed assertions: 244,039.',
            'Final primary certificates contain 244,039 assertions; all executed diagnostic revisions total 244,096. out/EXECUTION_HISTORY.json records the successful initial diagnostic and both real-guard revisions separately; overlapping replays are not counted as new functions.')
s=s.replace('244039 exact checks; four reviews', '244039 primary exact checks; four reviews')
s=s.replace('Pilot/full/diagnostic completed 244039 exact assertions;',
            'Final primary pilot/full/diagnostic certificates contain 244039 exact assertions; all executed revisions total244096;')
s=s.replace("'prior_scope_retractions':1,'math_assertions':244039,",
            "'prior_scope_retractions':1,'math_assertions':244039,'all_executed_assertions_including_replays':244096,")
marker="with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:"
insert="""# Refresh this stage's last rolling entry without duplicating it.
for rolling in ['WORKLOG.md','LEARNED.md']:
    path=A/rolling
    prior=path.read_text(encoding='utf-8')
    pos=prior.rfind('\\n## ')
    if pos>=0 and run in prior[pos:]:path.write_text(prior[:pos],encoding='utf-8')
"""
if insert not in s:s=s.replace(marker,insert+marker)
guards=[
 'An exact normalized real control psi=(1/4)sum of 16 input signs is unchanged by edits at its zero middle layer and z00; its core spectral energy is 1, while the mask core influence is 6435/4096. This invalidates real-field reserve ownership even with the same sparse-fiber cap and confirms the new Boolean step.',
 'The normalized real psi16 zero-middle-layer edit is unchanged, with core energy1 below mask influence6435/4096, so ownership fails outside Boolean signs even under the cap.',
]
for guard in guards:
    while guard+' '+guard in s:s=s.replace(guard+' '+guard,guard)
p.write_text(s,encoding='utf-8')
print('Updated finalizer for the frozen real-field guard; no search performed.')
