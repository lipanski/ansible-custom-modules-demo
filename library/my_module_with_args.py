#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

def main():
  argument_spec = dict(
    name=dict(type='str', required=True),
    scores=dict(type='list', required=False, default=[])
  )

  module = AnsibleModule(
    argument_spec=argument_spec,
    supports_check_mode=False
  )

  result = dict()
  result["changed"] = True

  module.exit_json(**result)

if __name__ == '__main__':
    main()
