#!/usr/bin/env python3
"""Verify the precise published report evidence; no network access required."""
from __future__ import annotations
import pathlib,hashlib,sys
BASE=pathlib.Path(__file__).resolve().parent.parent/"reports"/"001-riemann-hypothesis"
def main():
    expected={}
    for line in (BASE/"SHA256SUMS").read_text(encoding="utf8").splitlines():
        digest,sep,name=line.partition("  ")
        assert sep and len(digest)==64 and all(x in "0123456789abcdef" for x in digest)
        assert name and name not in expected and name==pathlib.PurePosixPath(name).name
        assert not name.endswith((".lean",".olean"))
        expected[name]=digest
    files={p.name for p in BASE.iterdir() if p.is_file() and p.name!="SHA256SUMS"}
    assert files==set(expected),(files,set(expected))
    assert len(expected)==6
    for name,digest in sorted(expected.items()):
        assert hashlib.sha256((BASE/name).read_bytes()).hexdigest()==digest,"checksum mismatch: "+name
        print("PASS",name)
    print("AETHER_PUBLIC_RH_EVIDENCE_VALID",len(expected))
if __name__=="__main__":
    try:main()
    except Exception as exc:
        print("INVALID_PUBLIC_RH_EVIDENCE",repr(exc))
        sys.exit(1)
