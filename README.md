## Description

Examples and slides for my Ansible Meetup talk about custom modules.

## Usage

Install dependencies (Ansible):

```
virtualenv -p $(which python) venv/
source venv/bin/activate
pip install -r requirements.txt
```

Call the playbooks:

```
ansible-playbook my_module_playbook.yml
```
