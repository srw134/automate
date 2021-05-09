terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

#provider "docker" {
#  host = var.docker.remote.host
#}

resource "docker_image" "mysql" {
  name         = "mysql:5.7"
  keep_locally = true
}

resource "docker_container" "mysql-db" {
  image = docker_image.mysql.name

  env   = ["MYSQL_ROOT_PASSWORD=PassWord!","MYSQL_DATABASE=db_name","MYSQL_USER=db_user", "MYSQL_PASSWORD=PassWord!"]
  name  = "mysql-db"
##MAY WANT TO LINK THIS TO THE PRECONFIGURED NETWORK SHOWN BELOW  
}

data "docker_network" "main" {
  name = "test_net"
}

output "test_out" {
  value="${data.docker_network.main.ipam_config}"
}

##This is a test change