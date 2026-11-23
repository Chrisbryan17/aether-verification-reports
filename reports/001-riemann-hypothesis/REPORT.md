# Aether Verification Report 001
## Independent Computational Reproduction of the Alpöge–Claude Riemann Hypothesis Formalization

**Release:** v1.0.0, public source-free technical report. **Zenodo DOI:** Not yet issued.
**Verification date:** 22 November 2026 (UTC)
**Original mathematical proof:** Levent Alpöge, working with Claude.
**Reproduction infrastructure:** Aether, operated on NGH-VPS-01.

### Executive summary

Aether's retained machine logs, source pins, and independently invoked Lean checks establish a successful computational reproduction of a pinned Lean formalization of the Riemann Hypothesis. A full original Main build exited 0 after 183,893 Lake jobs; 175,187 compiled Lean module artifacts were present. A subsequent original axiom audit exited 0. Another independently invoked Lean run checked the named theorem declarations and printed their axiom dependencies, also exiting 0.

These are **Lean-based verifications**, not checks by independently written kernel implementations. The machine certificate's internal status label is FULL_RH_KERNEL_AXIOM_CERTIFIED; this label should be understood strictly as the scope above and is not a broader mathematical or separate-kernel certification.

### Original-source identity

- Upstream original author archive SHA-256: 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc
- Local mirror Git commit: 7cbf7a0c32fca1badf05931879a37c3f8a2b03b4
- Original Main.lean SHA-256: 017645ca448f2fd1f6fd5c4c2cb2c6e96e472725be13f6e180ca6e1574360939
- Original Statements.lean SHA-256: 79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf
- Lean toolchain: leanprover/lean4:v4.33.1
- Mathlib revision: 0df444a360eaa60ab8c11dca51a86af692955474

The author-archive hash matches the hash independently published by Michael Rubinstein for the archived proof, subject to authentic reference publication. This establishes byte identity relative to the cited hash, not original authorship, a digital signature, distribution permission, or correctness of all external claims. The Git commit is a **local mirror identity**, not proof of an original-author Git release.

### Exact scope of named theorem checks

The local certificate reports successful Lean checking of these five declarations:

1. riemannHypothesis
2. riemannZeta_eq_zero_re
3. LFunction_ne_zero_of_half_lt_re
4. LFunction_eq_zero_re
5. LFunction_eq_zero_re_of_isPrimitive

The axiom checks report only propext, Classical.choice, and Quot.sound as dependencies of each listed declaration. Axiom checks alone do not establish that a named theorem states the mathematically intended proposition. The recorded separate Lean invocation also explicitly checked the type of riemannHypothesis against Mathlib's RiemannHypothesis declaration. The scope concerns the zeta-function RH and the stated Dirichlet L-function generalization, not analogous results for every automorphic, Hecke, or Dedekind L-function.

### Other researchers' independent checkers

Andrew Sutherland of MIT publicly reports using the different Lean proof-checking implementations nanoda, con-leche and con-ron to check proof exports and separately comparing statements. This report attributes those tests only to Sutherland. **Aether did not run these independent kernels locally**, and the present Aether report does not independently attest to Sutherland's checker source or execution logs.

External references:
- https://math.mit.edu/~drew/grh/
- https://mrubinst.github.io/grh-lean-verification/
- https://leanprover-community.github.io/blog/posts/riemann-hypothesis/

### Aether-native independent publication review

Aether R10 Swarm V2 executed an evidence lead, a distinct adversarial reviewer, and a final integrator in a source-pinned native mission. The original live peer board recorded genuine agent messages and peer-causal handoffs. Three separate deterministic independent verifier receipts were accepted. The previously failed R1 and R1b/R1c campaign journals were retained; this accepted successor did not overwrite or reset them.

The three accepted task receipts verify process provenance and review-message consistency, **not** independently prove the mathematics, authenticate original authorship, or establish a different-kernel proof check. The reviewers' output was technical and scientific writing feedback; the operator separately checked the machine evidence hashes and original source pins.

### Reproducibility package and limitations

The exact certificate, build status, axiom log, SHA-256 manifest, and native review provenance accompany this report. The complete source build log and internal review transcripts remain in a restricted evidence archive; their original SHA-256 digests are included for audit requests. Original third-party Lean proof source, compiled objects, credentials and code from other authors are excluded from this package.

This publication does not claim Aether solved, discovered or first verified the Riemann Hypothesis. No original mathematical authorship, source license, or redistribution rights are transferred. The original proof source is excluded. No Zenodo DOI is claimed until an independently confirmed Zenodo record exists. The private Aether engineering repository and its production releases remain unchanged.

### Publication and permanent citation

The source-free public repository is https://github.com/Chrisbryan17/aether-verification-reports, with this first report under GitHub release tag `v1.0.0`. Read the source-pinned evidence logs and exact file hashes from the repository and the tagged release. A future separate-kernel run under Aether can extend this infrastructure capability, but the current report does not claim such a run.

The `source-reproducibility.json` and original certificate preserve their *prepublication audit snapshot*, including historical `public_release_authorized=false` fields. Those are evidence about the original audit's state, not a statement of GitHub repository visibility or an implicit copyright transfer. Zenodo archiving and community discussion remain separate downstream actions and no DOI has been assigned by this release.
