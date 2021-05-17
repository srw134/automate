terraform {
  required_providers {
    esxi = {
      source = "kube-cloud/esxi"
      version = "1.9.5"
    }
  }
}

#provider "esxi" {
#  esxi_hostname      = "192.168.1.85"
#  esxi_hostport      = "22"
#  esxi_hostssl       = "443"
#  esxi_username      = "root"
#  esxi_password      = "PassWord!"
#}

provider "esxi" {
  esxi_hostname = var.esxi_hostname
  esxi_hostport = var.esxi_hostport
  esxi_hostssl  = var.esxi_hostssl
  esxi_username = var.esxi_username
  esxi_password = var.esxi_password
}

resource "esxi_guest" "vmtest1" {
  guest_name         = "vmtest1"
  disk_store         = "Main_DS"

  memsize            = "4096"
  numvcpus           = "1"
  power              = "on"
  resource_pool_name = "/"

  #
  #  Specify an existing guest to clone, an ovf source, or neither to build a bare-metal guest vm.
  #
  clone_from_vm      = "csr1k-template"
  #ovf_source        = "/ubuntu-template/ubuntu-template.vmx"

  network_interfaces {
    virtual_network = "VM Network"
     mac_address = "00:20:11:11:11:11"
     nic_type = "vmxnet3"
     
  }

  network_interfaces {
     virtual_network = "e2-PG"
     mac_address = "00:20:11:11:22:22"
     nic_type = "vmxnet3"
    
  }

  network_interfaces {
    virtual_network = "e3-PG"
    mac_address = "00:20:11:11:33:33"
    nic_type = "vmxnet3"
    
  }

}

resource "esxi_guest" "vmtest2" {
  guest_name         = "vmtest2"
  disk_store         = "Main_DS"

  memsize            = "4096"
  numvcpus           = "1"
  power              = "on"
  resource_pool_name = "/"

  #
  #  Specify an existing guest to clone, an ovf source, or neither to build a bare-metal guest vm.
  #
  clone_from_vm      = "csr1k-template"
  #ovf_source        = "/ubuntu-template/ubuntu-template.vmx"

  network_interfaces {
    virtual_network = "VM Network"
     mac_address = "00:20:22:22:11:11"
     nic_type = "vmxnet3"
     
  }

  network_interfaces {
     virtual_network = "e2-PG"
     mac_address = "00:20:22:22:22:22"
     nic_type = "vmxnet3"
    
  }

  network_interfaces {
    virtual_network = "e3-PG"
     mac_address = "00:20:22:22:33:33"
     nic_type = "vmxnet3"
    
  }

}

resource "null_resource" "ansible" {

  provisioner "local-exec" {
    command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i hosts.yaml main.yaml"
  }

  depends_on = [
    esxi_guest.vmtest1, esxi_guest.vmtest2
  ]

}
