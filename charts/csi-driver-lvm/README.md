---
abstract: A helm chart for the CSI LVM Driver.
authors: Xander Harris
date: 2024-04-28
title: CSI Driver LVM Helm Chart
---

This is the helm chart for the deployment of
[csi-driver-lvm](https://github.com/metal-stack/csi-driver-lvm).

**The chart requires that you have at least Kubernetes 1.16.**

## TL;DR

```{code-block} shell
helm install csi-driver-lvm csi-driver-lvm -n csi-driver-lvm --repo https://helm.metal-stack.io/csi-driver-lvm
```
