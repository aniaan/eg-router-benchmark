# benchmark

## Preparing

(4core/32GB/) * 4

| Name        | port  | vm   | version              |
| ----------- | ----- | ---- | -------------------- |
| ordered-v1  | 10080 | vm1   | main(golang 1.18.7) |
| ordered-v2  | 10080 | vm2   | feat/router(golang 1.18.7) |
| radixtree   | 10080 | vm3   | feat/router(golang 1.18.7)         |
| hey         | -     | vm4   | v0.1.4              |

[case](https://github.com/aniaan/eg-router-benchmark.git)

Start up the easegress server on vm1, vm2, vm3 and create the `mock-pipeline`

```shell
egctl object create -f eg-router-benchmark/static/mock-pipe.yaml
```

## Summary

The performance of `ordered-v1` and `ordered-v2` is basically the same, and the performance of `radixtree` is much better than them.

static: `radixtree` is about 3 times the performance of `ordered`
prefix: `radixtree` is about 3 times the performance of `ordered`
regexp: `radixtree` is about 40 times the performance of `ordered`

## static

The test case for static routes will create 10000 routes with md5 values from 1 to 10000, and test requests will be accessed using md5 values of 5000.

### 1. ordered-v1

vm1:

```shell
egctl object create -f eg-router-benchmark/static/order.yaml
```

**stress test**

vm4:

url:  `http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca`

eg: `./hey -n 900 -c 50 -m GET http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 24068.3219   |
| 90000  | 100 | 26077.3742   |
| 90000   | 120 | 27219.1946   |

### 2. ordered-v2

vm2:

```shell
egctl object create -f eg-router-benchmark/static/order.yaml
```

**stress test**

vm4:

url:  `http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca`

eg: `./hey -n 900 -c 50 -m GET http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 25078.4517   |
| 90000  | 100 | 27391.6867   |
| 90000   | 120 | 27401.6701   |

### 3. radixtree

vm3:

```shell
egctl object create -f eg-router-benchmark/static/redixtree.yaml
```

**stress test**

vm4:

url:  `http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca`

eg: `./hey -n 900 -c 50 -m GET http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 41687.5741   |
| 90000  | 100 | 65122.1171   |
| 90000   | 120 | 65638.4786   |

## prefix

The test case for prefix-matching routes will create 10000 routes with md5 values from 1 to 10000, and test requests will be accessed using md5 values of 5000

### 1. ordered-v1

vm1:

```shell
egctl object create -f eg-router-benchmark/prefix/order.yaml
```

**stress test**

vm4:

url:  `http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix`

eg: `./hey -n 900 -c 50 -m GET http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 22110.7111   |
| 90000  | 100 | 26023.5309   |
| 90000   | 120 | 26016.2430   |

### 2. ordered-v2

vm2:

```shell
egctl object create -f eg-router-benchmark/prefix/order.yaml
```

**stress test**

vm4:

url:  `http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix`

eg: `./hey -n 900 -c 50 -m GET http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 25449.3521  |
| 90000  | 100 | 28119.3687   |
| 90000   | 120 | 27882.9445   |

### 3. radixtree

vm3:

```shell
egctl object create -f eg-router-benchmark/prefix/redixtree.yaml
```

**stress test**

vm4:

url:  `http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix`

eg: `./hey -n 900 -c 50 -m GET http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 36541.2653   |
| 90000  | 100 | 58698.0033   |
| 90000   | 120 | 65060.4261   |

## regexp

The test case for regular matching routes will create 10000 RESTful style routes with the template `/users/{username}/<i>` and the test requests will be accessed using the md5 value of 5000

### 1. ordered-v1

vm1:

```shell
egctl object create -f eg-router-benchmark/regexp/order.yaml
```

**stress test**

vm4:

url:  `http://vm-1:10080/users/aniaan/5000`

eg: `./hey -n 900 -c 50 -m GET http://vm-1:10080/users/aniaan/5000`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 1769.1021   |
| 90000  | 100 | 1743.7057   |
| 90000   | 120 | 1743.2940   |

### 2. ordered-v2

vm2:

```shell
egctl object create -f eg-router-benchmark/regexp/order.yaml
```

**stress test**

vm4:

url:  `http://vm-2:10080/users/aniaan/5000`

eg: `./hey -n 900 -c 50 -m GET http://vm-2:10080/users/aniaan/5000`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 1733.3634   |
| 90000  | 100 | 1707.0785   |
| 90000   | 120 | 1686.6228   |

### 2. radixtree

vm3:

```shell
egctl object create -f eg-router-benchmark/regexp/radixtree.yaml
```

**stress test**

vm4:

url:  `http://vm-3:10080/users/aniaan/5000`

eg: `./hey -n 900 -c 50 -m GET http://vm-3:10080/users/aniaan/5000`

| requests    | concurrency  | tps   |
| ----------- | ----- | ---- |
| 900         | 50    | 38619.2734   |
| 90000  | 100 | 66155.8978   |
| 90000   | 120 | 66357.7316   |
