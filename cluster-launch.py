apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
    name: my-cluster-1
    region: us-west-1

nodeGroups:
    - name: small-ng
      instanceType: t2.medium
      desiredCapacity: 2

