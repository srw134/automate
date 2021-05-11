variable "esxi_hostname" {
  type = string
}

variable "esxi_hostport" {
  type = string
}

variable "esxi_hostssl" {
  type = string
}

variable "esxi_username" {
  type = string
}

variable "esxi_password" { 
  sensitive = true
}