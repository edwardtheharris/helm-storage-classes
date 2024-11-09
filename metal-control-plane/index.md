---
abstract: Metal Stack Control Plane Helm Chart docs
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-04-28
title: Metal Control Plane
---

This driver requires that LVM be deployed on the nodes it runs on.

## MCP Helm Chart

This chart deploys a `DaemonSet` that handles provisioning of local storage
resources.

```{autoyaml} metal-control-plane/Chart.yaml
```

## MCP Values

You can adjust the deployment of the CSI driver LVM with the contents
of the file {file}`metal-control-plane/values.yaml`.

```{autoyaml} metal-control-plane/values.yaml
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
