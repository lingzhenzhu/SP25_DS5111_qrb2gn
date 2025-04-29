import sys
import platform

def test_os_is_linux():
    assert platform.system() == "Linux", "OS is not Linux!"

def test_python_version():
    assert sys.version_info.major == 3 and sys.version_info.minor in (10, 11), "Python version is not 3.10 or 3.11!"
