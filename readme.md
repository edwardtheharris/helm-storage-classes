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

[![GitHub Actions OSSAR](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/ossar.yml?branch=main&style=flat&logo=githubactions&logoColor=%232088FF&label=OSSAR)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/ossar.yml)
[![GitHub Pages](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/pages.yml?branch=main&style=flat&logo=githubpages&logoColor=%23222222&label=GitHub%20Pages)](https://edwardtheharris.github.io/helm-storage-classes/)
[![Helm Test and Unittest](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/helm.yml?branch=main&style=flat&logo=helm&logoColor=%230F1689&label=Helm&color=%230F1689)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/helm.yml)

## Helm Charts for Static and Dynamic Storage Classes

Presently this includes a provisioner for local static storage as well as
a CSI driver for dynamically provisioning Linux LVM storage.

For more information, see the full documentation
[here](https://edwardtheharris.github.io/helm-storage-classes/).

### Install

To install this application, you can follow these steps.

1. Have a Kubernetes cluster that needs StorageClass objects.
2. Create a namespace in that cluster called `csi-driver-lvm`

   ```shell
   kubectl create ns csi-driver-lvm
   ```

3. Install the `lvm` app into the `csi-driver-lvm` namespace.

   ```shell
   helm -n csi-driver-lvm upgrade --install lvm .
   ```

4. Run the provided test suites.

   ```shell
   helm -n csi-driver-lvm test lvm
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

You will likely need to update the values contained in the file
{file}`values.yaml` file to suit your local cluster.

### Uninstall

Uninstall the application.

```shell
helm -n kube-system uninstall storage
```

### Test

Test the application.

```shell
helm -n kube-system test storage
```
