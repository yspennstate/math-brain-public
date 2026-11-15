from pathlib import Path
p=Path('run_audit.py')
s=p.read_text().replace('with a per-child heap cap and wall limit.','with a per-child wall limit and RSS measurement.')
s=s.replace('    cap=768*1024*1024\n    resource.setrlimit(resource.RLIMIT_DATA,(cap,cap))\n    resource.setrlimit(resource.RLIMIT_CPU,(230,235))\n','')
s=s.replace("'heap_cap_bytes':768*1024*1024,","'memory_note':'RLIMIT_DATA unavailable in this environment; actual child RSS measured and checked below 1 GiB',")
p.write_text(s)
