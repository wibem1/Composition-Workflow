"""Run native adapters against deterministic fixtures, without API credentials."""
from pathlib import Path
import subprocess,json,time
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'validation'
checks=[
 ('core','Engine',['python3','workflow-core/test_core.py']),
 ('reaper-workflow','Reaper',['python3','tools/test_workflow_core.py']),
 ('reaper-midi','Reaper',['python3','tools/test_lilypond_import.py']),
 ('reaper-provider','Reaper',['python3','tools/test_reasoning.py']),
 ('maestro-engine','Maestro',['python3','-m','unittest','discover','-s','engine','-p','*test*.py']),
 ('maestro-ui','Maestro',['node','engine/ui_selftest.js']),
]
for name in ['compactscore','workflows','shared_workflow','diagnostic_composition','model_catalog','startup_record','clipped_window','update','result_storage','diagnostic_helper']:
 checks.append(('muse-'+name,'MuseScore',['python3','tests/test_'+name+'.py']))
for name,args in [('ui-qt6',['test_ui.py']),('ui-qt5',['test_ui.py','--qt5']),('loader-qt6',['test_loader.py']),('loader-qt5',['test_loader.py','--qt5']),('restart-qt5',['test_update_restart.py','--qt5'])]:
 checks.append(('muse-'+name,'MuseScore',['python3','tests/'+args[0],*args[1:]]))
summary=[]
for name,folder,cmd in checks:
 start=time.monotonic()
 try:
  r=subprocess.run(cmd,cwd=ROOT/folder,capture_output=True,text=True,timeout=60)
  output=r.stdout+r.stderr;code=r.returncode
 except subprocess.TimeoutExpired as e: output=str(e);code='timeout'
 (OUT/(name+'.log')).write_text(output)
 summary.append(dict(name=name,exit_code=code,seconds=round(time.monotonic()-start,2),skips=[x for x in output.splitlines() if x.startswith('SKIP')]))
 print(name,code,flush=True)
(OUT/'results.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False))
raise SystemExit(1 if any(r['exit_code']!=0 for r in summary) else 0)
