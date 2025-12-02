---
date: 2025-12-01
title: Rook Ceph Cluster Helm Chart Index
---

```{toctree}
readme
```

This document will hopefully contain something like the path of
minimum time sailed for a working Ceph cluster with an object store.
The author doesn't need anything but the object store, so the other features
will be ignored for the purposes of this document. Go read someone else's
docs if you have a problem that, right after you go to hell.

## Thing the first

Before you start on any of this nonsense here, make sure you've already
finished [that other nonsense over there](path:/rook/index.md).
Which nonsense ought to have left you with a fully armed and operational
rook operator. You'll definitely need one of those to make this bit work,
so we hope you have one.

## Reference material

Whatever the case, the [CephCluster CRD manual](https://rook.io/docs/rook/latest/CRDs/Cluster/ceph-cluster-crd/)
will be something you'll want to keep handy as it is quite complex.


