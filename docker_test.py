import docker

creds = {
	"auths": {
		"https://index.docker.io/v1/": {
			"auth": "ZmF0aW5pc2htYW06ZGNrcl9wYXRfZU1vR3dKc0ZVenhoNVE1WU9UaXRNeWozaTNN"
		}
	},
	"credsStore": "desktop",
	"currentContext": "desktop-linux"
}

# Initialize the Docker client
client = docker.DockerClient(base_url='unix://var/run/docker.sock', credstore_env=creds)

# Define the NGINX image to use
nginx_image = "nginx:latest"

# Define container options
container_options = {
    "detach": True,
    "ports": {'80/tcp': 8080},  # Map container's port 80 to host's port 8080
    "name": "nginx_container"   # Name your container
}

# Pull the NGINX image if not already present
client.images.pull(nginx_image)

# Create and start the container
container = client.containers.run(nginx_image, **container_options)

print("Container ID:", container.id)
