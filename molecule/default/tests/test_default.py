import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service(host):
    nginx = host.service("nginx")
    assert nginx.is_enabled
    assert nginx.is_running