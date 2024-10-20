# from prefect.docker import DockerImage

# from flow import main

# if __name__ == "__main__":
#     main.deploy(
#         name="check-for-mouse",
#         work_pool_name="Production",
#         image=DockerImage(
#             name="ghcr.io/darrida/victor-mouse-trap",
#             tag="2024.10.20",
#             dockerfile="Dockerfile"
#         ),
#         build=True,
#         push=True
#     )