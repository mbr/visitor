class Visitor(object):
    """Base class for visitors."""

    def visit(self, node):
        """Visit a node.

        Calls ``visit_CLASSNAME`` on itself passing ``node``, where
        ``CLASSNAME`` is the node's class. If the visitor does not implement an
        appropriate visitation method, will go up the
        `MRO <https://www.python.org/download/releases/2.3/mro/>`_ until a
        match is found.

        If the search exhausts all classes of node, raises a
        :class:`~exceptions.NotImplementedError`.

        :param node: The node to visit.
        :return: The return value of the called visitation function.
        """
        for cls in type(node).mro():
            meth = getattr(self, 'visit_' + cls.__name__, None)
            if meth is None:
                continue
            return meth(node)

        raise NotImplementedError('No visitation method visit_{}'
                                  .format(node.__class__.__name__))
