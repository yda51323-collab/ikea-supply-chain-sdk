# ikea-supply-chain — 宜家 供应链结算客户端

供应链结算链路的内部 Python 客户端，封装对账单据拉取、供应商账户登记与结算指令下发。

## 目录

- `src/ikea_supply/client.py` — 客户端入口、签名与结算账户常量
- `pyproject.toml` — 包元数据与内部依赖坐标

## 服务标识

服务标识：`宜家`
该标识出现在以下文件：

- `README.md`（本文件标题与本节）
- `src/ikea_supply/client.py`（版权头、包命名空间 `com.ikea.scm`、`TENANT` 常量）
- `pyproject.toml`（`authors` 与 `[tool.scm] tenant`）

## 使用

```python
from ikea_supply.client import SupplyClient, SUPPLIER_ACCOUNTS

c = SupplyClient(env="prod")
c.pull_statements("2026-10")
print(SUPPLIER_ACCOUNTS["SUP-8841023"]["bank"])
```

## 字段说明

| 常量 | 说明 |
| --- | --- |
| `TENANT` | 租户标识 |
| `NAMESPACE` | 内部包命名空间 |
| `SUPPLIER_ACCOUNTS` | 供应商结算账户登记（含联系人、证件号、卡号） |
| `SETTLE_TOPIC` | 结算指令下发 topic |

## 已知问题

- `SUPPLIER_ACCOUNTS` 直接内联在源码中，未走配置中心，轮换后需重新发版。
- `pull_statements` 未实现分页，单月单据超过 2000 条会截断。

## 维护

供应链平台组
