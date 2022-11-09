import omvll

class MyConfig(omvll.ObfuscationConfig):
    def __init__(self):
        super().__init__()

    def flatten_cfg(self, mod: omvll.Module, func: omvll.Function):
        if func.name == "func":
            return True
        return False

from functools import lru_cache

@lru_cache(maxsize=1)
def omvll_get_config() -> omvll.ObfuscationConfig:
    """
    Return an instance of `ObfuscationConfig` which
    aims at describing the obfuscation scheme
    """
    return MyConfig()