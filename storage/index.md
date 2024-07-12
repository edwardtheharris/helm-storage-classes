---
abstract: Storage Chart, values and templates.
authors: Xander Harris
date: 2024-04-28
title: Storage Chart and Templates
---

## Usage

To install this chart you can run the following command from the root
of this repository.

```{code-block} shell
helm install --update storage storage/
```

This will install the `StorageClass` objects described in the file
{file}`storage/templates/storageClass.yaml`, then use them to create
`PersistentVolumes` as appropriate for the nodes in your cluster and described in the file {file}`storage/templates/persistentVolume.yaml`.

### Chart

```{autoyaml} storage/Chart.yaml
```

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
