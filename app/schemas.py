from pydantic import BaseModel, Field, field_validator


class OperationRequest(BaseModel):
    wallet_name: str = Field(..., max_lenght=27)
    amount: float
    description: str | None = Field(None, max_lenght=255)

    @field_validator('amount')
    def amount_must_be_positive(cls, value: float) -> float:
        if value < 0:
            raise ValueError('Amount must be positive')

        return value

    @field_validator('wallet_name')
    def wallet_name_not_empty(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError('Wallet name can not be empty')

        return value


class CreateWalletRequest(BaseModel):
    name: str = Field(..., max_lenght=27)
    initial_balance: float = 0

    @field_validator('name')
    def name_not_empty(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError('Name can not be empty')

        return value

    @field_validator('initial_balance')
    def balance_not_negative(cls, value: float) -> float:
        if value < 0:
            raise ValueError('Initial balance can not be negative')

        return value
