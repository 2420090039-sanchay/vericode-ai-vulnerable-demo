# VeriCode AI Vulnerable Demo

This repository contains intentionally vulnerable Python examples for testing the VeriCode AI security-scanning application.

## Test cases

- `app.py`: SQL injection pattern.
- `config.py`: Hardcoded dummy credentials.
- `server.py`: Unsafe use of `eval()`.

## Purpose

This repository is intended exclusively for authorized educational demonstrations and security-tool testing.

All credentials are synthetic demonstration values. No production credentials or real secrets should be added.

## Expected workflow

1. Submit this repository's GitHub URL to VeriCode AI.
2. Scan the repository using the configured security scanners.
3. Review the detected findings and their severity.
4. Review AI-generated explanations and remediation recommendations.
5. Export the scan report as a PDF.
