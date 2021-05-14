import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_motd_file(host):
    f = host.file('/etc/motd')

    assert f.exists


@pytest.mark.parametrize(
    "string, status", [
        ("Welcome to localhost!", True),
        ("FQDN:    ubuntu", True),
        ("Distro:  Ubuntu", True),
        ("Virtual: YES", True),
        ("Service: example.com", True),
        ("Last Ansible provisioning: 20", True),
    ]
)
def test_motd_content(host, string, status):
    f = host.file('/etc/motd')

    assert f.contains(string) is status
