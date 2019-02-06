from typing import Any, Callable

from django.db import IntegrityError

def CASCADE(collector, field, sub_objs, using): ...
def SET_NULL(collector, field, sub_objs, using): ...
def SET_DEFAULT(collector, field, sub_objs, using): ...
def DO_NOTHING(collector, field, sub_objs, using): ...
def PROTECT(collector, field, sub_objs, using): ...
def SET(value: Any) -> Callable: ...

class ProtectedError(IntegrityError): ...
class Collector: ...
