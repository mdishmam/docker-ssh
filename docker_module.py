import docker

class DockerManager:

    def __init__(self, application_folder, image_name, docker_username, docker_password):
        self.application_folder = application_folder
        self.image_name = image_name
        self.docker_username = docker_username
        self.docker_password = docker_password

        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')

        self.client.login(username=docker_username, password=docker_password)

    def build_image(self):
        self.client.images.build(path=self.application_folder, gzip=False, tag=f"{self.docker_username}/{self.image_name}")
        self.image = self.client.images.get(f"{self.docker_username}/{self.image_name}")
        return self.image

    def push_image(self):
        for line in self.client.images.push(f'{self.docker_username}/{self.image_name}', stream=True, decode=True):
            print(line)


if __name__ == '__main__':
    pass