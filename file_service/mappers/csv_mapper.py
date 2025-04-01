class ProductCsvMapper:
    def __init__(self, row: dict):
        self.row = row

    def to_nested_dict(self) -> dict:
        return {
            "name": self.row["name"],
            "stock": {
                "price": self._parse_decimal(self.row["price"])
            },
            "batch": [{
                "quantity": self._parse_int(self.row["quantity"]),
                "validity": self._parse_date(self.row.get("validity"))
            }]
        }
    
    def _parse_decimal(self, value):
        try:
            return float(value)
        except:
            raise ValueError(f"Invalid decimal: {value}")

    def _parse_int(self, value):
        try:
            return int(value)
        except:
            raise ValueError(f"Invalid integer: {value}")

    def _parse_date(self, value):
        if not value:
            return None
        try:
            return value
        except:
            raise ValueError(f"Invalid date: {value}")
