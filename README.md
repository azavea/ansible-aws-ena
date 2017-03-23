# ansible-aws-ena

An Ansible role for installing AWS Elastic Networking Adapter (ENA) drivers. 


## Usage

Amazon's Elastic Networking service is availble on `c3`, `c4`, `d2`, `i2`, `r3`, and `m4` instance types (excluding `m4.16xlarge`). To setup Elastic Networking, use this role to install drivers on the instance, and then enable Elastic Networking using the AWS CLI:

```bash
# Install the role
$ ansible-galaxy install azavea.aws-ena

# Create a playbook.yml that uses the role
$ cat /path/to/your/playbook.yml
---
- hosts: all
  pre_tasks:
    - name: Update APT cache
      apt: update_cache=true

  roles:
    - role: azavea.aws-ena

# Ensure your inventory has an entry for your EC2 instance
$ ansible-playbook -i /path/to/inventory /path/to/your/playbook.yml

# Enable ENA on your EC2 instance via the aws CLI
$ aws ec2 modify-instance-attribute --instance-id <YOUR_INSTANCE_ID> --ena-support
```
Further information is available in the AWS ENA [documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html#test-enhanced-networking-ena).

## Role Variables

- `aws_ena_driver_version` - AWS ENA driver version.

## Testing
Tests are done using [molecule](http://molecule.readthedocs.io/). To run the test suite, install molecule and its dependencies and run ` molecule test` from the folder containing molecule.yml. To add additional tests, add a [testinfra](http://testinfra.readthedocs.org/) python script in the [tests](./tests/) directory, or add a function to [test_ena.py](./tests/test_ena.py). Information about available Testinfra modules is available [here](http://testinfra.readthedocs.io/en/latest/modules.html).

### Example 
```
# Download molecule, dependencies
$ pip install molecule

# Change to the top-level project directory, which contains molecule.yml
$ cd /path/to/ansible-aws-ena

# Ensure that molecule.yml is present
$ ls
CHANGELOG.md                             molecule.yml
LICENSE                                  playbook.retry
README.md                                playbook.yml
ansible.cfg                              tasks
defaults                                 templates
handlers                                 tests
meta                                     

# We're in the right directory, so let's run tests!
$ molecule test

```
