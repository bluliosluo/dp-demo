class Solution:
    def pre_order(self, node):
        if not node:
            return
        # process
        cur_node_val = node.val
        res = min(self.pre_order(node.left) +
                  self.pre_order(node.right), cur_node_val)
        return res


def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node.val)
    in_order(node.right)



def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.val)