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
