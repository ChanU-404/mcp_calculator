from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider


public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1E5a4/40rutB2CUNwHuP
cdWMtIWNwI5gXBp4I5TaLDV4EMW1fEtFW3PnEkgplB2G11d+nx/MPmTn9HXHJtQ1
YxVAslUj8795k7pF/1fr0kp+6j59SFASZywkuE1Cy+rV2EN+au/PlkkIVFxkuc4f
UYga34zXEdpl/+wSFOLJ5iJWrVzigJi4z9jGnr88TAc2pWswIVMFnm2ouYAGNNcS
6Qb70Yg2F1CaQYhdZOx17jVo0phR8mNAkjE5LwU8dx2xpLXTWRwqAAcj7wYa8m7V
rvYlgvPFOFlSwF0acErbXSykvpQtmfeYo/iIlrRZ2V5h4/IhZKOAdukq8P1ZqrIu
IwIDAQAB
-----END PUBLIC KEY-----"""



auth = BearerAuthProvider(
    public_key=public_key,
    issuer="https://dev.example.com",
    audience="calculator"
)

#mcp = FastMCP(name="calculator", auth=auth)
mcp  = FastMCP(name="calculator")

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    print(f"원격 MCP 서버: Multiplying {a} and {b}")
    return a * b

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        path="/",
        log_level="debug",
    )
