# eg-router-benchmark

## static

vm1 static 2.6w/tps
http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca

./hey -n 900 -c 50 -m GET http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 24068.3219

./hey -n 90000 -c 100 -m GET http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 26077.3742

./hey -n 90000 -c 120 -m GET http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 27219.1946

vm2 static 2.7w/tps

http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca

./hey -n 900 -c 50 -m GET http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 25078.4517

./hey -n 90000 -c 100 -m GET http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 27391.6867

./hey -n 90000 -c 120 -m GET http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 27401.6701

vm3 static 6.5w/tps

http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca

./hey -n 900 -c 50 -m GET http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 41687.5741

./hey -n 90000 -c 100 -m GET http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 65122.1171

./hey -n 90000 -c 120 -m GET http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca
> 65638.4786
