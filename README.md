# MCP Server – Calculator 🧮

A lightweight **Model Context Protocol (MCP)** server that exposes basic
calculator operations (add, subtract, multiply, divide, power, sqrt, modulo)
via the **streamable-http** transport.

Built with [FastMCP](https://github.com/modelcontextprotocol/python-sdk) for
maximum compatibility with MCP-enabled AI agents and gateways.

## Quick Start

```bash
# Install
pip install -e .

# Run (streamable-http on port 8000)
mcp-server-calculator
```

The server listens on `http://0.0.0.0:8000/mcp` by default.

## Available Tools

| Tool       | Description                        |
|------------|------------------------------------|
| `add`      | Add two numbers                    |
| `subtract` | Subtract b from a                  |
| `multiply` | Multiply two numbers               |
| `divide`   | Divide a by b (guards zero)        |
| `power`    | Raise base to the power of exponent|
| `sqrt`     | Square root of a non-negative num  |
| `modulo`   | Remainder of a divided by b        |

## Environment Variable Overrides

| Variable        | Default              |
|-----------------|----------------------|
| `MCP_TRANSPORT` | `streamable-http`    |
| `MCP_HOST`      | `0.0.0.0`           |
| `MCP_PORT`      | `8000`              |

## License

MIT
