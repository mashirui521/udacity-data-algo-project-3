class RouteTrieNode:
    def __init__(self):
        self.children = dict()
        self.handler = None

    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, path_parts, handler):
        current_node = self.root

        for path_part in path_parts:
            current_node.insert(path_part)
            current_node = current_node.children[path_part]

        current_node.handler = handler

    def find(self, path_parts):
        current_node = self.root

        for path_part in path_parts:
            if path_part not in current_node.children:
                return None
            current_node = current_node.children[path_part]

        return current_node.handler


class Router:
    def __init__(self, root_handler, non_found_handler):
        self.router = RouteTrie(root_handler)
        self.non_found_handler = non_found_handler

    def add_handler(self, path, handler):
        path_parts = self.__split_path__(path)
        self.router.insert(path_parts, handler)

    def lookup(self, path):
        path_parts = self.__split_path__(path)

        if len(path_parts) == 0:
            return self.router.handler

        found_handler = self.router.find(path_parts)
        if found_handler is None:
            found_handler = self.non_found_handler

        return found_handler

    def __split_path__(self, path):
        path_parts_raw = path.split(sep='/')
        return [path_part for path_part in path_parts_raw if path_part != '']


# Here are some test cases and expected outputs you can use to test your implementation


# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))                 # should print 'root handler'
print(router.lookup("/home"))             # should print 'not found handler'
print(router.lookup("/home/about"))       # should print 'about handler'
print(router.lookup("/home/about/"))      # should print 'about handler'
print(router.lookup("/home/about/me"))    # should print 'not found handler'
print(router.lookup("12"))                # should print 'not found handler'
print(router.lookup(""))                  # should print 'root handler'