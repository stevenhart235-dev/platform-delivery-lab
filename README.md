# Platform Delivery Lab

A small, personal learning repo for exploring standardized GitHub delivery, governance metadata, and eventual AKS target selection. No cloud infrastructure is created in milestone 1.

## Milestone 1: one working CI pipeline

- `apps/sample-api/sample_api.py`: dependency-free HTTP service with `/health` endpoint.
- `tests/test_sample_api.py`: unit tests.
- `.github/workflows/ci.yml`: runs on pull requests and pushes to `main`.

### Try it locally

```bash
python -m unittest discover -s tests -v
python apps/sample-api/sample_api.py
# In another terminal: curl http://localhost:8080/health
```

### Push to a new personal GitHub repo

Create an **empty** GitHub repo called `platform-delivery-lab` (do not initialize with a README), then run from this folder:

```bash
git init
git branch -M main
git add .
git commit -m "lab: establish baseline CI"
git remote add origin https://github.com/YOUR_USERNAME/platform-delivery-lab.git
git push -u origin main
```

Visit the repo's **Actions** tab and open `CI - sample API`. For pull-request behavior, create a feature branch, commit a small change, push it, and open a PR.

## Planned (not implemented yet)

1. Extract a reusable workflow and a caller workflow.
2. Validate workload metadata and tags.
3. Map approved workload types to simulated AKS targets.
4. Generate a deployment plan, without deploying real clusters.

Keep company code, secrets, internal hostnames, subscription IDs, and configuration out of this personal repository.
