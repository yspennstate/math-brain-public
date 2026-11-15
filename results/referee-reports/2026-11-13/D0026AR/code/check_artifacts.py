import csv,hashlib,json,pathlib,re
root=pathlib.Path(__file__).resolve().parents[1]
report=(root/'REPORT.md').read_text()
assert report.splitlines()[0] in ('ACCEPT','MINOR','MAJOR','WRONG')
assert report.splitlines()[0]=='ACCEPT'
for name in ('2510.20461','1205.4584','1609.01364'):
    p=root/'sources'/f'{name}.txt'; assert p.exists() and 'PDF PAGE 2' in p.read_text()
for p in (root/'sources').iterdir():
    assert p.suffix=='.txt'
    s=p.read_text();assert all(ord(ch)>=32 or ch in '\n\t' for ch in s)
for line in (root/'sources'/'manifest.txt').read_text().splitlines():
    url=line.split()[1]
    name={'https://www.normalesup.org/~hartarsky/files/research/publi/KCM_book.pdf':'KCM_book_2025','https://irma.math.unistra.fr/~mareche/these_mareche.pdf':'Mareche_thesis'}.get(url,url.rsplit('/',1)[-1])
    p=root/'sources'/(name+'.txt');assert p.exists()
    assert re.search(r'TEXT_SHA256=([0-9a-f]+)',line)[1]==hashlib.sha256(p.read_bytes()).hexdigest()
for line in (root/'data'/'claim_snapshot_sha256.txt').read_text().splitlines():
    digest,name=line.split('  ',1);assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
for p in root.rglob('*'):
    if not p.is_file():continue
    assert p.suffix.lower() not in ('.pdf','.png','.jpg','.jpeg','.tiff','.bmp','.gif')
    with p.open('rb') as f: assert not f.read(8).startswith(b'%PDF-')
for label,q in [('055',.55),('070',.7)]:
    rows=list(csv.DictReader((root/'data'/f'q{label}.csv').open()))
    assert float(rows[-1]['time'])==100 and int(rows[-1]['paths'])==10000
    for r in rows:
        n=int(r['paths']);count=int(r['origin_zero_count']);mean=count/n
        assert abs(mean-float(r['origin_zero_mean']))<1e-12
        se=(mean*(1-mean)/(n-1))**.5
        assert abs(se-float(r['origin_zero_se']))<1e-12
    assert 'boundary_infections=0' in (root/'data'/f'q{label}_run.txt').read_text()
result={'report_verdict':report.splitlines()[0],'requested_sources_verified':3,'all_source_text_hashes_verified':True,'claim_snapshot_unchanged':True,'no_retained_pdf_or_raster_images':True,'csv_means_and_standard_errors_verified':True}
(root/'data'/'artifact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
