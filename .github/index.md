---
abstract: CI/CD usage guide.
authors: Xander Harris
date: 2024-04-28
title: Continuous Integration and Delivery
---

## GitHub Actions Workflows

The following GHA workflows are used in this repository for CI/CD purposes.

### Helm Workflow

[![Helm](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/helm.yml?branch=main&style=flat-square&logo=helm&logoColor=%230F1689&logoSize=auto&label=helm)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/helm.yml)

This runs `helm lint` and `helm unittest`.

```{autoyaml} .github/workflows/helm.yml
```

### Documentation Workflow

[![Documentation](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/documentation.yml?branch=main&style=flat-square&logo=githubpages&logoColor=%23222222&logoSize=auto&label=Documentation)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/documentation.yml)

This generates and deploys the documentation for the Helm Charts in this repo.

```{autoyaml} .github/workflows/documentation.yml
```

## Dependabot Settings

Dependabot manages dependency updates.

```{autoyaml} .github/dependabot.yml
```
