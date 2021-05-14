# Tangrama: MOTD

Configures MOTD of a server

This playbook produces the `/etc/motd` file looking like this:

```
********************************************************

Welcome to tupi!

 Hostname: tupi
 FQDN:    nyt.example.local
 Distro:  Ubuntu 16.04 xenial
 Virtual: YES

 CPUs:    2
 RAM:     2.0GB
 Service: example.com

Last Ansible provisioning: 2021-04-01T09:38:53Z

********************************************************

```

## Role Variables

- `motd_info`: List of additional information to show.

Look into the `defaults` for an example.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: tangrama.motd  }

If you want to change the defaults, please configure them in the _VARS_ of the playbook:

Example playbook:

```yml

- hosts: "{{ target }}"
  remote_user: admin
  become: true
  gather_facts: true
    vars:
      - group_vars/vault.yml
      motd_info:
        - " FQDN:    ": "{{ ansible_fqdn }}"
        - " RAM:     ": "{{ (ansible_memtotal_mb / 1000) | round(1) }}GB"
```
