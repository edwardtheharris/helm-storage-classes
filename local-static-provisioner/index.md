---
abstract: Local Static Provisioner, values and templates.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-04-28
title: Local Static Provisioner and Templates
---

This service enables easier use of static local storage provisioning to
provide a slightly more dynamic usage.

## Local Static Provisioner Chart

This chart deploys a `DaemonSet` that handles provisioning of local storage
resources.

```{autoyaml} local-static-provisioner/Chart.yaml
```

## Local Static Provisioner Values

You can adjust the deployment of the local static provisioner with the contents
of the file {file}`local-static-provisioner/values.yaml`.

```{autoyaml} local-static-provisioner/values.yaml
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
