# Calculator Sample

A lightweight Python calculator library supporting basic arithmetic operations with robust edge case handling.

## Features

- **Operations**: Addition, subtraction, multiplication, division
- **Edge Cases**: Handles divide by zero (raises `ValueError`), decimals, negatives, large numbers, and infinity
- **Type Safety**: Uses type hints for better code quality
- **Testing**: Comprehensive unit tests with pytest (100% coverage)

## Installation

```bash
pip install -e .
```

## Usage

```python
from calculator import add, subtract, multiply, divide

result = add(5, 3)        # 8
result = divide(10, 2)    # 5.0
result = multiply(4, 0.5) # 2.0
```

## Testing

Run tests with coverage:

```bash
pytest tests/ --cov=calculator --cov-report=term-missing
```

## Project Structure

- `calculator/core.py`: Core arithmetic functions
- `tests/test_calculator.py`: Unit tests
- `pyproject.toml`: Configuration for pytest and coverage

## License

MIT
