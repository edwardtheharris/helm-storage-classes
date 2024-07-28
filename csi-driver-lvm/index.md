---
abstract: This file contains an example of available CSI Driver LVM values.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-07-21
title: CSI Driver LVM values
---

## {term}`csi-driver-lvm`

```{sidebar} default values
Local volume dynamic provisioning is handled using the
{term}`csi-driver-lvm` CSI Driver provided
by [Metal Stack](https://github.com/metal-stack/).

The complete list of possible settings for {term}`csi-driver-lvm` can be found
[here](https://github.com/metal-stack/helm-charts/blob/master/charts/csi-driver-lvm/values.yaml).

An example with default values is available to the left.

To update configuration for this driver, change any of the corresponding
values in the main values file at the root of this repository.
```

```{autoyaml} csi-driver-lvm/values.yaml
```
