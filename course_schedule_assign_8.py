#Course Schedule

#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
#You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
#must take course bi first if you want to take course ai.

#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true

#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false

def course_schedule(n,prerequisites):
    graph = [[] for _ in range(n)]
    g = [0] * n

    for a, b in prerequisites:
        graph[b].append(a)
        g[a] = g[a] + 1

    res = [a for a in range(n) if g[a] == 0]

    while res:
        b = res.pop()
        for a in graph[b]:
            g[a] = g[a] - 1
            if g[a] == 0:
                res.append(a)

    return not any(g)

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    print("The total number of courses to take is :",numCourses)
    print("The prerequisite is :", prerequisites)
    print("Output:",course_schedule(numCourses,prerequisites))