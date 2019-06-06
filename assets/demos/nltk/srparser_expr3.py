
from nltk.app.srparser_app import ShiftReduceApp

def app():
    """
    Create a shift reduce parser app, using a simple grammar and
    text. 
    """
    from nltk import CFG
    expr_grammar = """
        E -> T E1
        E1 -> PLUS T E1
        E1 ->
        T -> F
        F -> ID

        PLUS -> '+'
        ID -> 'a'
        ID -> 'b'
        ID -> 'c'
    """
    grammar = CFG.fromstring(expr_grammar)
    text = "a + b".split()
    ShiftReduceApp(grammar, text).mainloop()

if __name__ == '__main__':
    app()

__all__ = ['app']
