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
  #power              = "on"
  resource_pool_name = "/"

  #
  #  Specify an existing guest to clone, an ovf source, or neither to build a bare-metal guest vm.
  #
  clone_from_vm      = "csr1k-template"
  #ovf_source        = "/ubuntu-template/ubuntu-template.vmx"

  network_interfaces {
    virtual_network = "VM Network"
    nic_type = "vmxnet3"
     
  }

  network_interfaces {
     virtual_network = "e2-PG"
     mac_address = "0200.1111.1111"
     nic_type = "vmxnet3"
    
  }

  network_interfaces {
    virtual_network = "e3-PG"
    mac_address = "0200.1111.2222"
    nic_type = "vmxnet3"
    
  }

}

resource "esxi_guest" "vmtest2" {
  guest_name         = "vmtest2"
  disk_store         = "Main_DS"

  memsize            = "4096"
  numvcpus           = "1"
  #power              = "on"
  resource_pool_name = "/"

  #
  #  Specify an existing guest to clone, an ovf source, or neither to build a bare-metal guest vm.
  #
  clone_from_vm      = "csr1k-template"
  #ovf_source        = "/ubuntu-template/ubuntu-template.vmx"

  network_interfaces {
    virtual_network = "VM Network"
    nic_type = "vmxnet3"
     
  }

  network_interfaces {
     virtual_network = "e2-PG"
     mac_address = "0200.2222.1111"
     nic_type = "vmxnet3"
    
  }

  network_interfaces {
    virtual_network = "e3-PG"
     mac_address = "0200.2222.2222"
     nic_type = "vmxnet3"
    
  }

}
