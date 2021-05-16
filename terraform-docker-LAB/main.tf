terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

provider "docker" {}

resource "docker_network" "joint_network" {
  name = "my_network"
  ipam_config {
    subnet = "10.1.1.0/24"
    ip_range = "10.1.1.0/24"
    gateway = "10.1.1.1"
  }

  #options = {"ip-range":"10.1.1.0/24","gateway":"10.1.1.1","ip-range":"10.1.1.0/24"} #Map of strings
}

resource "docker_image" "mysql" {
  name         = "mysql:5.7"
  keep_locally = true
}

resource "docker_image" "wordpress" {
  name         = "wordpress:latest"
  keep_locally = true
}

resource "docker_container" "wordpress-db" {
  image = docker_image.mysql.name

  env   = ["MYSQL_ROOT_PASSWORD=PassWord!","MYSQL_DATABASE=wordpress","MYSQL_USER=wordpress", "MYSQL_PASSWORD=PassWord!"] #Set of Strings
  name  = "wordpress-db"
  networks_advanced{
    name      = docker_network.joint_network.name
    ipv4_address = "10.1.1.2"
  }
}

resource "docker_container" "wordpress" {
  image = docker_image.wordpress.name

  env   = ["WORDPRESS_DB_HOST=10.1.1.2:3306","WORDPRESS_DB_USER=wordpress","WORDPRESS_DB_PASSWORD=PassWord!", "WORDPRESS_DB_NAME=wordpress"] #Set of Strings
  name  = "wordpress"
  networks_advanced{
    name      = docker_network.joint_network.name
    ipv4_address = "10.1.1.3"
  }
  ports {
    internal = 80
    external = 8080
  }

  depends_on = [
    docker_container.wordpress-db
  ]

}
