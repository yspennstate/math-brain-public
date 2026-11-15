from pathlib import Path
import subprocess
p=Path('~/Downloads/frontier_layer_report_2026-10-15.html')
mesh=Path('~/brain-repo/12_cognitive_architecture/agent_mesh/agent_mesh.py')
subprocess.run(['C:/Python314/python.exe',str(mesh),'assert','--agent','codex-term-362ebe34','--resource',str(p)],capture_output=True,check=True)
b=p.read_bytes()
for old,new in [(b'cutoff91 admitted',b'cutoff 91 admitted'),(b'every0&lt;',b'every 0&lt;'),(b'improves256 to91',b'improves 256 to 91'),(b'Degrees2,3,4 retained;5',b'Degrees 2, 3, 4 retained; 5')]:b=b.replace(old,new)
b=b.replace(b'<td>T067, every degree</td>',b'<td>T067, earlier large-degree milestones</td>')
b=b.replace(b'q&nbsp;=&nbsp;3 is now open only for',b'At that stage q&nbsp;=&nbsp;3 was open only for')
b=b.replace(b'q&nbsp;=&nbsp;3 is open only for',b'At 07:12 q&nbsp;=&nbsp;3 was open only for')
b=b.replace(b'Next, in this order: (1) a Lindeberg',b'The proposals before the current cutoff-91 result above were: (1) a Lindeberg')
p.write_bytes(b)
