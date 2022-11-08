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


## prefix

vm1 prefix 2.6w/tps
http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca/abc

./hey -n 900 -c 50 -m GET http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 22110.7111

./hey -n 90000 -c 100 -m GET http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 26023.5309

./hey -n 90000 -c 120 -m GET http://vm-1:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 26016.2430


vm2 prefix 2.7w/tps
http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca/abc

./hey -n 900 -c 50 -m GET http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 25449.3521

./hey -n 90000 -c 100 -m GET http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 28119.3687

./hey -n 90000 -c 120 -m GET http://vm-2:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 27882.9445


vm3 prefix 6.5w/tps
http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca/abc

./hey -n 900 -c 50 -m GET http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 36541.2653

./hey -n 90000 -c 100 -m GET http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 58698.0033

./hey -n 90000 -c 120 -m GET http://vm-3:10080/a35fe7f7fe8217b4369a0af4244d1fca/suffix
> 65060.4261


## regexp

vm1 regexp 1700/tps
http://vm-1:10080/users/aniaan/5000

./hey -n 900 -c 50 -m GET http://vm-1:10080/users/aniaan/5000
> 1769.1021

./hey -n 90000 -c 100 -m GET http://vm-1:10080/users/aniaan/5000
> 1743.7057

./hey -n 90000 -c 120 -m GET http://vm-1:10080/users/aniaan/5000
> 1743.2940


vm2 regexp 1700/tps
http://vm-2:10080/users/aniaan/5000

./hey -n 900 -c 50 -m GET http://vm-2:10080/users/aniaan/5000
> 1733.3634

./hey -n 90000 -c 100 -m GET http://vm-2:10080/users/aniaan/5000
> 1707.0785

./hey -n 90000 -c 120 -m GET http://vm-2:10080/users/aniaan/5000
> 1686.6228

vm3 regexp 6w/tps
http://vm-3:10080/users/aniaan/5000

./hey -n 900 -c 50 -m GET http://vm-3:10080/users/aniaan/5000
> 38619.2734

./hey -n 90000 -c 100 -m GET http://vm-3:10080/users/aniaan/5000
> 66155.8978

./hey -n 90000 -c 120 -m GET http://vm-3:10080/users/aniaan/5000
> 66357.7316
