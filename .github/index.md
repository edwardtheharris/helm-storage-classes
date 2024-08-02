---
abstract: CI/CD usage guide.
authors: Xander Harris
date: 2024-04-28
title: Continuous Integration and Delivery
---

## GitHub Actions Workflows

The following GHA workflows are used in this repository for CI/CD purposes.

### CodeQL

[![CodeQL](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/codeql.yml?branch=main&style=flat-square&logoSize=auto&logo=githubactions)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/codeql.yml)

```{autoyaml} .github/workflows/codeql.yml
```

### Helm Workflow

[![Helm](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/helm.yml?branch=main&style=flat-square&logo=helm&logoColor=%230F1689&logoSize=auto&label=helm)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/helm.yml)

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
