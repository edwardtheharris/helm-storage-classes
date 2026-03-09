---
date: 2025-12-01
title: Index for Rook Operator Helm Chart
---

```{note}
Given the paucity of information available in the doucment presently
it is likely that the
[official rook helm chart docs](https://github.com/rook/rook/blob/master/Documentation/Helm-Charts/operator-chart.md)
may be of more use.
```

```{block-quote}
We promise not to turn it into a thing if you decide to use the actual docs instead of
this blank-ass shit right here. Pinky swear.

-- ed
```

## Getting started

So there are two things here, of which this is the first, being the Rook Operator. Once this is deployed and you can verify
that it is working, you'll be able to deploy a Ceph Cluster to your Kubernetes Cluster assuming it is a near-complete match
for the author's hardware and software configuration choices (bare-metal, Arch Linux, you probably don't need to know any
more than that.

### Thing the first

Since there's no getting around this operator we're going to have to make it work,
we'll try to describe the simplest process for that here. Most likely we'll fail.

```{block-quote}
The editorial board would like to note that there is only one author of this document
as well as our frequent and ignored suggestions that the second-person isn't necessarily
the best, uh, person in which to write documentation.

-- ed
```

```{block-quote}
The author would like to tell the editorial board to fuck off as he'll be using whichever
. . . person he pleases while writing this filthy document. Ban this sick filth.

-- author
```

On the surface the process should be simple enough. You'll need to add the helm repository for
the rook operator chart (which also contains the ceph cluster chart), to your local
helm repository list, then update the provided {file}`values.yaml` file to suit your needs,
install the operator with helm and verify it. Likely it's that last step that we'll get hung up
on if experience is any guide. That is if the squirrels don't get us first.

1. Add the rook operator helm repository.

   ```{code-block} shell
   :caption: we'll call it rook for short
   helm repo add rook https://charts.rook.io/release
   ```

2. Update your local repository list.

   ```{code-block} shell
   :caption: update the usual way
   helm repo update
   ```

3. Configure your {file}`values.yaml`.

   ```{block-quote}
   We're not here to tell you how to do this, after all there are a near infinite
   varieties of text editors to choose from, so you should probably just use
   whatever makes sense to you. Just know that if that's not some version of VIM,
   we'll know and you should also know that we know that revenge is a dish best
   served with text editors from the 70's, or cold or whatever. Go to hell.

   -- author
   ```

4. Create a namespace on your cluster called `rook-ceph`.

   ```{code-block} shell
   :caption: ns rook-ceph, they were very clear about this

   kubectl create ns rook-ceph
   ```

5. Deploy the rook operator to your cluster.

   ```{code-block} shell
   helm upgrade --install rook rook/rook-ceph -f values.yaml
   ```

   Keep running that until it works, you know how to debug a helm chart
   or you wouldn't have made it this far. Once it's working, we'll
   double-check that it's operating.

6. Validate the deployment.

   ```{code-block} shell
   ```

## Rook Operator Chart Values

```{autoyaml} /rook/values.yaml
```
