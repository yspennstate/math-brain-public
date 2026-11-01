from pathlib import Path
p=Path(__file__).with_name('finalize.py')
s=p.read_text(encoding='utf-8')
edits={
"modes=['small']+['n3-'+str(j) for j in range(8)]+['audit']":"modes=['small','n3-0','n3-1','audit']",
"results['core_edit_pairs']==6360 and results['reference_cases']==12720":"results['core_edit_pairs']==1752 and results['reference_cases']==3504",
"No dimension was automatically increased.":"n3-2 hit the55-second guard without completion; zero assertions credited. FROZEN_SPEC_V1_3 reduced final scope before the audit;remaining n3 shards were not executed. No exhaustive three-bit claim remains. The next-stage prompt arrived during checkpointing; this prior stage is finalized first. No dimension was automatically increased.",
"Completed final full coverage:":"Completed final reduced coverage:",
"All 276 labelled cores on k1,2,3":"All4 one-bit and16 two-bit labelled cores plus three-bit labels0..63",
"`n3-0` through `n3-7`":"`n3-0`, `n3-1`",
"over6360 core edits/12720 references":"over1752 core edits/3504 references"
}
for a,b in edits.items():
    assert a in s,a
    s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
print('Final checkpoint scope corrected to completed domain')
