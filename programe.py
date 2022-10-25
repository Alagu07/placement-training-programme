def generate(result: List[str], s: str, _open: int, close: int, n: int):
 if _open == n and close == n:
 result.append(s)
 return
 if _open < n:
 generate(result, s + "(", _open + 1, close, n)
 if close < _open:
 generate(result, s + ")", _open, close + 1, n)
def generateParenthesis(n: int) -> List[str]:
 result = []
 generate(result, "", 0, 0, n)
 return result
