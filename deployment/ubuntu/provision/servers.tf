# Copyright 2021 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

resource "digitalocean_droplet" "cattle" {

  image = var.image

  name = "${var.name}"

  region = var.region

  ipv6 = true

  monitoring = true

  size = var.droplet_size

  ssh_keys = [data.digitalocean_ssh_key.main.id]

  vpc_uuid = digitalocean_vpc.cattle_infra.id
}

resource "digitalocean_floating_ip" "cattle" {

  droplet_id = digitalocean_droplet.cattle.id

  region     = digitalocean_droplet.cattle.region
}
