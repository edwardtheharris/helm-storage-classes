---
abstract: >-
    This is the readme for the Helm Charts in this repository that can
    be used to deploy Static and Dynamic Storage Classes to bare metal
    Kubernetes clusters.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-07-18
title: Helm Charts for Static and Dynamic Storage Classes
---

## Chart Usage

To install this application, you can follow these steps.

```shell
kubectl create ns storage
helm -n storage upgrade --install storage storage/
```

You will likely need to update the values contained in the file
{file}`storage/values.yaml` file to suit your local cluster.
