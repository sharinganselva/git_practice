from collections import defaultdict, deque


def test_scheduler(tests, dependencies):
    dependency_graph = defaultdict(list)
    indegree = {}
    test_schedule = []
    for test in tests:
        indegree[test] = 0
    print(f"indegree = {indegree}")
    for prereq, test in dependencies:
        print(f"prereq: {prereq}; test: {test}")
        dependency_graph[prereq].append(test)
        indegree[test] += 1
    # for each_tuple in dependencies:
    #     print(each_tuple)
    #     dependency_graph[each_tuple[0]].append(each_tuple[1])
    #     indegree[each_tuple[1]] += 1
    print(f"indegree = {indegree}")
    queue = deque()
    for test, degree in indegree.items():
        print(f"test: {test}; degree: {degree}")
        if degree == 0:
            queue.append(test)
    print(f"queue: {queue}")
    while len(queue) > 0:
        test = queue.popleft()
        test_schedule.append(test)

        for test_affected in dependency_graph[test]:
            indegree[test_affected] -= 1
            if indegree[test_affected] == 0:
                queue.append(test_affected)

    if len(test_schedule) != len(tests):
        print("A circular dependency is detected")

    return test_schedule


if __name__ == "__main__":
    tests = ["t1", "t2", "t3", "t4", "t5", "t6"]
    dependencies = [("t1", "t2"), ("t2", "t6"), ("t4", "t5"), ("t4", "t6")]
    print(f"The Test Schedule : {test_scheduler(tests, dependencies)}")
