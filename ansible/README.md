# Running Ansible

## Docker provisioning

1. Go to right path: 
   ```bash
   cd ../terraform/virtualbox/
   ```
2. Run vagrant. This command creates 1 virtual machine and provisions there playbook.
    ```bash 
    vagrant up
    ```
3. If playbook is modified, you can reprovision it: 
    ```bash 
    vagrant provision
    ```
4. To connect to VM: 
    ```bash 
    vagrant ssh
    ```