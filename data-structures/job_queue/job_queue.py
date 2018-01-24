# python3
import heapq


class Thread:
    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.release_time = 0

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for thread_id, start_time in self.result:
            print(thread_id, start_time)

    def assign_jobs(self):
        self.result = []
        self.thread_queue = [Thread(i) for i in range(self.num_workers)]

        for job_len in self.jobs:
            worker = heapq.heappop(self.thread_queue)
            self.result.append((worker.thread_id, worker.release_time))
            worker.release_time += job_len
            heapq.heappush(self.thread_queue, worker)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
