---
abstract: A brief guide to using local nfs shares in bare-metal k8s.
title: nfs csi driver readme
---

1. Add the nfs-subdir-external-provisioner helm repository.

   ```{code-block} shell
   helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
   ```

2. Install the provisioner.

   ```{code-block} shell
   helm install csi-driver-nfs csi-driver-nfs/csi-driver-nfs --namespace kube-system --version 4.12.0
   ```

More information is available from the
[related documentation](https://github.com/kubernetes-csi/csi-driver-nfs/tree/master/charts).
