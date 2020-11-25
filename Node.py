from typing import List


class Nodes():
    def __init__(self, nodes) -> None:
        self.nodes: List = nodes

    def add_node(self, node) -> None:
        self.nodes.append(node)


class LiteralNode():
    def __init__(self, value) -> None:
        self.value = value


class StringNode(LiteralNode):
    def __init__(self, value) -> None:
        super(LiteralNode, self).__init__(value)


class NumberNode(LiteralNode):
    def __init__(self, value) -> None:
        super(LiteralNode, self).__init__(value)


class TrueNode(LiteralNode):
    def __init__(self) -> None:
        super(LiteralNode, self).__init__(True)


class FalseNode(LiteralNode):
    def __init__(self) -> None:
        super(LiteralNode, self).__init__(False)


class NilNode(LiteralNode):
    def __init__(self) -> None:
        super(LiteralNode, self).__init__(None)


class CallNode():
    def __init__(self, receiver, method, arguments) -> None:
        self.receiver = receiver
        self.method = method
        self.arguments = arguments


class GetConstantNode():
    def __init__(self, name) -> None:
        self.name = name


class SetConstantNode():
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value


class GetLocalNode():
    def __init__(self, name) -> None:
        self.name = name


class SetLocalNode():
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value


class DefNode():
    def __init__(self, name, params, body) -> None:
        self.name = name
        self.params = params
        self.body = body


class ClassNode():
    def __init__(self, name, body) -> None:
        self.name = name
        self.body = body


class IfNode():
    def __init__(self, condition, body) -> None:
        self.condition = condition
        self.body = body
