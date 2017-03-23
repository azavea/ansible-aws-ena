import pytest
import re


@pytest.fixture()
def AnsibleDefaults(Ansible):
    """ Load default variables into dictionary.
    Args:
        Ansible - Requires the ansible connection backend.
    """
    return Ansible("include_vars", "./defaults/main.yml")["ansible_facts"]


def test_driver_version(Command, AnsibleDefaults):
    """ Ensure the candidate version of pip is installed.

    Args:
        Command - Module to determine package install status and version
        GetAnsibleDefaults - Get default version of the package
    """
    ena_version_check = Command('modinfo ena')
    default_ena_version = AnsibleDefaults["aws_ena_driver_version"]

    assert re.search("^version:\s+{}$".format(default_ena_version),
                     ena_version_check.stdout, re.M) is not None
