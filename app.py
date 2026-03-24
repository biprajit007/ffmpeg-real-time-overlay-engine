#!/usr/bin/env python3
"""Apply dynamic text/stat/timestamp overlays to live streams."""
import argparse, shutil, subprocess

def require(x):
    if shutil.which(x) is None: raise SystemExit(f'Missing required binary: {x}')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input'); p.add_argument('output'); p.add_argument('--text', default='LIVE'); p.add_argument('--dry-run', action='store_true')
    a=p.parse_args(); require('ffmpeg')
    vf=f"drawtext=text='{a.text} %{pts\:hms}':x=20:y=20:fontsize=24:fontcolor=white:box=1:boxcolor=black@0.5"
    cmd=['ffmpeg','-y','-i',a.input,'-vf',vf,'-c:a','copy',a.output]
    print(' '.join(cmd))
    if not a.dry_run: subprocess.check_call(cmd)
if __name__ == '__main__': main()
