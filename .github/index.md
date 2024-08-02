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

### Kind Workflow

[![Kind](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/kind.yml?branch=main&style=flat-square&logo=kubernetes&logoColor=%23326CE5&logoSize=auto&label=Kind)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/kind.yml)

This workflow starts a Kind cluster and deploys the package to it.

```{autoyaml} .github/workflows/kind.yml
```

### OSSAR Workflow

[![OSSAR](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/ossar.yml?branch=main&style=flat-square&logo=githubactions&logoColor=%230F1689&logoSize=auto&label=OSSAR)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/ossar.yml)

```{autoyaml} .github/workflows/ossar.yml
```

### Pages Workflow

[![GitHub Pages](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/ossar.yml?branch=main&style=flat-square&logo=githubpages&logoColor=%23222222&logoSize=auto&label=GitHub%20Pages)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/pages.yml)

This generates and deploys the documentation for the Helm Charts in this repo.

```{autoyaml} .github/workflows/pages.yml
```

## Dependabot Settings

Dependabot manages dependency updates.

```{autoyaml} .github/dependabot.yml
```
