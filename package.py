
name = "cmake"

version = "3.18.2"

_data = {
    "label": "cmake",
    "icon": "{root}/resources/cmake.ico"
}

tools = [
    "cmake"
]

build_command = False


def commands():
    env = globals()["env"]
    env.PATH.prepend("C:/Program Files/CMake/bin")
    env.REZ_CMAKE_GENERATOR = "Visual Studio 15 2017 Win64"

    # (TODO) What will MacOS/Linux do ?
