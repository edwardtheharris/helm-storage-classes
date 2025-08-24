---
abstract: >-
    This is the readme for the Helm Charts in this repository that can
    be used to deploy Static and Dynamic Storage Classes to bare metal
    Kubernetes clusters.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-07-18
title: Readme
---

[![Documentation](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/documentation.yml/badge.svg)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/documentation.yml)
[![Test Helm Chart](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/helm.yml/badge.svg)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/helm.yml)
[![wakatime](https://wakatime.com/badge/github/edwardtheharris/helm-storage-classes.svg)](https://wakatime.com/badge/github/edwardtheharris/helm-storage-classes)

## Helm Charts for Static and Dynamic Storage Classes

Presently this includes a provisioner for local static storage as well as
a {term}`CSI` driver for dynamically provisioning Linux {term}`LVM` storage.

For more information, see the full documentation
[on GitHub Pages](https://edwardtheharris.github.io/helm-storage-classes/).

### Pre-Install

For the sake of the author's convenience, install instructions will assume that
you have already completed the following steps on an {term}`ArchLinux` system.

1. Install [kubie](https://github.com/sbstp/kubie)

   ```{code-block} shell
   yay -S kubie
   ```

2. Update your {term}`kubie` context so it points to your cluster.

   ```{code-block}
   kubie ctx
   ```

### Install

To install this application, you can follow these steps. The {term}`CSI` {term}`LVM` driver
supports 3 volume modes (linear, striped, mirror). All three are enabled by
default. The local static provisioner is disabled by default.

1. Have a {term}`Kubernetes` cluster that needs {term}`StorageClass` objects.
2. On at least one node in your cluster provision a Volume Group that matches
   the name you've provided in the `csi-driver-lvm.lvm.vgName`{l=yaml} setting in
   {file}`values.yaml`. For best results, provision this volume group on all of the
   nodes in your cluster on which you intend to run this application.
3. Create a namespace in that cluster called `storage`

   ```shell
   kubectl create ns storage
   ```

4. Change your namespace in {term}`kubie`.

   ```{code-block}
   kubie ns storage
   ```

5. You will likely need to update the values contained in the file
   {file}`values.yaml` file to suit your local cluster. Prior to installing
   the application would be a good time for that.
6. Install the `csi-lvm` app into the `storage` namespace.

   ```shell
   helm upgrade --install csi-lvm .
   ```

6. Run the provided test suites.
   1. Start with the basic Helm tests.

      ```shell
      helm test lvm
      ```

      If things went well, you should see output similar to this.

      ```shell
      NAME: lvm
      LAST DEPLOYED: Sun Jul 28 15:43:34 2024
      NAMESPACE: csi-driver-lvm
      STATUS: deployed
      REVISION: 9
      TEST SUITE:     csi-driver-lvm-pod-test
      Last Started:   Mon Jul 29 07:31:39 2024
      Last Completed: Mon Jul 29 07:31:39 2024
      Phase:          Succeeded
      TEST SUITE:     csi-driver-lvm-pod-test
      Last Started:   Mon Jul 29 07:31:39 2024
      Last Completed: Mon Jul 29 07:31:49 2024
      Phase:          Succeeded
      TEST SUITE:     csi-driver-lvm-sts-test
      Last Started:   Mon Jul 29 07:31:49 2024
      Last Completed: Mon Jul 29 07:31:49 2024
      Phase:          Succeeded
      ```

   2. Install the
      [Helm unittest](https://github.com/helm-unittest/helm-unittest) plugin.

      ```shell
      helm plugin install https://github.com/helm-unittest/helm-unittest
      ```

   3. Run the included unit tests.

      ```shell
      helm unittest -f 'tests/*.yaml' csi-driver-lvm/
      ```

      If things went well, you should see output similar to this.

      ```shell
      ### Chart [ lvm ] .

      PASS  CSI Driver LVM StatefulSet Test Suite    tests/controller_test.yaml
      PASS  CSI Driver LVM CSIDriver Test Suite      tests/driver_test.yaml
      PASS  CSI Driver LVM Test Suite        tests/manifest_test.yaml
      PASS  CSI Driver LVM DaemonSet Test Suite      tests/plugin_test.yaml
      PASS  CSI Driver LVM Role Test Suite   tests/role_test.yaml
      PASS  CSI Driver LVM Test Suite        tests/storageClass_test.yaml
      PASS  CSI Driver LVM StorageClasses Test Suite tests/storageclasses_test.yaml
      PASS  CSI Driver LVM Test Suite        tests/sts_test.yaml

      Charts:      1 passed, 1 total
      Test Suites: 8 passed, 8 total
      Tests:       41 passed, 41 total
      Snapshot:    0 passed, 0 total
      Time:        261.729855ms
      ```

Now, you can dynamically provision `PersistentVolumeClaims`{l=yaml} for any node in your
cluster that has a Volume Group with the same name as the value of
`csi-driver-lvm.lvm.vgName`{l=yaml} in your {file}`values.yaml` file.

See the test files in the `templates/` directory for examples.

### Uninstall

Uninstall the application.

```shell
helm uninstall storage
```
