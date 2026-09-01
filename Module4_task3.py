# модуль 4 задание 3

def horizontal_search(graph,start,found = []):
	found.append(start)
	for friend in graph[start]:
		if friend not in found:
			found.append(friend)
			found = horizontal_search(graph,friend,found)
	return list(set(found))
