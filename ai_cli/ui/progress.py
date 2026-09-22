"""Progress indicators and spinner for Cortex CLI."""

import itertools
import threading
import time
from typing import Optional


class Spinner:
    FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def __init__(self, message: str = "Processing..."):
        self.message = message
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    def start(self) -> None:
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()

    def _spin(self) -> None:
        i = 0
        while not self._stop_event.is_set():
            frame = self.FRAMES[i % len(self.FRAMES)]
            print(f"\r  {frame} {self.message}...", end="", flush=True)
            time.sleep(0.1)
            i += 1

    def stop(self, final_message: str = "Done") -> None:
        if self._thread and self._thread.is_alive():
            self._stop_event.set()
            self._thread.join(timeout=2)
        print(f"\r  \033[92m\u2713 {final_message}\033[0m" + " " * 30)


def show_progress(steps: list, func, **kwargs):
    results = []
    for i, step in enumerate(steps, 1):
        print(f"  \033[94m[{i}/{len(steps)}]\033[0m {step}")
        result = func(step, i, len(steps), **kwargs)
        results.append(result)
    return results
