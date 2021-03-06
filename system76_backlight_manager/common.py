import logging
import subprocess

logger = logging.getLogger(f"system76_backlight_manager.{__name__}")


def read_file(path: str) -> str:
    with open(path, "r") as f:
        data = f.read()
        logger.debug(f"Read {data} from {path}")
        return data if isinstance(data, str) else data.decode("utf-8")


def write_file(path: str, value: str):
    with open(path, "wb") as f:
        logger.debug(f"Writing: {value} to {path}")
        f.write(value.encode())


def get_laptop_model() -> str:
    return subprocess.check_output(["dmidecode", "-s", "system-version"]).decode("utf-8").strip()
