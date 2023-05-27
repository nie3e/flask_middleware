import requests
import pytest
import os
import subprocess

cur_dir = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(scope="session")
def start_docker_compose():
    compose_file = f"{cur_dir}/../docker-compose.yml"

    build_command = f"docker compose -f {compose_file} build"
    subprocess.run(build_command.split())

    start_command = f"docker compose -f {compose_file} up --wait"
    subprocess.run(start_command.split())

    yield True

    end_command = f"docker compose -f {compose_file} down"
    subprocess.run(end_command.split())


def test_middleware_app_v1_hello(start_docker_compose):
    res = requests.get("http://127.0.0.1:5555/v1/hello").json()
    assert "msg" in res
    assert res["msg"] == "Hello from app v1"


def test_middleware_app_v2_hello(start_docker_compose):
    res = requests.get("http://127.0.0.1:5555/v2/hello").json()
    assert "msg" in res
    assert res["msg"] == "Hello from app v2"
