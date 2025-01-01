"""Top-level package for what-llm-can-i-run."""

__app_name__ = "whatllm"
__version__ = "0.1.0"

(
    SUCCESS, # integer 0
    RAM_ERROR, # integer 1
    VRAM_ERROR, # so on
) = range(3) # error code

ERRORS = {
    RAM_ERROR: "Error getting physical memory",
    VRAM_ERROR: "Error getting GPU memory",
}
