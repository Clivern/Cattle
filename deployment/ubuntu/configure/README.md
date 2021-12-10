### Configure Steps

1. Setup servers

```bash
$ echo "[cattle_server]
x.x.x.x     ansible_connection=ssh        ansible_user=root    ansible_python_interpreter=/usr/bin/python3" > hosts.prod
```

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ make config
$ make configure
```

Access the server

```bash
$ ssh root@x.x.x.x
```

To lint the code

```bash
$ make lint
```
