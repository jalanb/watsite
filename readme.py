"""
>>> import watsite as site

>>> split_ext('fred')
('fred', '')
>>> split_ext('fred.py')
['fred', 'py']
>>> split_ext('fred.sh')
['fred', 'sh']
"""
def split_ext(string):
    return string.split('.') if '.' in string else (string, '')


import inspect
import doctest

here = inspect.getmoduleinfo(__file__)
name, suffix, mode, module_type = here
_, ext = split_ext(suffix)

module = importlib.import_module(name)

doctest.testmod(
        module,
        optionflags=get_doctest_options(options),
        verbose=options.verbose,
    )
