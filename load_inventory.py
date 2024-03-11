from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

# Load inventory
loader = DataLoader()
inventory = InventoryManager(loader=loader, sources='hosts.yml')

# Print host information
for host in inventory.get_hosts():
    print(f"Name: {host.name}, IP Address: {host.vars['ansible_host']}, Groups: {host.groups}")
