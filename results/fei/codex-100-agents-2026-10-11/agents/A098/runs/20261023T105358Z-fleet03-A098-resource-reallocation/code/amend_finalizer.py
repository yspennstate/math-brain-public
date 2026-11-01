from pathlib import Path
p=Path(__file__).with_name('finalize.py')
with p.open('r',encoding='utf-8',newline='') as f:s=f.read()
replacements={
    '3072':'176',
    'exact full-domain checks':'exact bounded-domain checks',
    'Two guarded runtime aborts preserved':'Three guarded runtime aborts preserved',
    "'aborts_not_counted':2":"'aborts_not_counted':3",
}
for old,new in replacements.items():
    assert old in s,old
    s=s.replace(old,new)
with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
print('FINALIZER_COUNTS_CORRECTED')
