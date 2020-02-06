
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

print("My Graph is : ", graph)



visited = []  
queue = []  
v = []   

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


bfs(visited, graph, 'A')

Node = input("New : ")

No_Vertex = int(input("Number of Vertex : "))

for i in range(0,No_Vertex):
	v = input()
	graph[Node].append(v)
	
print("New Node : ",graph[Node])



print("My New Graph : ",graph)

NewG = graph

#bfs(visited, NewG, Node)

