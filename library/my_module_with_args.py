#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

def main():
  argument_spec = {
    'name': {'type': 'str', 'required': True},
    'scores': {'type': 'list', 'required': False, 'default': []},
    'state': {'choices': ['present', 'absent'], 'default': 'present'},
    'options': {'type': 'dict', 'default': {}}
  }

  module = AnsibleModule(
    argument_spec=argument_spec,
    supports_check_mode=False
  )

  result = dict()
  result["changed"] = True

  # This is how you fetch parameters
  name = module.params['name']
  scores = module.params['scores']

  module.exit_json(**result)

if __name__ == '__main__':
    main()
