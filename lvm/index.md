---
abstract: CSI Driver LVM docs index
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-04-28
title: CSI driver LVM
---

This driver requires that LVM be deployed on the nodes it runs on.

## CSI driver LVM Chart

This chart deploys a `DaemonSet` that handles provisioning of local storage
resources.

```{autoyaml} lvm/Chart.yaml
```

## CSI driver LVM Values

You can adjust the deployment of the CSI driver LVM with the contents
of the file {file}`lvm/values.yaml`.

```{autoyaml} csi-driver-lvm/values.yaml
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```

```{toctree}
:caption: readme

readme
```
