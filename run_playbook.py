from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.errors import AnsibleError
from ansible import context
from ansible.module_utils.common.collections import ImmutableDict
import requests

# Load inventory
loader = DataLoader()




context.CLIARGS = ImmutableDict( syntax=False, connection='ssh',
                                  private_key_file="secrets/id_rsa",
                                ssh_common_args=None, become=True,
                                become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)

inventory = InventoryManager(loader=loader, sources='hosts.yml')
variable_manager = VariableManager(loader=loader, inventory=inventory)

# Playbook path
playbook_path = 'hello.yml'

# Create playbook executor
pb_executor = PlaybookExecutor(
    playbooks=[playbook_path],
    inventory=inventory,
    loader=loader,
    variable_manager=variable_manager,
    passwords={}
)




# Run playbook
try:
    pb_executor.run()
except AnsibleError as e:
    print("An error occurred while running the playbook:", e)



response = requests.get('http://127.0.0.1:3000')
if response.text != "Hello World from managedhost-app-1 !":
   raise Exception("Return is not correct")
print(response.text)

response = requests.get('http://127.0.0.1:3001') 
if response.text != "Hello World from managedhost-app-2 !":
   raise Exception("Return is not correct")
print(response.text)


response = requests.get('http://127.0.0.1:3002') 
if response.text != "Hello World from managedhost-app-3 !":
   raise Exception("Return is not correct")
print(response.text)





