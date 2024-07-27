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

```{contents}
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

## Storage Contents

```{toctree}
local-static-provisioner/index
```

## Installation

To install this chart you can run the following command from the root
of this repository.

```{code-block} shell
kubectl create ns storage
helm dependency update storage storage/
helm -n storage upgrade --install storage storage/
```

This will install the {term}`StorageClass` objects described in the file
{file}`templates/service.yaml`, then use them to create
{term}`PersistentVolume`s as appropriate for the nodes in your cluster
and described in the file {file}`storage/templates/persistentVolume.yaml`[^pv].

```{note}
The default values are those used with the author's personal cluster
and should be changed in the {file}`storage/values.yaml`
```

### Testing

You can run the Helm template tests this way.

```{code-block} shell
helm -n storage test storage
```

### Uninstall

To remove all resources deployed with this chart run this.

```{code-block} shell
helm -n storage uninstall storage
```

## Chart

```{autoyaml} storage/Chart.yaml
```

### Sub Charts

Local volume dynamic provisioning is handled using the
[csi-driver-lvm](https://github.com/metal-stack/helm-charts/tree/master/charts/csi-driver-lvm)
CSI Driver.

The complete list of possible settings for {term}`csi-driver-lvm` can be found
[here](https://github.com/metal-stack/helm-charts/blob/master/charts/csi-driver-lvm/values.yaml).

#### Local Chart Values

```{autoyaml} values.yaml
```

#### Local Provisioner Plugin

This chart depends on the static local provisioner plugin described in detail
[here](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner/blob/master/helm/README.md).

The helm chart and templates are located in {file}`local-static-provisioner`.

[^pv]: Information about the `range` function can be found in the
    [Helm docs](https://helm.sh/docs/chart_template_guide/control_structures/#looping-with-the-range-action).
