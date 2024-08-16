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
:caption: Helm Charts

csi-driver-lvm/index
local-static-provisioner/index
metal-control-plane/index
```

```{contents}
```

````{sidebar} Indices and tables
```{list-table}
* - {ref}`genindex`
* - {ref}`modindex`
* - {ref}`search`
````

```{toctree}
:caption: Meta Pages

.github/index
license
readme
security
```

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

DaemonSet
   A Kubernetes workload object that is intended to run on all nodes in a
   cluster by default. Can be configured to ignore control plane nodes.
   More information is available
   [here](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

kubelet
   An application that must run on every node in a Kubernetes cluster,
   responsible for interfacing with the container runtime and the other
   components of Kubernetes.

LVM
   Logical Volume Manager, described in more detail
   [here](https://wiki.archlinux.org/title/LVM)

NFS
   Network File Storage, described in more detail
   [here](https://wiki.archlinux.org/title/NFS).

OSSAR
   Open Source Static Analysis Runner, runs GitHub Actions Open Source Static
   Analysis tools on your repository. More information
   [here](https://github.com/github/ossar-action)

RAID
   Redundant Array of Inexpensive Disks is a method of clustering cheap and
   easily replaced disks into an array that appears to an operating system
   as a single disk. More information is available
   [here](https://en.wikipedia.org/wiki/RAID).

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

Taint
   A condition applied to a Kubernetes node that can be used to prevent
   certain workloads from being run on it. More information is available
   [here](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

Tolerations
   A condition that can be apply to a Kubernetes workload that can be used
   to allow certain workloads to ignore a {term}`Taint` that has been applied
   to a node. More information is available
   [here](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).
```

## Local Chart Values

```{autoyaml} values.yaml
```

### Local Provisioner Plugin

This chart depends on the static local provisioner plugin described in detail
[here](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner/blob/master/helm/README.md).

The helm chart and templates are located in
{file}`charts/local-static-provisioner`.
