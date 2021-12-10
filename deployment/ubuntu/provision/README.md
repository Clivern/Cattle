### Provision Steps

1. Create `terraform.tfvars` and define required vars.

```bash
region = "nyc3"
ssh_key = "clivern"
name = "cattle.sh"
droplet_size = "s-1vcpu-2gb"
image = "ubuntu-20-04-x64"
```

2. Create a digitalocean token from digitalocean dashboard and then run `terraform init`.

3. Run `terraform plan` to check the changes.

4. Run `terraform apply` to perform the action.
