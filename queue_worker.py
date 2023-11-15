from queue import Queue
from typing import Callable

from utility.custom_logger import root_logger


class QueueWorker:
    def __init__(self, queue: Queue):
        self.queue = queue
        self.is_working = False

    def run(self):
        while not self.queue.empty():
            self.is_working = True
            item = self.queue.get()
            try:
                item()
            except Exception as e:
                root_logger.exception(e)
            self.queue.task_done()
        self.is_working = False

    def put_command(self, item: Callable):
        self.queue.put(item)

        if self.queue.empty() and not self.is_working:
            self.is_working = True
            self.run()

    def soft_stop(self):
        self.is_working = False
