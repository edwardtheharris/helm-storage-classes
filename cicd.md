---
abstract: CI/CD usage guide.
authors: Xander Harris
date: 2024-04-28
title: Continuous Integration and Delivery
---

## GitHub Actions Workflows

The following GHA workflows are used in this repository for CI/CD purposes.

### Helm Workflow

This runs `helm lint` and `helm unittest`.

```{autoyaml} .github/workflows/helm.yml
```

### OSSAR Workflow

```{autoyaml} .github/workflows/ossar.yml
```

### Pages Workflow

This generates and deploys the documentation for the Helm Charts in this repo.

```{autoyaml} .github/workflows/pages.yml
```

## Dependabot Settings

Dependabot manages dependency updates.

```{autoyaml} .github/dependabot.yml
```
