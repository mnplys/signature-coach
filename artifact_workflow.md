# Artifact Workflow

This document explains the workflow of adding, signing, and verifying artifacts:

1. Place your artifact files in `artifacts/`
2. Run `python scripts/sign_artifacts.py` to generate SHA-256 signatures
3. Verify integrity at any time with `python scripts/verify_artifacts.py`
4. All artifacts are version-controlled and MIT licensed for safe learning
