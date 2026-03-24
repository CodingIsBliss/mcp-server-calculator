"""MCP Calculator Server – exposes basic math tools over streamable-http."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator", host="0.0.0.0", port=8000)


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Returns an error message when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base**exponent


@mcp.tool()
def sqrt(a: float) -> float:
    """Return the square root of a non-negative number."""
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return a**0.5


@mcp.tool()
def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot compute modulo with zero divisor")
    return a % b


def main():
    """Entry-point used by the console-script."""
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
