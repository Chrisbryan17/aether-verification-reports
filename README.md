# Aether Verification Reports

Source-pinned computational verification records produced using the Aether research infrastructure.

## Report 001: Lean Riemann Hypothesis reproduction, November 2026

**[Read Report 001](reports/001-riemann-hypothesis/REPORT.md)** | **[Original machine certificate](reports/001-riemann-hypothesis/independent-rh-certification.json)** | **[Evidence hashes](reports/001-riemann-hypothesis/source-reproducibility.json)**

Original mathematical proof: **Levent Alpöge, working with Claude**. Aether's local work reproduced the published Lean 4 formalization: a full compilation, an axiom audit of five statements, and an independently invoked Lean check. The Lean-based compilation and checks passed. Aether did *not* locally run a separately written kernel such as nanoda, con-leche or con-ron; those external verifications were reported by Andrew Sutherland of MIT.

**Scope:** This is an independent computational reproduction, *not* a new mathematical proof, a first verification claim, a claim of proof authorship, or a claim to distribute the original proof source. The author's Lean files and compiled artifacts are excluded.

The original audit certificate and provenance JSON retain their historic private-review authorization flags. These are snapshots of the verification process, not rights claims or a description of the published GitHub repository.

To confirm all published evidence bytes, run:

```bash
python scripts/verify_release.py
```

The report is citation-ready through [CITATION.cff](CITATION.cff); a Zenodo DOI will be added only if Zenodo successfully issues one.

### External references

- [Michael Rubinstein's independent reproduction record](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)
- [Andrew Sutherland's independent checker record](https://math.mit.edu/~drew/grh/)
- [Lean community research discussion](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
