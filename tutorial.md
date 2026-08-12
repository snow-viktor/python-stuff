## Number 數字

- `//` 除法取商數
- `%` 除法取餘數
- `**` 次方
- `<<` 左移（n << x ⇔ n * 2^x）
- `>>` 右移（n >> x ⇔ n // 2^x）
- `int(variable, n)` 進位制轉換（0b 二進位、0o 八進位、0x 十六進位）
- `divmod(a, b)` 回傳 (商, 餘數)
- `round(n, 小數位)` 四捨五入

## String 字串

### 進階切片

- `[start:end:step]` 指定起始、結束、步進
- `[::-1]` 反轉字串

### 字串方法

- `split('')` 拆分 → 串列
- `join('')` 結合成字串
- `replace(舊, 新, 量)` 替換
- `strip('')` / `lstrip()` / `rstrip()` 剝除
- `find('')` / `rfind('')` 搜尋（回傳索引，找不到回傳 -1）
- `index('')` / `rindex('')` 搜尋（找不到會報錯）
- `count('')` 計算出現次數
- `startswith('')` / `endswith('')` 判斷開頭結尾
- `zfill(n)` 左側補零
- `center(n, ' ')` 居中對齊
- `expandtabs(n)` 替換 Tab 為空格
- `encode()` 字串編碼
- `isalnum()` / `isalpha()` / `isdigit()` 類型判斷

### f-string 格式化

```python
f"{variable}"              # 基本
f"{variable:.2f}"          # 小數點2位
f"{variable:>10}"          # 右對齊，寬度10
f"{variable:<10}"          # 左對齊
f"{variable:^10}"          # 居中對齊
f"{variable:0>10}"         # 右側補零
f"{variable:,}"            # 千分位逗號
f"{variable:%}"            # 百分比
f"{variable!r}"            # repr()
f"{variable!s}"            # str()
```

## Bool 布林

- `True` / `False`
- `any iterable` 任一為真即回傳 True
- `all iterable` 全部為真才回傳 True

## Data Structures 資料結構

### List 串列

- `append()` / `insert(i, x)` 新增
- `extend()` / `+` 合併
- `pop(i)` / `remove(x)` / `del` 刪除
- `sort()` / `sorted()` 排序（`key` 參數）
- `reverse()` / `[::-1]` 反轉
- `*list` 解包（unpacking）
- `[x for x in iterable]` List comprehension

### Tuple 元組

- 不可變的 List
- `tuple(iterable)` 轉換
- `a, b = (1, 2)` 解包
- `namedtuple` 命名元組

### Dict 字典

- `dict[key]` / `dict.get(key, default)` 取值
- `dict.update()` / `|` 合併
- `dict.keys()` / `dict.values()` / `dict.items()` 視圖
- `dict.pop(key)` 刪除
- `{k: v for k, v in iterable}` Dict comprehension
- `dict1 | dict2` 合併（Python 3.9+）
- `dict1 |= dict2` 原地合併（Python 3.9+）

### Set 集合

- `set()` 建立
- `add()` / `remove()` / `discard()` 操作
- `&` 交集 / `|` 聯集 / `-` 差集 / `^` 對稱差集
- `issubset()` / `issuperset()` 子集判斷
- `{x for x in iterable}` Set comprehension

## Control Flow 流程控制

### 三元運算式

```python
x = 值1 if 條件 else 值2
```

### match-case（Python 3.10+）

```python
match value:
    case pattern1:
        ...
    case pattern2 if guard:
        ...
    case _:
        ...  # 預設
```

### 迴圈

- `for x in iterable`
- `while condition`
- `break` / `continue` / `pass`

## Functions 函式

### 基本

```python
def func(a, b=10):      # 預設參數
    return a + b
```

### Lambda 匿名函式

```python
func = lambda x, y: x + y
```

### 可變參數

```python
def func(*args):         # 位置參數 tuple
    ...

def func(**kwargs):      # 命名參數 dict
    ...
```

### Type Hints 類型提示

```python
def func(a: int, b: str = "default") -> bool:
    ...
```

### Decorator 裝飾器

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 前置處理
        result = func(*args, **kwargs)
        # 後置處理
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

## Iteration 迭代工具

### 常用函式

- `enumerate(iterable, start=0)` 迴圈計數
- `zip(iterable1, iterable2)` 併行迭代
- `map(func, iterable)` 映射轉換
- `filter(func, iterable)` 條件篩選
- `reversed(iterable)` 反轉迭代
- `sorted(iterable, key=func, reverse=True)` 排序

### Generator 產生器

```python
def my_gen(n):
    for i in range(n):
        yield i

# Generator expression
gen = (x**2 for x in range(10))
```

## Error Handling 錯誤處理

```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Error: {e}")
except (TypeError, KeyError):
    print("Multiple errors")
except Exception as e:
    print(f"Unexpected: {e}")
finally:
    cleanup()
```

- `raise ValueError("msg")` 丟擲例外
- `assert condition, "msg"` 斷言（除錯用）

## File & Context 檔案與情境管理

### with statement

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### pathlib（Python 3.4+）

```python
from pathlib import Path

path = Path("folder/file.txt")
path.exists()          # 存在判斷
path.read_text()       # 讀取
path.write_text("...") # 寫入
path.mkdir(parents=True, exist_ok=True)  # 建立目錄
path.glob("*.py")      # 搜尋
```

## Common Patterns 常見模式

### Walrus Operator 海象運算子（Python 3.8+）

```python
if (n := len(data)) > 10:
    print(f"Too long: {n}")
```

### Sorted Key 排序鍵

```python
sorted(list, key=lambda x: x[1])    # 依第二個元素排序
sorted(list, key=lambda x: abs(x))  # 依絕對值排序
sorted(list, key=str.lower)         # 忽略大小寫排序
```

### Collections 模組

```python
from collections import Counter, defaultdict, deque, namedtuple

Counter("abracadabra")              # 計算次數
defaultdict(int)                    # 預設值字典
deque([1, 2, 3])                    # 雙端佇列
Point = namedtuple("Point", "x y")  # 命名元組
```

### Enum 枚舉

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

### 上下文管理器

```python
class MyContext:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
```
