import os
import sys


class Utils:
    @staticmethod
    def base_path():
        return os.path.dirname(os.path.abspath(sys.argv[0]))

    @staticmethod
    def asset_path(file):
        base_dir = Utils.base_path()
        return f"{base_dir}/assets/{file}"

    @staticmethod
    def llm_path():
        base_dir = Utils.base_path()
        return f"{base_dir}/llm"

    @staticmethod
    def prompt_path(file):
        base_dir = Utils.base_path()
        return f"{base_dir}/src/prompts/{file}"
