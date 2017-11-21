#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

def main():
  module = AnsibleModule(
    argument_spec=dict(),
    supports_check_mode=False
  )

  result = dict()
  result["failed"] = True

  module.exit_json(**result)

if __name__ == '__main__':
    main()
