from src.profiler.io_profiler import IOProfiler


class TFProfiler(IOProfiler):
    def __init__(self, logdir):
        super().__init__(logdir)

    def start(self):
        pass

    def stop(self):
        pass