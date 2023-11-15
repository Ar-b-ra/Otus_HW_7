import threading

from queue_worker import QueueWorker


class ThreadWorker:
    def __init__(self, queue_worker: QueueWorker):
        self.queue_worker = queue_worker
        self.thread = threading.Thread(target=self.queue_worker.run)

    def hard_stop(self):
        self.thread.join(0)