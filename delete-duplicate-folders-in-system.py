from collections import defaultdict

class Solution(object):
    class Node:
        def __init__(self):
            self.children = dict()
            self.del_mark = False

    def deleteDuplicateFolder(self, paths):
        root = self.Node()

        for path in paths:
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = self.Node()
                curr = curr.children[folder]

        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            serials = []
            for folder in sorted(node.children):
                child_serial = serialize(node.children[folder])
                serials.append(f"({folder}{child_serial})")
            serial_str = "".join(serials)
            serial_map[serial_str].append(node)
            return serial_str

        serialize(root)

        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.del_mark = True

        result = []

        def collect(node, path):
            for folder, child in node.children.items():
                if not child.del_mark:
                    new_path = path + [folder]
                    result.append(new_path)
                    collect(child, new_path)

        collect(root, [])
        return result