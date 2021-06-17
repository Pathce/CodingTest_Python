import math

def solution(progresses, speeds):
    job_list = []
    answer = []
    stack = 0
    for p, s in zip(progresses, speeds):
        progress = (100 - p)
        result = math.ceil(progress / s)
        job_list.append(result)

    for i in range(100):
        for n, job in enumerate(job_list, 0):
            job -= 1
            job_list[n] = job
        if job_list[0] == 0:
            for job in job_list:
                if job > 0:
                    break
                stack += 1
            answer.append(stack)
            del job_list[:stack]
            stack = 0
        if not len(job_list):
            break
    return answer