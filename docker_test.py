import docker

client = docker.DockerClient(base_url='unix://var/run/docker.sock')


docker_folder = "simple_web_app"
deployment_name = "simplewebapp"
docker_username = "fatinishmam"
docker_password = "dckr_pat_eMoGwJsFUzxh5Q5YOTitMyj3i3M"


client.images.build(path=docker_folder, gzip=False, tag=f"{docker_username}/{deployment_name}")

image = client.images.get(f"{docker_username}/{deployment_name}")
print(image.short_id)
print("start pushing your docker image to docker hub")
client.login(username=docker_username, password=docker_password)
# client.images.push('arycloud/istiogui', tag=f"{docker_username}/{deployment_name}")
for line in client.images.push(f'{docker_username}/{deployment_name}', stream=True, decode=True):
    print(line)

