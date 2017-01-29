class Annotated(object):
    def __new__(cls, *args): ...
    def __init__(self, element, values): ...
    def _annotate(self, values): ...
    def _with_annotations(self, values): ...
    def _deannotate(self, values=..., clone: bool=...): ...
    def _compiler_dispatch(self, visitor, **kw): ...
    def _constructor(self): ...
    def _clone(self): ...
    def __hash__(self): ...
    def __eq__(self): ...