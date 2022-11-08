import hashlib
import json
from ruamel.yaml import YAML


def gen_ordered_router_rules(count: int = 10000):

    config = {
        "kind": "HTTPServer",
        "name": "server-demo",
        "port": 10080,
        "keepAlive": True,
        "https": False,
    }

    paths = []
    for i in range(1, count + 1):
        path = "^/users/([a-z]+)/" + str(i) + "$"
        paths.append({"pathRegexp": path, "backend": "mock", "methods": ["GET"]})

    config["rules"] = [{"paths": paths}]

    with open("./regexp/order.yaml", "w") as out:
        yaml = YAML()
        yaml.dump(config, out)


def gen_radix_tree_router_rules(count: int = 10000):
    config = {
        "kind": "HTTPServer",
        "name": "server-demo",
        "port": 10080,
        "keepAlive": True,
        "https": False,
        "routerKind": "RadixTree",
    }

    paths = []
    for i in range(1, count + 1):
        path = "/users" + "/{name:^[a-z]+}/" + str(i)
        paths.append({"path": path, "backend": "mock", "methods": ["GET"]})

    config["rules"] = [{"paths": paths}]

    with open("./regexp/radixtree.yaml", "w") as out:
        yaml = YAML()
        yaml.dump(config, out)


# 5000: a35fe7f7fe8217b4369a0af4244d1fca
if __name__ == "__main__":
    gen_ordered_router_rules()
    gen_radix_tree_router_rules()
