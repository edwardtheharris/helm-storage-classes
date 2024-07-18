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

```{list-table}
* - [![GitHub Actions OSSAR](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/ossar.yml?branch=main&style=flat&logo=githubactions&logoColor=%232088FF&label=OSSAR)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/ossar.yml)
  - [![GitHub Pages](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/pages.yml?branch=main&style=flat&logo=githubpages&logoColor=%23222222&label=GitHub%20Pages)](https://edwardtheharris.github.io/helm-storage-classes/)
  - [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/edwardtheharris/helm-storage-classes/helm.yml?branch=main&style=flat&logo=helm&logoColor=%230F1689&label=Helm&color=%230F1689)](https://github.com/edwardtheharris/helm-storage-classes/actions/workflows/helm.yml)

```

## Helm Charts for Static and Dynamic Storage Classes

Presently this includes a provisioner for local static storage as well as
a CSI driver for dynamically provisioning Linux LVM storage.

### Install

To install this application, you can follow these steps.

1. Create a namespace called `storage`.

   ```shell
   kubectl create ns storage
   ```

2. Install the `storage` app into the `storage` namespace.

   ```shell
   helm -n storage upgrade --install storage storage/
   ```

3. Run the provided test suites.

   ```sh
   helm -n storage test storage
   ```

You will likely need to update the values contained in the file
{file}`storage/values.yaml` file to suit your local cluster.

### Uninstall

Uninstall the application.

```shell
helm -n storage uninstall storage
```
