import docker
import requests

class DockerImage(object):

	def __init__(self, docker_image_dict):
		self.docker_image_dict = docker_image_dict

	@property
	def image_id(self):
		if not self.docker_image_dict:
			return None
		return self.docker_image_dict['images'][0]['digest']
	

class DockerAPIclient(object):

	def __init__(
		self, 
		dockerhub_username=None, 
		dockerhub_password=None
	):

		self.dockerhub_username = dockerhub_username
		self.dockerhub_password = dockerhub_password

	@classmethod
	def get_image_info(cls, repo_name, image_name, tag="latest"):
		url = f'https://hub.docker.com/v2/repositories/{repo_name}/{image_name}/tags/{tag}'
		response = requests.get(url)
		if response.status_code != 200:
			return DockerImage({})

		return DockerImage(response.json())

class DockerEngineClient(object):

	_client = docker.from_env()

	@classmethod
	def get_image_id(cls, repo_name, image_name, tag="latest"):
		image_identifier = f"{repo_name}/{image_name}:{tag}"
		repo_digest = cls._client.images.get(image_identifier).attrs['RepoDigests'][0]
		return repo_digest.split('@')[1]



if __name__=="__main__":
	import sys
	import os
	repo_name, image_name, app_port = sys.argv[1], sys.argv[2], int(sys.argv[3])
	local_image_id = DockerEngineClient().get_image_id(repo_name, image_name)
	remote_image_id = DockerAPIclient().get_image_info(repo_name, image_name).image_id

	if local_image_id != remote_image_id:
		print(f"local_image_id {local_image_id} is different from remote_image_id {remote_image_id}, Pull latest image and Run it")
		os.system(f"docker stop {image_name}")
		os.system(f"docker image rm {repo_name}/{image_name}:latest")
		os.system(f"docker pull {repo_name}/{image_name}:latest")
		os.system(f"docker run --rm -d -p {app_port}:{app_port} -e APP_VERSION=latest -e APP_HOST=$HOSTNAME --name={image_name} {repo_name}/{image_name}:latest")
	else:
		print("remote image has not changed, no deploy needed")
	