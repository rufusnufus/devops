# Infrastructure as code | Terraform
I was not able to run terraform under the only currently available virtualbox provider terra-farm/virtualbox since it last releases are unstable and platform dependent and previous releases use `terraform==0.6.0`, which is not installing on my system(macOS Big Sur Version 11.4). The file that I used to create VM is attached here - `main.tf`

### Error connected to terra-farm/virtualbox 
```bash
virtualbox_vm.node[0]: Creating...
virtualbox_vm.node[1]: Creating...
virtualbox_vm.node[1]: Still creating... [10s elapsed]
virtualbox_vm.node[0]: Still creating... [10s elapsed]
virtualbox_vm.node[0]: Still creating... [20s elapsed]
virtualbox_vm.node[1]: Still creating... [20s elapsed]
virtualbox_vm.node[1]: Still creating... [30s elapsed]
virtualbox_vm.node[0]: Still creating... [30s elapsed]
virtualbox_vm.node[1]: Still creating... [40s elapsed]
virtualbox_vm.node[0]: Still creating... [40s elapsed]
virtualbox_vm.node[0]: Still creating... [50s elapsed]
virtualbox_vm.node[1]: Still creating... [50s elapsed]
virtualbox_vm.node[1]: Still creating... [1m0s elapsed]
virtualbox_vm.node[0]: Still creating... [1m0s elapsed]
virtualbox_vm.node[0]: Still creating... [1m10s elapsed]
virtualbox_vm.node[1]: Still creating... [1m10s elapsed]
virtualbox_vm.node[1]: Still creating... [1m20s elapsed]
╷
│ Error: [ERROR] Setup VM properties: exit status 1
│ 
│   with virtualbox_vm.node[0],
│   on main.tf line 12, in resource "virtualbox_vm" "node":
│   12: resource "virtualbox_vm" "node" {
│ 
╵
╷
│ Error: [ERROR] Setup VM properties: exit status 1
│ 
│   with virtualbox_vm.node[1],
│   on main.tf line 12, in resource "virtualbox_vm" "node":
│   12: resource "virtualbox_vm" "node" {
```

### Error connected to terraform=0.6.0
```bash
Switching default version to v0.6.0
failed MSpanList_Insert 0xb9c000 0x1e8b43117c7c 0x0
fatal error: MSpanList_Insert

runtime stack:
runtime.throw(0xa952ab)
        /opt/go/src/runtime/panic.go:491 +0xad fp=0x7ffeefbfdca0 sp=0x7ffeefbfdc70
runtime.MSpanList_Insert(0xac2788, 0xb9c000)
        /opt/go/src/runtime/mheap.c:692 +0x8f fp=0x7ffeefbfdcc8 sp=0x7ffeefbfdca0
MHeap_FreeSpanLocked(0xabf380, 0xb9c000, 0x100)
        /opt/go/src/runtime/mheap.c:583 +0x163 fp=0x7ffeefbfdd08 sp=0x7ffeefbfdcc8
MHeap_Grow(0xabf380, 0x8, 0x0)
        /opt/go/src/runtime/mheap.c:420 +0x1a8 fp=0x7ffeefbfdd48 sp=0x7ffeefbfdd08
MHeap_AllocSpanLocked(0xabf380, 0x1, 0x1)
        /opt/go/src/runtime/mheap.c:298 +0x365 fp=0x7ffeefbfdd88 sp=0x7ffeefbfdd48
mheap_alloc(0xabf380, 0x1, 0x7f0000000012, 0x639e000)
        /opt/go/src/runtime/mheap.c:190 +0x121 fp=0x7ffeefbfddb0 sp=0x7ffeefbfdd88
runtime.MHeap_Alloc(0xabf380, 0x1, 0x10000000012, 0x15ec9)
        /opt/go/src/runtime/mheap.c:240 +0x66 fp=0x7ffeefbfdde8 sp=0x7ffeefbfddb0
MCentral_Grow(0xac70f8, 0x7ffeefbfded8)
        /opt/go/src/runtime/mcentral.c:197 +0x8b fp=0x7ffeefbfde50 sp=0x7ffeefbfdde8
runtime.MCentral_CacheSpan(0xac70f8, 0x1007ffeefbfdf08)
        /opt/go/src/runtime/mcentral.c:85 +0x167 fp=0x7ffeefbfde88 sp=0x7ffeefbfde50
runtime.MCache_Refill(0xb98000, 0x7ffe00000012, 0x7ffeefbfdf50)
        /opt/go/src/runtime/mcache.c:90 +0xa0 fp=0x7ffeefbfdeb0 sp=0x7ffeefbfde88
runtime.mcacheRefill_m()
        /opt/go/src/runtime/malloc.c:368 +0x57 fp=0x7ffeefbfded0 sp=0x7ffeefbfdeb0
runtime.onM(0x897800)
        /opt/go/src/runtime/asm_amd64.s:273 +0x9a fp=0x7ffeefbfded8 sp=0x7ffeefbfded0
runtime.mallocgc(0x120, 0x6ede80, 0x0, 0x0)
        /opt/go/src/runtime/malloc.go:178 +0x849 fp=0x7ffeefbfdf88 sp=0x7ffeefbfded8
runtime.newobject(0x6ede80, 0xb98000)
        /opt/go/src/runtime/malloc.go:353 +0x49 fp=0x7ffeefbfdfb0 sp=0x7ffeefbfdf88
runtime.newG(0x3094a)
        /opt/go/src/runtime/proc.go:233 +0x2a fp=0x7ffeefbfdfc8 sp=0x7ffeefbfdfb0
allocg(0xaae180)
        /opt/go/src/runtime/proc.c:925 +0x1f fp=0x7ffeefbfdfd8 sp=0x7ffeefbfdfc8
runtime.malg(0x8000, 0xaae5c0)
        /opt/go/src/runtime/proc.c:2106 +0x1f fp=0x7ffeefbfe008 sp=0x7ffeefbfdfd8
runtime.mpreinit(0xaaee00)
        /opt/go/src/runtime/os_darwin.c:137 +0x27 fp=0x7ffeefbfe020 sp=0x7ffeefbfe008
mcommoninit(0xaaee00)
        /opt/go/src/runtime/proc.c:201 +0xc9 fp=0x7ffeefbfe048 sp=0x7ffeefbfe020
runtime.schedinit()
        /opt/go/src/runtime/proc.c:138 +0x55 fp=0x7ffeefbfe070 sp=0x7ffeefbfe048
runtime.rt0_go(0x7ffeefbfe0a8, 0x2, 0x7ffeefbfe0a8, 0x0, 0x0, 0x2, 0x7ffeefbfe320, 0x7ffeefbfe357, 0x0, 0x7ffeefbfe35f, ...)
        /opt/go/src/runtime/asm_amd64.s:95 +0x116 fp=0x7ffeefbfe078 sp=0x7ffeefbfe070
'terraform version' failed. Something is seriously wrong
```

# Infrastructure as Code | Vagrant
However, on the lab we have got a permission to use vagrant tool instead.

## Prerequisites:
* [VirtualBox==6.1.26](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant==2.2.18](https://www.vagrantup.com/downloads)

## Creating a VM in VirtualBox
1. Provision your VM:
    ```bash
    vagrant up
    ```
2. Connect to your VM:
    ```bash
    vagrant ssh
    ```
3. To destroy your VM:
    ```bash
    vagrant destroy
    ```

## References

* https://medium.com/@JohnFoderaro/how-to-set-up-a-local-linux-environment-with-vagrant-163f0ba4da77