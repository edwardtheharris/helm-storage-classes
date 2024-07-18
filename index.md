---
abstract: >-
   Helm Storage Class documentation master file, created by
   sphinx-quickstart on Sun Apr 28 15:35:08 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
authors:
   - name: Xander Harris
     email: xandertheharris@gmail.com
date: 2024-04-28
title: Storage Helm Chart
---

## Repository Contents

```{toctree}
:maxdepth: 2

manifests/index
storage/index
```

### Meta Contents

```{toctree}
cicd
license
readme
security
```

## Indices and tables

* {ref}`genindex`
* {ref}`modindex`
* {ref}`search`

### Glossary

```{glossary}
CSI
   Container Storage Interface, described in more detail
   [here](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/).

CSIDriver
   A driver that enables a Kubernetes cluster to interact with storage devices
   described by the Container Storage Interface. This repository uses
   {term}`csi-driver-lvm` and {term}`csi-driver-nfs`

csi-driver-lvm
   A CSI driver that enables dynamic provisioning of volumes via Logical
   Volume Manager volume groups. More information is available
   [here](https://github.com/metal-stack/csi-driver-lvm).

csi-driver-nfs
   A CSI driver that enables dynamic provisioning of volumes via NFS shares.
   More information is available
   [here](https://github.com/kubernetes-csi/csi-driver-nfs)

LVM
   Logical Volume Manager, described in more detail
   [here](https://wiki.archlinux.org/title/LVM)

NFS
   Network File Storage, described in more detail
   [here](https://wiki.archlinux.org/title/NFS).

PersistentVolume
   A Kubernetes object that is statically defined by a cluster administrator
   and may be bound to a PersistentVolumeClaim at runtime. More information
   is available [here](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

PersistentVolumeClaim
   A Kubernetes object that may refer to a dynamically or statically provisioned
   persistent storage class. More information is available
   [here](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).

StorageClass
   A Kubernetes object that describes a persistent or ephemeral form of storage
   that may be provisioned by a cluster. Described in more detail
   [here](https://kubernetes.io/docs/concepts/storage/storage-classes/#storageclass-objects).
```
