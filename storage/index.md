---
abstract: Storage Chart, values and templates.
authors: Xander Harris
date: 2024-04-28
title: Storage Chart and Templates
---

## Storage Contents

```{toctree}
local-static-provisioner/index
```

## Usage

To install this chart you can run the following command from the root
of this repository.

```{code-block} shell
helm dependency update storage storage/
helm upgrade --install storage storage/
```

This will install the `StorageClass` objects described in the file
{file}`storage/templates/storageClass.yaml`, then use them to create
`PersistentVolumes` as appropriate for the nodes in your cluster
and described in the file {file}`storage/templates/persistentVolume.yaml`[^pv].

```{note}
The default values are those used with the author's personal cluster
and should be changed in the {file}`storage/values.yaml`
```

### Chart

```{autoyaml} storage/Chart.yaml
```

#### Sub Charts

Local volume dynamic provisioning is handled using the
[csi-driver-lvm](https://github.com/metal-stack/helm-charts/tree/master/charts/csi-driver-lvm)
CSI Driver.

#### Values

```{autoyaml} storage/values.yaml
```

#### Templates

```{rubric} HDD
```

---

This class is meant for any magnetic storage, though it is probably
mounted via USB like the USB storage class that class is intended
for non-magnetic storage.

```{code-block} yaml
:caption: local hard disk drive (magnetic)

apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
    storageclass.kubernetes.io/name: hdd
    storageclass.kubernetes.io/provisioner: local
    storageclass.kubernetes.io/type: magnetic
  name: "hdd"
provisioner: kubernetes.io/no-provisioner
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
```

---

```{rubric} Local
```

---

This is the default storage class.

```{code-block} yaml
:caption: local partition available per node

apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
    storageclass.kubernetes.io/name: local
    storageclass.kubernetes.io/provisioner: local
    storageclass.kubernetes.io/type: ssd
  name: local
provisioner: kubernetes.io/no-provisioner
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
```

```{rubric} USB
```

---

```{code-block} yaml
:caption: removable storage mounted via USB

apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
    storageclass.kubernetes.io/name: usb
    storageclass.kubernetes.io/provisioner: removable
    storageclass.kubernetes.io/type: ssd
  name: usb
provisioner: kubernetes.io/no-provisioner
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
```

## Local Provisioner Plugin

This chart depends on the static local provisioner plugin described in detail
[here](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner/blob/master/helm/README.md).

The helm chart and templates are located in {file}`local-static-provisioner`.

[^pv]: Information about the `range` function can be found in the
    [Helm docs](https://helm.sh/docs/chart_template_guide/control_structures/#looping-with-the-range-action).
