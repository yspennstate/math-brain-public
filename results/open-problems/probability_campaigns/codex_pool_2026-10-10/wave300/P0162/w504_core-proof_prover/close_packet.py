"""Finalize the signed-coefficient clarification without altering live stores."""
import ast
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def save(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def main():
    m=json.loads((ROOT/'measurements.json').read_text(encoding='utf-8'))
    assert m['status']=='PASS' and m['signed_auxiliary_coefficient_checks']==44838
    s=json.loads((ROOT/'BRAIN_SUBMISSION.json').read_text(encoding='utf-8'))
    bundle=json.loads(Path(s['draft_path']).read_text(encoding='utf-8'))
    bad='each of the other three blocks has coefficients -2t.'
    good='each other control block U has coefficients -2t*(-1)^1_{z in U}; their absolute values are 2t.'
    changed=False
    for entry in bundle['entries']:
        if entry['proof_text'] and bad in entry['proof_text']:
            entry['proof_text']=entry['proof_text'].replace(bad,good)
            entry['source']['revision']='reviewed-claim-signed-coefficients-clarified-20261010-v3'
            changed=True
    helper=ROOT/'finish_review.py'
    text=helper.read_text(encoding='utf-8').replace(bad,good)
    helper.write_text(text,encoding='utf-8')
    if changed:
        inbox=Path(s['draft_path']).parent
        part=inbox/'bundle_003.part'
        target=inbox/'bundle_003.json'
        assert not part.exists() and not target.exists()
        bundle['bundle_slug']='p0162-adaptive-coordinate-reviewed-draft-20261010-v3'
        save(ROOT/'bundle_003.json',bundle)
        save(part,bundle)
        part.rename(target)
        s['prior_reviewed_draft_path']=s['draft_path']
        s['draft_path']=str(target)
        s['submitted']['draft_files']=3
        s['submitted']['state']='reviewed-claim-proof-clarification-submitted-as-DRAFT'
    s['proof_clarification']={'scope':'Signed phases in auxiliary control blocks; entropy uses magnitude 2t',
                              'signed_integer_checks':44838,'full_P0162_proof':False,
                              'referee_keeps':'C001-C004 mathematical statements remain the same'}
    save(ROOT/'BRAIN_SUBMISSION.json',s)

    rows=[json.loads(x) for x in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if x]
    for row in rows:
        if row['id']=='w504-P0162-source-001':
            row['independent_reviewer']={'agent':'w506','verdict':'KEEP','scope':'historical source metadata only','receipt':'~/brain_workers/w506/REVIEW_PACKET.md'}
        if row['id'].endswith('C004'):
            row['remaining_gap']='No remaining gap in the independently checked displayed-family proof. The general FEI target is not proved.'
        if row['id'].endswith('C003'):
            row['proof_clarification']='Auxiliary block U has coefficient -2t*(-1)^1_{z in U}, not one common signed value. Its magnitude is 2t; the entropy calculation and stated Delta_j inequality use that magnitude. All 44838 nonzero-control coefficients in the gated cases passed exact integer checks.'
    (ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')

    note=(ROOT/'PROOF.md').read_text(encoding='utf-8')
    live='proofnet24/P03-fei/continuations/2026-10-10-w504-adaptive-coordinate/NOTE.md'
    lines=note.splitlines()
    patch=f'diff --git a/{live} b/{live}\nnew file mode 100644\n--- /dev/null\n+++ b/{live}\n@@ -0,0 +1,{len(lines)} @@\n'+''.join('+'+x+'\n' for x in lines)
    (ROOT/'patches/01_adaptive_coordinate_note.diff').write_text(patch,encoding='utf-8')
    overlay=Path('~/math-brain-build/src/math_brain/overlay.py')
    tree=ast.parse(overlay.read_text(encoding='utf-8'))
    a=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='IDENTIFIER_RE' for t in n.targets))
    pattern=re.compile(ast.literal_eval(a.value.args[0]))
    assert all(pattern.fullmatch(e[f]) for e in bundle['entries'] for f in ['namespace','logical_name'])
    assert sum(e['kind']=='lemma' for e in bundle['entries'])==3
    assert all(e['kind']=='concept' or e['proof_text'] for e in bundle['entries'])
    save(ROOT/'bundle_validation.json',{'status':'PASS','scope':'Local schema, actual identifier regex, proof-text and relation ends; integration pending',
                                      'unique_entries':4,'reviewed_lemma_entries':3,'conjectural_concept_entries':1,'relations':3,
                                      'signed_auxiliary_checks':44838})
    last=m['families'][-1]
    report=f'''The adaptive base-coordinate lemma is independently checked: w506 kept C001-C004 after separate algebra and truth-table checks. C003 proves Delta_j(F_m)<=4 Inf_j(F_m) for every base coordinate of the explicit bent rare-flip family. C004 gives H(F_m)<=2I(F_m). C001 is an exact entropy identity; C002 is a conditional reduction. The full P0162 conjecture is not proved, current openness remains UNKNOWN, and no novelty is claimed.

Before/after is the splitting choice on the same function. Command: {m['command']}. At m=12 the selector ratio is {last['selector_delta_over_influence']:.12f}, while every base-coordinate ratio is {last['base_coordinates'][0]['delta_over_influence']:.12f}. Thirty base-coordinate checks, 64 entropy/influence identity checks, and 44,838 exact signed auxiliary-coefficient checks passed. Maximum floating residual {m['max_absolute_identity_residual']:.3g}; CPU {m['cpu_seconds']:.5f}s; wall {m['wall_seconds']:.5f}s. Original measurements and gate are preserved in measurements_initial.json and COMPUTE_GATE_INITIAL.json.

A final proof pass corrected the signs of the three auxiliary control blocks: U has coefficient -2t*(-1)^1_{{z in U}}, with magnitude 2t. The entropy calculation uses those magnitudes. The fresh integer checks verify the corrected signed formula. Written proofs and independent algebra support the special cases; the numerical runs are not formal theorem receipts.

The single hardest remaining input is a uniform suitable-coordinate inequality for all Boolean functions with all influences below 1/16. C005 remains conjectural. C006's elementary conditional localization still awaits a narrow independent check; it does not prove this input.

The current four-entry DRAFT is {s['draft_path']}: three independently checked special-case lemmas with full proof text and one conjectural concept, with three supported relations. Prior versions are preserved and supersedes_existing marks the reviewed revisions. BRAIN_SUBMISSION.json records publication and review separately from ingestion (not observed) and retrieval (not tested). The validating coordinator integrates. The hook proposal is staged locally in proposals/math-w504.jsonl under the worker write restriction.

After review, apply the new research note from ~/<private-repo>/06_math_research/math-open-problems with git apply --check ~/brain_workers/w504/patches/01_adaptive_coordinate_note.diff, then git apply with the same path. The worker checked the patch in its own fixture; no original repository was modified.

NEXT: Independently check C006's Delta<=2 localization and validate the reviewed draft, while keeping C005 conjectural.
'''
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    packet=(ROOT/'REVIEW_PACKET.md').read_text(encoding='utf-8')
    packet+='\nFinal clarification: the auxiliary blocks have coefficient -2t*(-1)^1_{z in U}; entropy uses their magnitude 2t. Fresh '+m['command']+' passed 44,838 exact signed coefficient checks plus the 94 coordinate checks. Current draft: '+s['draft_path']+'.\n'
    (ROOT/'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
    attempt=(ROOT/'ATTEMPT.md').read_text(encoding='utf-8')
    attempt+='\nFinal signed-block clarification and fresh verification are recorded in REPORT.md: 44,838 exact auxiliary coefficients and the 94 coordinate checks passed. The mathematical claim remains the independently checked family-only bound.\n'
    (ROOT/'ATTEMPT.md').write_text(attempt,encoding='utf-8')
    receipt=json.loads((ROOT/'FINAL_VALIDATION.json').read_text(encoding='utf-8'))
    receipt['signed_auxiliary_coefficient_checks']=44838
    receipt['numeric_command']=m['command']
    receipt['patch_check']='pending after documentation clarification'
    save(ROOT/'FINAL_VALIDATION.json',receipt)
    print(json.dumps({'current_draft':s['draft_path'],'reviewed_lemmas':3,'conjectural_concepts':1,'signed_checks':44838,'coordinate_checks':94,'next':'Recheck the regenerated patch and mark NEEDS_REVIEW'}))


if __name__=='__main__':
    main()
